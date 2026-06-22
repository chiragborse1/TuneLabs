# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

"""Default model lists for inference, split by platform."""

import utils.hardware.hardware as hw

DEFAULT_MODELS_GGUF = [
    "tunelabs/Qwen3.6-27B-MTP-GGUF",
    "tunelabs/Qwen3.6-35B-A3B-MTP-GGUF",
    "tunelabs/gemma-4-E2B-it-GGUF",
    "tunelabs/gemma-4-E4B-it-GGUF",
    "tunelabs/gemma-4-31B-it-GGUF",
    "tunelabs/gemma-4-26B-A4B-it-GGUF",
    "tunelabs/Qwen3.5-4B-MTP-GGUF",
    "tunelabs/Qwen3.5-9B-MTP-GGUF",
    "tunelabs/Qwen3.5-35B-A3B-MTP-GGUF",
    "tunelabs/Qwen3.5-0.8B-MTP-GGUF",
    "tunelabs/Llama-3.2-1B-Instruct-GGUF",
    "tunelabs/Llama-3.2-3B-Instruct-GGUF",
    "tunelabs/Llama-3.1-8B-Instruct-GGUF",
    "tunelabs/gemma-3-1b-it-GGUF",
    "tunelabs/gemma-3-4b-it-GGUF",
    "tunelabs/Qwen3-4B-GGUF",
]

DEFAULT_MODELS_STANDARD = [
    "tunelabs/Qwen3.6-27B-MTP-GGUF",
    "tunelabs/Qwen3.6-35B-A3B-MTP-GGUF",
    "tunelabs/gemma-4-E2B-it-GGUF",
    "tunelabs/gemma-4-E4B-it-GGUF",
    "tunelabs/gemma-4-31B-it-GGUF",
    "tunelabs/gemma-4-26B-A4B-it-GGUF",
    "tunelabs/Qwen3.5-4B-MTP-GGUF",
    "tunelabs/Qwen3.5-9B-MTP-GGUF",
    "tunelabs/Qwen3.5-35B-A3B-MTP-GGUF",
    "tunelabs/Qwen3.5-0.8B-MTP-GGUF",
    "tunelabs/gemma-4-E2B-it",
    "tunelabs/gemma-4-E4B-it",
    "tunelabs/gemma-4-31B-it",
    "tunelabs/gemma-4-26B-A4B-it",
    "tunelabs/Qwen3-4B-Instruct-2507",
    "tunelabs/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
    "tunelabs/Mistral-Nemo-Instruct-2407-bnb-4bit",
    "tunelabs/Phi-3.5-mini-instruct",
    "tunelabs/Gemma-3-4B-it",
    "tunelabs/Qwen2-VL-2B-Instruct-bnb-4bit",
]


def get_default_models() -> list[str]:
    hw.get_device()  # ensures detect_hardware() has run
    if hw.CHAT_ONLY:
        return list(DEFAULT_MODELS_GGUF)
    return list(DEFAULT_MODELS_STANDARD)
