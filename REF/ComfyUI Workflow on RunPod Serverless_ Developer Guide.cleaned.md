# ComfyUI Workflow on RunPod Serverless: Developer Guide

## Overview
This guide describes how to deploy a ComfyUI workflow on RunPod Serverless for NSFW video generation.

### API Inputs
- `prompt`: Text string describing the scene, for example `"Seductive woman in lingerie, high detail"`.
- `base64 image`: Base64-encoded input image used for conditioning or reference.
- `LoRA settings`: A list of categories to enable, for example `["boob_jiggle", "general_nsfw"]`.

Multiple LoRAs can be stacked by setting their strengths above `0`. Unused LoRAs are bypassed by setting strength to `0`.

### Output
- A base64-encoded 15-second video clip in `MP4` or `GIF` form.

### Deployment Model
- Single endpoint.
- Request payload is modified dynamically by a helper before submission.

### Prerequisites
- RunPod account and API key.
- Local ComfyUI installation for exporting `workflow_api.json`.
- LoRAs from CivitAI or Hugging Face.
- Custom nodes such as AnimateDiff, VideoHelperSuite, and a Base64 image handler.
- Docker.

## Setup Steps

### 1. Export Workflow JSON
- Recreate the workflow with:
  - Base model
  - Chained LoRA loaders
  - `CLIPTextEncode` for the prompt
  - A Base64 image input node
  - Sampler such as `ModelSamplingSD3`
  - Video generation for 15 seconds
- Export the workflow as `workflow_api.json`.
- Keep all LoRAs enabled in the exported workflow, and use `strength_model=0` in the API layer to bypass any LoRA you do not want to apply.

### 2. Build Docker Image

```dockerfile
FROM runpod/worker-comfyui:5.1.0-base

RUN comfy-node-install ComfyUI-AnimateDiff-Evolved ComfyUI-VideoHelperSuite ComfyUI-Manager ComfyUI-Base64-Images

RUN comfy model download --url https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors --relative-path models/checkpoints

# Download all LoRAs similarly
```

Build and push:

```bash
docker build -t yourusername/custom-comfy:1.0 .
docker push yourusername/custom-comfy:1.0
```

### 3. Deploy on RunPod
- In `Serverless > New Endpoint`, use your image.
- Recommended GPU in the document: `A100` with `24GB+`.
- Recommended disk size in the document: `50GB`.
- Use a network volume for models.
- Get the endpoint ID, for example `abc123`.

Example endpoint URL:

```text
https://api.runpod.ai/v2/abc123/runsync
```

### 4. Bypass Mechanism
Set `strength_model=0` in LoRA nodes to bypass them. This skips the LoRA adaptation and passes the base model through unchanged, similar to bypass behavior in the UI.

## Python Payload Helper
The helper handles prompt input, base64 image input, LoRA selection, and LoRA bypassing.

```python
import json


def prepare_payload(json_path, prompt, base64_img, loras=None):
    if isinstance(loras, str):
        loras = [loras]
    if not loras:
        loras = []

    with open(json_path, "r") as f:
        wf = json.load(f)

    wf["prompt_node"]["inputs"]["text"] = prompt
    wf["img_node"]["inputs"]["base64"] = base64_img

    category_strengths = {
        "general_nsfw": {
            "nodes": ["lora_general1", "lora_general2", "lora_general3"],
            "strengths": [1.0, 1.0, 1.0],
        },
        "fingering": {
            "nodes": ["lora_fingering1", "lora_fingering2", "lora_fingering3"],
            "strengths": [1.0, 1.0, 1.0],
        },
        "gyrating_hips": {
            "nodes": ["lora_gyrating1", "lora_gyrating2", "lora_gyrating3"],
            "strengths": [1.0, 1.0, 1.0],
        },
        "deepthroat_bj": {
            "nodes": ["lora_deepthroat1", "lora_deepthroat2", "lora_deepthroat3"],
            "strengths": [0.021, 0.028, 0.038],
        },
        "hip_slam": {
            "nodes": ["lora_hipslam1", "lora_hipslam2", "lora_hipslam3"],
            "strengths": [1.0, 1.0, 1.0],
        },
        "boob_jiggle": {
            "nodes": ["lora_boobjiggle1", "lora_boobjiggle2", "lora_boobjiggle3"],
            "strengths": [0.024, 0.038, 0.031],
        },
        "butt_jiggle": {
            "nodes": ["lora_buttjiggle1", "lora_buttjiggle2", "lora_buttjiggle3"],
            "strengths": [0.20, 0.20, 0.20],
        },
    }

    all_nodes = [n for cat in category_strengths.values() for n in cat["nodes"]]

    # Bypass all by default
    for node in all_nodes:
        wf[node]["inputs"]["strength_model"] = 0.0

    # Enable selected LoRAs
    for lora in loras:
        if lora in category_strengths:
            for i, node in enumerate(category_strengths[lora]["nodes"]):
                wf[node]["inputs"]["strength_model"] = category_strengths[lora]["strengths"][i]

    return {"input": {"workflow": wf}}
```

