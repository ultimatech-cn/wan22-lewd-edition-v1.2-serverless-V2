#!/usr/bin/env python3
"""Generate client-facing RunPod test payloads from the current working workflow."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "project-inputs" / "WAN 2.2 Lewd Edition v1.2_runsync.json"
OUT_DIR = ROOT / "project-inputs" / "client-combos"

PLACEHOLDER_IMAGE_URL = "https://example.com/replace-with-your-input-image.png"
PLACEHOLDER_IMAGE_NAME = "client_input.png"
NEGATIVE_PROMPT = (
    "low quality, worst quality, blurry details, jpeg artifacts, bad anatomy, "
    "deformed body, deformed face, bad hands, extra fingers, fused fingers, "
    "extra limbs, duplicate body parts, face drift, identity change, static frame, "
    "stiff motion, frame jitter, camera shake, cluttered background, crowd, "
    "upside down motion, slow motion, slow, talking"
)

# Positive prompt node in the current workflow
PROMPT_NODE_ID = "13"
# Negative prompt node in the current workflow
NEGATIVE_PROMPT_NODE_ID = "6"
# LoadImage node in the current workflow
LOAD_IMAGE_NODE_ID = "14"
TITLE_FIXUPS = {
    "Video Combine 馃帴馃叆馃厳馃參": "Video Combine",
}

CORE_LORA_NODE_IDS = {"63", "64"}
GROUPS = {
    "general_nsfw": {"75", "76", "78"},
    "boob_butt_jiggle": {"68", "69", "70", "71", "80", "81"},
    "hip_slam": {"73", "74", "79"},
    "deepthroat": {"97", "98", "99"},
    "fingering": {"135", "136", "137"},
    "gyrating_hips": {"138", "139", "140"},
}

SCENARIOS = [
    {
        "slug": "01_base_lightning_only",
        "prompt": "The woman is doing a happy playful dance while looking at the viewer",
        "groups": [],
        "notes": "Base test with only the core Lightning LoRAs enabled.",
    },
    {
        "slug": "02_general_nsfw",
        "prompt": "The woman is doing a happy playful dance while looking at the viewer",
        "groups": ["general_nsfw"],
        "notes": "General NSFW stack only.",
    },
    {
        "slug": "03_bounce_and_twerk",
        "prompt": "The woman is dancing with energetic breast and hip motion while looking at the viewer",
        "groups": ["boob_butt_jiggle"],
        "notes": "Bounce plus twerk stack only.",
    },
    {
        "slug": "04_hip_slam",
        "prompt": "The woman is performing an assertive hip-slam style riding motion while looking at the viewer",
        "groups": ["hip_slam"],
        "notes": "Hip Slam stack only.",
    },
    {
        "slug": "05_deepthroat",
        "prompt": "The woman is performing a deepthroat blowjob motion while looking at the viewer",
        "groups": ["deepthroat"],
        "notes": "Deepthroat stack only.",
    },
    {
        "slug": "06_fingering",
        "prompt": "The woman is performing a fingering motion while looking at the viewer",
        "groups": ["fingering"],
        "notes": "Fingering stack only.",
    },
    {
        "slug": "07_gyrating_hips",
        "prompt": "The woman is doing a gyrating hips motion while looking at the viewer",
        "groups": ["gyrating_hips"],
        "notes": "Gyrating Hips stack only.",
    },
    {
        "slug": "08_full_current_stack",
        "prompt": "The woman is doing a happy playful dance while looking at the viewer",
        "groups": list(GROUPS.keys()),
        "notes": "Matches the current full feature stack for broad smoke testing.",
    },
    {
        "slug": "09_face_locked_zoomout_safe",
        "prompt": (
            "4.8s seamless POV loop. Starts as the exact reference headshot of the woman, "
            "face perfectly locked, warm eager eye contact. 0.0-0.9s: smooth cinematic "
            "zoom-out into a softly lit bedroom. 0.9-1.5s: outfit transitions quickly into "
            "elegant minimal sleepwear with natural cloth motion. 1.5-4.8s: full body woman "
            "kneeling on the floor in front of the viewer, gentle body sway, natural breathing, "
            "soft shoulder and hair motion, affectionate upward gaze, subtle smile, photoreal 8k, "
            "perfect face likeness, clean motion, stable anatomy, realistic skin texture."
        ),
        "groups": [],
        "notes": "Safe face-lock and zoom-out workflow using only the core Lightning LoRAs.",
    },
]


def load_source() -> dict:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    if "input" in data:
        return data
    return {
        "input": {
            "images": [
                {
                    "name": PLACEHOLDER_IMAGE_NAME,
                    "image": PLACEHOLDER_IMAGE_URL,
                }
            ],
            "workflow": data,
        }
    }


def set_enabled_groups(workflow: dict, enabled_groups: list[str]) -> None:
    enabled_nodes = set(CORE_LORA_NODE_IDS)
    for group in enabled_groups:
        enabled_nodes.update(GROUPS[group])

    for node_id, node in workflow.items():
        inputs = node.get("inputs", {})
        if "lora_name" not in inputs:
            continue
        if node_id in enabled_nodes:
            continue
        inputs["strength_model"] = 0


def normalize_meta_titles(workflow: dict) -> None:
    for node in workflow.values():
        if not isinstance(node, dict):
            continue
        meta = node.get("_meta")
        if not isinstance(meta, dict):
            continue
        title = meta.get("title")
        if isinstance(title, str) and title in TITLE_FIXUPS:
            meta["title"] = TITLE_FIXUPS[title]


def customize_payload(base_payload: dict, scenario: dict) -> dict:
    payload = deepcopy(base_payload)
    workflow = payload["input"]["workflow"]

    payload["input"]["images"] = [
        {
            "name": PLACEHOLDER_IMAGE_NAME,
            "image": PLACEHOLDER_IMAGE_URL,
        }
    ]

    workflow[PROMPT_NODE_ID]["inputs"]["text"] = scenario["prompt"]
    workflow[NEGATIVE_PROMPT_NODE_ID]["inputs"]["text"] = NEGATIVE_PROMPT
    workflow[LOAD_IMAGE_NODE_ID]["inputs"]["image"] = PLACEHOLDER_IMAGE_NAME
    normalize_meta_titles(workflow)
    set_enabled_groups(workflow, scenario["groups"])
    return payload


def build_manifest() -> str:
    lines = [
        "# Client Test Payload Matrix",
        "",
        "These payloads are generated from the current working WAN 2.2 RunPod workflow.",
        "",
        "Before sending any payload:",
        "",
        "1. Replace `input.images[0].image` with a real image URL or base64 image.",
        "2. If needed, replace `input.images[0].name` and keep the same filename in workflow node `14`.",
        "3. Replace the prompt in node `13` if you want a different scene description.",
        "",
        "| File | Enabled feature groups | Notes |",
        "| --- | --- | --- |",
    ]
    for scenario in SCENARIOS:
        groups = ", ".join(scenario["groups"]) if scenario["groups"] else "core_lightning_only"
        lines.append(f"| `{scenario['slug']}.json` | `{groups}` | {scenario['notes']} |")
    lines.append("")
    lines.append("Core LoRAs that remain enabled in all payloads:")
    lines.append("")
    lines.append("- `WAN/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors`")
    lines.append("- `WAN/v2 low_noise_model_rank64.safetensors`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    base_payload = load_source()

    for scenario in SCENARIOS:
        payload = customize_payload(base_payload, scenario)
        out_path = OUT_DIR / f"{scenario['slug']}.json"
        out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    manifest_path = OUT_DIR / "README.md"
    manifest_path.write_text(build_manifest() + "\n", encoding="utf-8")
    print(OUT_DIR)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
