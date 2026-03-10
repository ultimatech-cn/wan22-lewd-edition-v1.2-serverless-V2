# WAN 2.2 Lewd Edition v1.2 Project Status

## Current Goal

Deploy `WAN 2.2 Lewd Edition v1.2.json` as a RunPod serverless project today.

## Source Files

- Workflow: `project-inputs/workflow.json`
- Model manifest draft: `project-config/model-manifest.txt`
- Custom nodes draft: `project-config/custom-nodes.txt`
- Dependency review sheet: `templates/serverless-project/02_dependencies.md`

## Model Source Strategy

Use Hugging Face first when possible.

Primary mirror provided by user:

- `https://huggingface.co/datasets/Robin9527/LoRA/tree/main/Wan22`

Reason:

- RunPod can download any public direct file URL that `curl/wget` can access.
- Hugging Face is more stable and easier to reproduce than mixed Civitai page links.

## Current Manifest State

`project-config/model-manifest.txt` has now been switched to a Hugging Face first strategy.

There are two classes of entries inside it:

- direct-confidence links: exact or near-exact links already known
- approximate mappings: workflow filename is mapped to the closest Hugging Face mirror filename for deployment-first testing

## Direct Or Near-Direct Links

These are the stronger links currently in `model-manifest.txt`:

- `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors`
- `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors`
- `wan_2.1_vae.safetensors`
- `Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors`
- `v2 low_noise_model_rank64.safetensors`
- `DR34ML4Y_I2V_14B_HIGH.safetensors`

## Approximate Hugging Face Mappings

These are deployment-first substitutions and should be verified with output quality:

- `BounceHighWan2_2.safetensors` -> `mql_massage_tits_wan22_i2v_v1_high_noise.safetensors`
- `BounceLowWan2_2.safetensors` -> `mql_massage_tits_wan22_i2v_v1_low_noise.safetensors`
- `DR34ML4Y_I2V_14B_LOW.safetensors` -> `DR34MJOB_I2V_14b_LowNoise.safetensors`
- `slop_twerk_HighNoise_merged3_7_v2.safetensors` -> `wan22-jellyhips-i2v-13epoc-high-k3nk.safetensors`
- `slop_twerk_LowNoise_merged3_7_v2.safetensors` -> `wan22-jellyhips-i2v-23epoc-low-k3nk.safetensors`
- `Wan2.2 - I2V - Gyrating Hips - HIGH 14B.safetensors` -> `wan22-jellyhips-i2v-13epoc-high-k3nk.safetensors`
- `Wan2.2 - I2V - Gyrating Hips - LOW 14B.safetensors` -> `wan22-jellyhips-i2v-23epoc-low-k3nk.safetensors`
- `Wan22-I2V-HIGH-Hip_Slammin_Assertive_Cowgirl.safetensors` -> `Wan2.2 - I2V - Doggy Style - 14B_high_noise.safetensors`
- `Wan22-I2V-LOW-Hip_Slammin_Assertive_Cowgirl.safetensors` -> `Wan2.2 - I2V - Doggy Style - 14B_low_noise.safetensors`
- `wan22-ultimatedeepthroat-I2V-101epoc-low-k3nk.safetensors` -> `wan2.2-i2v-low-oral-insertion-v1.0.safetensors`
- `wan22-ultimatedeepthroat-I2V-34epoc-high-k3nk.safetensors` -> `wan2.2-i2v-high-oral-insertion-v1.0.safetensors`
- `wan_fingering_pussy_i2v2.2hi_v10.safetensors` -> `fingering_i2v_e248.safetensors`
- `wan_fingering_pussy_i2v2.2lo_v10.safetensors` -> `fingering_for_wan_v1.0_e184.safetensors`

## Custom Nodes

Current custom node set is already consolidated in `project-config/custom-nodes.txt`.
No unresolved custom node repository is blocking the project right now.

## Immediate Next Steps

1. Download all required models to the RunPod volume.
2. Run one local or containerized validation pass with these approximate LoRA mappings.
3. Replace any obviously wrong LoRA with a better HF mirror after the first output check.
4. Check whether any custom node repo needs a pinned branch or commit.
5. Deploy to RunPod serverless and test with Postman.

## Operational Notes

- Use a temporary Pod with an explicitly mounted Network Volume at `/runpod-volume`.
- Do not use a community ComfyUI Pod that only mounts `/workspace` to pre-download models.
- All `/runpod-volume` commands run inside the RunPod Linux container shell, not local PowerShell.
- Some Hugging Face dataset links may require auth or trigger CAS-style restrictions.
- If a model returns `401` or `403`, retry with `HF_TOKEN` or manually upload the file to `/runpod-volume/models/...`.
