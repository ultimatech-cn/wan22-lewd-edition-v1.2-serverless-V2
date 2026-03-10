# 02 依赖清单

## 模型清单

| 模型文件名 | 类型 | 下载链接 | 目标路径 | 是否必须 | 备注 |
| --- | --- | --- | --- | --- | --- |
| umt5_xxl_fp8_e4m3fn_scaled.safetensors | clip | https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors | clip | 是 | 推荐来源: explicit; 置信度: high; 来源节点: CLIPLoader |
| BounceHighWan2_2.safetensors | lora | https://huggingface.co/yeqiu168182/BounceHighWan2_2 | loras/WAN | 是 | 推荐来源: Hugging Face; 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| BounceLowWan2_2.safetensors | lora | https://huggingface.co/yeqiu168182/BounceLowWan2_2 | loras/WAN | 是 | 推荐来源: Hugging Face; 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| DR34ML4Y_I2V_14B_HIGH.safetensors | lora | https://civitai.com/api/download/models/2176505 | loras/TODO-family | 是 | 推荐来源: Note Link (Civitai); 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| DR34ML4Y_I2V_14B_LOW.safetensors | lora | https://huggingface.co/yeqiu168182/DR34ML4Y_I2V_14B_LOW | loras/TODO-family | 是 | 推荐来源: Hugging Face; 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| slop_twerk_HighNoise_merged3_7_v2.safetensors | lora | https://civitai.com/api/download/models/2273468 | loras/TODO-family | 是 | 推荐来源: Note Link (Civitai); 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| slop_twerk_LowNoise_merged3_7_v2.safetensors | lora |  | loras/TODO-family | 是 | 需人工核对; 来源节点: LoraLoaderModelOnly |
| v2 low_noise_model_rank64.safetensors | lora | https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/resolve/main/loras/low_noise_model_rank64.safetensors | loras/TODO-family | 是 | 推荐来源: Note Link (HF); 置信度: medium; 需人工核对; 来源节点: LoraLoaderModelOnly |
| Wan2.2 - I2V - Gyrating Hips - HIGH 14B.safetensors | lora |  | loras/WAN | 是 | 需人工核对; 来源节点: LoraLoaderModelOnly |
| Wan2.2 - I2V - Gyrating Hips - LOW 14B.safetensors | lora |  | loras/WAN | 是 | 需人工核对; 来源节点: LoraLoaderModelOnly |
| Wan22-I2V-HIGH-Hip_Slammin_Assertive_Cowgirl.safetensors | lora | https://civitai.com/api/download/models/2129122 | loras/WAN | 是 | 推荐来源: Note Link (Civitai); 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| Wan22-I2V-LOW-Hip_Slammin_Assertive_Cowgirl.safetensors | lora |  | loras/WAN | 是 | 需人工核对; 来源节点: LoraLoaderModelOnly |
| wan22-ultimatedeepthroat-I2V-101epoc-low-k3nk.safetensors | lora | https://huggingface.co/Dgwilso/wan22-ultimatedeepthroat-I2V-101epoc-low-k3nk.safetensors | loras/WAN | 是 | 推荐来源: Hugging Face; 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| wan22-ultimatedeepthroat-I2V-34epoc-high-k3nk.safetensors | lora | https://huggingface.co/yeqiu168182/wan22-ultimatedeepthroat-I2V-34epoc-high-k3nk | loras/WAN | 是 | 推荐来源: Hugging Face; 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors | lora | https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors | loras/WAN | 是 | 推荐来源: Note Link (HF); 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| wan_fingering_pussy_i2v2.2hi_v10.safetensors | lora |  | loras/WAN | 是 | 需人工核对; 来源节点: LoraLoaderModelOnly |
| wan_fingering_pussy_i2v2.2lo_v10.safetensors | lora | https://civitai.com/api/download/models/2272102 | loras/WAN | 是 | 推荐来源: Note Link (Civitai); 置信度: high; 需人工核对; 来源节点: LoraLoaderModelOnly |
| wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors | unet | https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors | unet | 是 | 推荐来源: explicit; 置信度: high; 来源节点: UNETLoader |
| wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors | unet | https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors | unet | 是 | 推荐来源: explicit; 置信度: high; 来源节点: UNETLoader |
| wan_2.1_vae.safetensors | vae | https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors | vae | 是 | 推荐来源: explicit; 置信度: high; 来源节点: VAELoader |

