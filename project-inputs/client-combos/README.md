# Client Test Payload Matrix

These payloads are generated from the current working WAN 2.2 RunPod workflow.

Before sending any payload:

1. Replace `input.images[0].image` with a real image URL or base64 image.
2. If needed, replace `input.images[0].name` and keep the same filename in workflow node `14`.
3. Replace the prompt in node `13` if you want a different scene description.

| File | Enabled feature groups | Notes |
| --- | --- | --- |
| `01_base_lightning_only.json` | `core_lightning_only` | Base test with only the core Lightning LoRAs enabled. |
| `02_general_nsfw.json` | `general_nsfw` | General NSFW stack only. |
| `03_bounce_and_twerk.json` | `boob_butt_jiggle` | Bounce plus twerk stack only. |
| `04_hip_slam.json` | `hip_slam` | Hip Slam stack only. |
| `05_deepthroat.json` | `deepthroat` | Deepthroat stack only. |
| `06_fingering.json` | `fingering` | Fingering stack only. |
| `07_gyrating_hips.json` | `gyrating_hips` | Gyrating Hips stack only. |
| `08_full_current_stack.json` | `general_nsfw, boob_butt_jiggle, hip_slam, deepthroat, fingering, gyrating_hips` | Matches the current full feature stack for broad smoke testing. |
| `09_face_locked_zoomout_safe.json` | `core_lightning_only` | Safe face-lock and zoom-out workflow using only the core Lightning LoRAs. |

Core LoRAs that remain enabled in all payloads:

- `WAN/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors`
- `WAN/v2 low_noise_model_rank64.safetensors`

