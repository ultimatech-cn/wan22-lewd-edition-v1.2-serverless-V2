# Client Test Payload Matrix

These payloads are generated from the current working WAN 2.2 RunPod workflow.

Before sending any payload:

1. Replace `input.images[0].image` with a real image URL or base64 image.
2. If needed, replace `input.images[0].name` and keep the same filename in workflow node `14`.
3. Replace the prompt in node `13` if you want a different scene description.

| File | Output | Enabled feature groups | Notes |
| --- | --- | --- | --- |
| `01_base_lightning_only_video.json` | `video` | `core_lightning_only` | Base test with only the core Lightning LoRAs enabled. H.264 MP4 output. |
| `01_base_lightning_only_gif.json` | `gif` | `core_lightning_only` | Base test with only the core Lightning LoRAs enabled. GIF output. |
| `02_general_nsfw_video.json` | `video` | `general_nsfw` | General NSFW stack only. H.264 MP4 output. |
| `02_general_nsfw_gif.json` | `gif` | `general_nsfw` | General NSFW stack only. GIF output. |
| `03_bounce_and_twerk_video.json` | `video` | `boob_butt_jiggle` | Bounce plus twerk stack only. H.264 MP4 output. |
| `03_bounce_and_twerk_gif.json` | `gif` | `boob_butt_jiggle` | Bounce plus twerk stack only. GIF output. |
| `04_hip_slam_video.json` | `video` | `hip_slam` | Hip Slam stack only. H.264 MP4 output. |
| `04_hip_slam_gif.json` | `gif` | `hip_slam` | Hip Slam stack only. GIF output. |
| `05_deepthroat_video.json` | `video` | `deepthroat` | Deepthroat stack only. H.264 MP4 output. |
| `05_deepthroat_gif.json` | `gif` | `deepthroat` | Deepthroat stack only. GIF output. |
| `06_fingering_video.json` | `video` | `fingering` | Fingering stack only. H.264 MP4 output. |
| `06_fingering_gif.json` | `gif` | `fingering` | Fingering stack only. GIF output. |
| `07_gyrating_hips_video.json` | `video` | `gyrating_hips` | Gyrating Hips stack only. H.264 MP4 output. |
| `07_gyrating_hips_gif.json` | `gif` | `gyrating_hips` | Gyrating Hips stack only. GIF output. |
| `08_full_current_stack_video.json` | `video` | `general_nsfw, boob_butt_jiggle, hip_slam, deepthroat, fingering, gyrating_hips` | Matches the current full feature stack for broad smoke testing. H.264 MP4 output. |
| `08_full_current_stack_gif.json` | `gif` | `general_nsfw, boob_butt_jiggle, hip_slam, deepthroat, fingering, gyrating_hips` | Matches the current full feature stack for broad smoke testing. GIF output. |
| `09_face_locked_zoomout_safe_video.json` | `video` | `core_lightning_only` | Safe face-lock and zoom-out workflow using only the core Lightning LoRAs. H.264 MP4 output. |
| `09_face_locked_zoomout_safe_gif.json` | `gif` | `core_lightning_only` | Safe face-lock and zoom-out workflow using only the core Lightning LoRAs. GIF output. |

Core LoRAs that remain enabled in all payloads:

- `WAN/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors`
- `WAN/v2 low_noise_model_rank64.safetensors`

