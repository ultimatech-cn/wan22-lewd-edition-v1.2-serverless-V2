# Client Guide Delta for This Project

This file explains how the client-provided deployment guide maps to the current repository.

The client PDF is a generic ComfyUI-on-RunPod guide. This repository already has a working deployment path and should not blindly copy the guide's example handler logic.

## Keep As-Is

- `handler.py` already accepts RunPod serverless input in the form:

```json
{
  "input": {
    "workflow": {},
    "images": [
      {
        "name": "input.png",
        "image": "data:image/png;base64,..."
      }
    ]
  }
}
```

- `handler.py` already supports:
  - `workflow`
  - optional `images`
  - image URL to base64 conversion
  - image and video output collection

- `src/start.sh` already handles model mounting from Network Volume into `/comfyui/models/...` using symlinks at container startup.

- Custom nodes are installed into the image at build time by `Dockerfile` plus `install-custom-nodes.sh`.

## Do Not Copy Directly From the Client Guide

### 1. Category-Based LoRA Helper

The client guide shows a generic helper that enables LoRAs by category names such as:

- `general_nsfw`
- `fingering`
- `boob_jiggle`

This repository does not expose that abstraction in the server handler.

Current behavior:

- LoRA selection is controlled directly in the workflow JSON.
- The working workflow uses explicit `LoraLoaderModelOnly` nodes and concrete `lora_name` values.
- For this project, LoRA filenames under the mounted volume must match the actual ComfyUI model paths, for example `WAN/...` where applicable.

### 2. Output Shape Examples

The client guide uses a simplified response example like:

```json
{
  "status": "COMPLETED",
  "output": [
    {
      "base64": "..."
    }
  ]
}
```

This project's actual handler returns media entries under `output.images`.

Typical current response shape:

```json
{
  "status": "COMPLETED",
  "output": {
    "message": "Job completed successfully.",
    "images": [
      {
        "filename": "WAN_00001.mp4",
        "type": "base64",
        "data": "data:video/mp4;base64,..."
      }
    ]
  }
}
```

Notes:

- Videos may be returned as `data:video/mp4;base64,...`
- Images may be returned as `data:image/...;base64,...`
- Some outputs may be returned as URLs instead of base64 depending on storage configuration

### 3. Dockerfile Example

The client guide shows a minimal sample image based on older defaults.

This repository already has project-specific image logic:

- custom node installation
- startup orchestration
- offline ComfyUI-Manager mode
- Network Volume model linking
- ffmpeg and build dependencies required by the working workflow

Do not replace the current `Dockerfile` with the generic sample from the client guide.

## Canonical Contract for This Repo

### Request

Use:

```json
{
  "input": {
    "workflow": {},
    "images": []
  }
}
```

`images` is optional.

### Output

Read media from:

```json
output.images[]
```

Each media entry may contain:

- `filename`
- `type`
- `data`

If `data` starts with a data URI prefix, strip the prefix before base64-decoding.

## Recommended Testing Flow

1. Use a known-good `runsync` payload that already matches this handler contract.
2. Keep workflow node wiring changes outside the handler unless a real server-side gap is found.
3. Decode returned `output.images[*].data` with a helper script instead of manually copying long base64 strings.

## Included Helper

Use:

```bash
python scripts/extract-runpod-media.py output/output1.json
```

This extracts media from current handler responses and also supports the client's older simplified base64 response shape.