## Usage Examples

### Generate Payload

```python
payload = prepare_payload(
    "workflow_api.json",
    "NSFW scene with jiggle",
    "your_base64_image_string",
    ["boob_jiggle", "butt_jiggle"],
)
```

### Send Request in Python

```python
import base64
import requests

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}

response = requests.post(
    "https://api.runpod.ai/v2/abc123/runsync",
    json=payload,
    headers=headers,
)

video_base64 = response.json().get("output", [{}])[0].get("base64")

with open("output.mp4", "wb") as f:
    f.write(base64.b64decode(video_base64))
```

### curl Example
Generate the JSON with Python first, then send it with `curl`:

```bash
curl -X POST https://api.runpod.ai/v2/abc123/runsync \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d @payload.json
```

### Response Example

```json
{
  "status": "COMPLETED",
  "output": [
    {
      "base64": "UklGRi... (base64-encoded video clip)"
    }
  ]
}
```

## Testing with Postman
- Use `POST` against the endpoint.
- Put the helper-generated JSON in the raw request body.
- Set `Authorization: Bearer ...` and `Content-Type: application/json`.
- Extract the base64 video from the response.

## Example LoRA Scenarios

### 1. General NSFW

```text
curl -X POST https://api.runpod.ai/v2/abc123/runsync -H ... -d '{"input":{"workflow":{"prompt":{"text":"NSFW scene"},"img":{"base64":"..."},"lora_general1":{"strength_model":1.0}, ... // others 0 }}}'
```

Example response:

```json
{"output":[{"base64":"UklGRi..."}],"status":"COMPLETED"}
```

### 2. Fingering

```text
curl ... -d '{"input":{"workflow":{"prompt":{"text":"Fingering scene"},"img":{"base64":"..."},"lora_fingering1":{"strength_model":1.0}, ... // others 0 }}}'
```

Response is similar, with a tailored video.

### 3. Gyrating Hips

```text
curl ... -d '{"input":{"workflow":{"prompt":{"text":"Gyrating hips"},"img":{"base64":"..."},"lora_gyrating1":{"strength_model":1.0}, ... }}}'
```

Response is similar to the previous examples.

### 4. Deepthroat BJ

```text
curl ... -d '{"input":{"workflow":{"prompt":{"text":"Deepthroat BJ"},"img":{"base64":"..."},"lora_deepthroat1":{"strength_model":0.021},"lora_deepthroat2":{"strength_model":0.028},"lora_deepthroat3":{"strength_model":0.038}, ... }}}'
```

Response is standard.

### 5. Hip Slam

```text
curl ... -d '{"input":{"workflow":{"prompt":{"text":"Hip slam"},"img":{"base64":"..."},"lora_hipslam1":{"strength_model":1.0}, ... }}}'
```

Response returns a video output.

### 6. Boob Jiggle

```text
curl ... -d '{"input":{"workflow":{"prompt":{"text":"Boob jiggle"},"img":{"base64":"..."},"lora_boobjiggle1":{"strength_model":0.024},"lora_boobjiggle2":{"strength_model":0.038},"lora_boobjiggle3":{"strength_model":0.031}, ... }}}'
```

Response is similar to the previous examples.

### 7. Butt Jiggle

```text
curl ... -d '{"input":{"workflow":{"prompt":{"text":"Butt jiggle"},"img":{"base64":"..."},"lora_buttjiggle1":{"strength_model":0.20}, ... }}}'
```

Response completes normally.

### 8. No LoRA

```text
curl ... -d '{"input":{"workflow":{"prompt":{"text":"Base scene"},"img":{"base64":"..."},"lora_*":{"strength_model":0}}}}'
```

Response returns a base video.

## Troubleshooting
- Cold starts: refresh the worker.
- VRAM pressure: use a larger GPU for multi-LoRA workflows.
- Video length: adjust FPS or total frames in the workflow.
- LoRA conflicts: tune strengths if multiple LoRAs overlap.