## 自定义节点清单

| 节点名称 | 仓库地址 | 版本要求 | 安装方式 | 额外依赖 | 是否必须 |
| --- | --- | --- | --- | --- | --- |
| Any Switch (rgthree) | https://github.com/rgthree/rgthree-comfy |  | git:https://github.com/rgthree/rgthree-comfy | high | 是 |
| ColorMatch | https://github.com/WASasquatch/was-node-suite-comfyui |  | git:https://github.com/WASasquatch/was-node-suite-comfyui | high | 是 |
| CRTFirstLastFrameSelector | https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes |  | git:https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes | high | 是 |
| DownloadAndLoadGIMMVFIModel | https://github.com/kijai/ComfyUI-GIMM-VFI |  | git:https://github.com/kijai/ComfyUI-GIMM-VFI | high | 是 |
| easy cleanGpuUsed | https://github.com/yolain/ComfyUI-Easy-Use |  | git:https://github.com/yolain/ComfyUI-Easy-Use | high | 是 |
| Fast Groups Bypasser (rgthree) | https://github.com/rgthree/rgthree-comfy |  | git:https://github.com/rgthree/rgthree-comfy | high | 是 |
| GIMMVFI_interpolate | https://github.com/kijai/ComfyUI-GIMM-VFI |  | git:https://github.com/kijai/ComfyUI-GIMM-VFI | high | 是 |
| Label (rgthree) | https://github.com/rgthree/rgthree-comfy |  | git:https://github.com/rgthree/rgthree-comfy | high | 是 |
| MarkdownNote | https://github.com/pythongosssss/ComfyUI-Custom-Scripts |  | git:https://github.com/pythongosssss/ComfyUI-Custom-Scripts | high | 是 |
| PathchSageAttentionKJ | https://github.com/kijai/ComfyUI-KJNodes |  | git:https://github.com/kijai/ComfyUI-KJNodes | high | 是 |
| Resolution | https://github.com/pythongosssss/ComfyUI-Custom-Scripts |  | git:https://github.com/pythongosssss/ComfyUI-Custom-Scripts | high | 是 |
| SetNode | https://github.com/WASasquatch/was-node-suite-comfyui |  | git:https://github.com/WASasquatch/was-node-suite-comfyui | high | 是 |
| VHS_LoadVideoPath | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |  | git:https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite | high | 是 |
| VHS_SelectLatest | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |  | git:https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite | high | 是 |
| VHS_VideoCombine | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |  | git:https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite | high | 是 |
| WanImageToVideo | https://github.com/Wan-Video/ComfyUI-Wan-Node |  | git:https://github.com/Wan-Video/ComfyUI-Wan-Node | high | 是 |

## Python 依赖

| 包名 | 版本 | 用途 | 是否已在 requirements 中 |
| --- | --- | --- | --- |
| | | | |

## 系统依赖

| 依赖 | 用途 | 是否需要写入 Dockerfile |
| --- | --- | --- |
| ffmpeg | 视频读写或帧处理 | 是 |

## 环境变量

| 变量名 | 说明 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| | | | | |

## 外部服务

| 服务 | 用途 | 是否必须 | 备注 |
| --- | --- | --- | --- |
| | | | |

## 依赖总结

- 已识别模型: 20
- 已识别自定义节点: 16
- 待补模型链接: slop_twerk_LowNoise_merged3_7_v2.safetensors, Wan2.2 - I2V - Gyrating Hips - HIGH 14B.safetensors, Wan2.2 - I2V - Gyrating Hips - LOW 14B.safetensors, Wan22-I2V-LOW-Hip_Slammin_Assertive_Cowgirl.safetensors, wan_fingering_pussy_i2v2.2hi_v10.safetensors
