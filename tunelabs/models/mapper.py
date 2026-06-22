# Copyright 2023-present Daniel Han-Chen & the TuneLabs team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    "INT_TO_FLOAT_MAPPER",
    "FLOAT_TO_INT_MAPPER",
    "MAP_TO_TUNELABS_16bit",
    "FLOAT_TO_FP8_BLOCK_MAPPER",
    "FLOAT_TO_FP8_ROW_MAPPER",
]

__INT_TO_FLOAT_MAPPER = \
{
    "tunelabs/gemma-4-E2B-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-4-E2B-it",
        "google/gemma-4-E2B-it",
    ),
    "tunelabs/gemma-4-E4B-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-4-E4B-it",
        "google/gemma-4-E4B-it",
    ),
    "tunelabs/gemma-4-31B-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-4-31B-it",
        "google/gemma-4-31B-it",
    ),
    "tunelabs/gemma-4-26B-A4B-it" : (
        "tunelabs/gemma-4-26B-A4B-it",
        "google/gemma-4-26B-A4B-it",
    ),
    "tunelabs/gemma-4-E2B-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-4-E2B",
        "google/gemma-4-E2B",
    ),
    "tunelabs/gemma-4-E4B-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-4-E4B",
        "google/gemma-4-E4B",
    ),
    "tunelabs/gemma-4-31B-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-4-31B",
        "google/gemma-4-31B",
    ),
    "tunelabs/LFM2-1.2B-tunelabs-bnb-4bit" : (
        "tunelabs/LFM2-1.2B",
        "LiquidAI/LFM2-1.2B",
    ),

    "tunelabs/mistral-7b-bnb-4bit" : (
        "tunelabs/mistral-7b",
        "mistralai/Mistral-7B-v0.1",
    ),
    "tunelabs/llama-2-7b-bnb-4bit" : (
        "tunelabs/llama-2-7b",
        "meta-llama/Llama-2-7b-hf",
    ),
    "tunelabs/llama-2-13b-bnb-4bit" : (
        "tunelabs/llama-2-13b",
        "meta-llama/Llama-2-13b-hf",
    ),
    "tunelabs/codellama-34b-bnb-4bit" : (
        "codellama/CodeLlama-34b-hf",
    ),
    "tunelabs/zephyr-sft-bnb-4bit" : (
        "tunelabs/zephyr-sft",
        "HuggingFaceH4/mistral-7b-sft-beta",
    ),
    "tunelabs/tinyllama-bnb-4bit" : (
        "tunelabs/tinyllama",
        "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
    ),
    "tunelabs/tinyllama-chat-bnb-4bit" : (
        "tunelabs/tinyllama-chat",
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    ),
    "tunelabs/mistral-7b-instruct-v0.1-bnb-4bit" : (
        "tunelabs/mistral-7b-instruct-v0.1",
        "mistralai/Mistral-7B-Instruct-v0.1",
    ),
    "tunelabs/mistral-7b-instruct-v0.2-bnb-4bit" : (
        "tunelabs/mistral-7b-instruct-v0.2",
        "mistralai/Mistral-7B-Instruct-v0.2",
    ),
    "tunelabs/llama-2-7b-chat-bnb-4bit" : (
        "tunelabs/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "tunelabs/llama-2-7b-chat-bnb-4bit" : (
        "tunelabs/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "tunelabs/Mixtral-8x7B-v0.1-tunelabs-bnb-4bit" : (
        "tunelabs/Mixtral-8x7B-v0.1",
        "mistralai/Mixtral-8x7B-v0.1",
        "tunelabs/Mixtral-8x7B-v0.1-bnb-4bit",
    ),
    "tunelabs/Mixtral-8x7B-Instruct-v0.1-tunelabs-bnb-4bit" : (
        "tunelabs/Mixtral-8x7B-Instruct-v0.1",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "tunelabs/Mixtral-8x7B-Instruct-v0.1-bnb-4bit",
    ),
    "tunelabs/codellama-7b-bnb-4bit" : (
        "tunelabs/codellama-7b",
        "codellama/CodeLlama-7b-hf",
    ),
    "tunelabs/codellama-13b-bnb-4bit" : (
        "codellama/CodeLlama-13b-hf",
    ),
    "tunelabs/yi-6b-bnb-4bit" : (
        "tunelabs/yi-6b",
        "01-ai/Yi-6B",
    ),
    "tunelabs/solar-10.7b-bnb-4bit" : (
        "upstage/SOLAR-10.7B-v1.0",
    ),
    "tunelabs/gemma-7b-bnb-4bit" : (
        "tunelabs/gemma-7b",
        "google/gemma-7b",
    ),
    "tunelabs/gemma-2b-bnb-4bit" : (
        "tunelabs/gemma-2b",
        "google/gemma-2b",
    ),
    "tunelabs/gemma-7b-it-bnb-4bit" : (
        "tunelabs/gemma-7b-it",
        "google/gemma-7b-it",
    ),
    "tunelabs/gemma-2b-bnb-4bit" : (
        "tunelabs/gemma-2b-it",
        "google/gemma-2b-it",
    ),
    "tunelabs/mistral-7b-v0.2-bnb-4bit" : (
        "tunelabs/mistral-7b-v0.2",
        "alpindale/Mistral-7B-v0.2-hf",
    ),
    "tunelabs/gemma-1.1-2b-it-bnb-4bit" : (
        "tunelabs/gemma-1.1-2b-it",
        "google/gemma-1.1-2b-it",
    ),
    "tunelabs/gemma-1.1-7b-it-bnb-4bit" : (
        "tunelabs/gemma-1.1-7b-it",
        "google/gemma-1.1-7b-it",
    ),
    "tunelabs/Starling-LM-7B-beta" : (
        "tunelabs/Starling-LM-7B-beta",
        "Nexusflow/Starling-LM-7B-beta",
    ),
    "tunelabs/Hermes-2-Pro-Mistral-7B-bnb-4bit" : (
        "tunelabs/Hermes-2-Pro-Mistral-7B",
        "NousResearch/Hermes-2-Pro-Mistral-7B",
    ),
    "tunelabs/OpenHermes-2.5-Mistral-7B-bnb-4bit" : (
        "tunelabs/OpenHermes-2.5-Mistral-7B",
        "teknium/OpenHermes-2.5-Mistral-7B",
    ),
    "tunelabs/codegemma-2b-bnb-4bit" : (
        "tunelabs/codegemma-2b",
        "google/codegemma-2b",
    ),
    "tunelabs/codegemma-7b-bnb-4bit" : (
        "tunelabs/codegemma-7b",
        "google/codegemma-7b",
    ),
    "tunelabs/codegemma-7b-it-bnb-4bit" : (
        "tunelabs/codegemma-7b-it",
        "google/codegemma-7b-it",
    ),
    "tunelabs/llama-3-8b-bnb-4bit" : (
        "tunelabs/llama-3-8b",
        "meta-llama/Meta-Llama-3-8B",
    ),
    "tunelabs/llama-3-8b-Instruct-bnb-4bit" : (
        "tunelabs/llama-3-8b-Instruct",
        "meta-llama/Meta-Llama-3-8B-Instruct",
    ),
    "tunelabs/llama-3-70b-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B",
    ),
    "tunelabs/llama-3-70b-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B-Instruct",
    ),
    "tunelabs/Phi-3-mini-4k-instruct-bnb-4bit" : (
        "tunelabs/Phi-3-mini-4k-instruct",
        "microsoft/Phi-3-mini-4k-instruct",
    ),
    "tunelabs/mistral-7b-v0.3-bnb-4bit" : (
        "tunelabs/mistral-7b-v0.3",
        "mistralai/Mistral-7B-v0.3",
    ),
    "tunelabs/mistral-7b-instruct-v0.3-bnb-4bit" : (
        "tunelabs/mistral-7b-instruct-v0.3",
        "mistralai/Mistral-7B-Instruct-v0.3",
    ),
    "tunelabs/Phi-3-medium-4k-instruct-bnb-4bit" : (
        "tunelabs/Phi-3-medium-4k-instruct",
        "microsoft/Phi-3-medium-4k-instruct",
    ),
    "tunelabs/Qwen2-0.5B-bnb-4bit" : (
        "tunelabs/Qwen2-0.5B",
        "Qwen/Qwen2-0.5B",
    ),
    "tunelabs/Qwen2-0.5B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2-0.5B-Instruct",
        "Qwen/Qwen2-0.5B-Instruct",
    ),
    "tunelabs/Qwen2-1.5B-bnb-4bit" : (
        "tunelabs/Qwen2-1.5B",
        "Qwen/Qwen2-1.5B",
    ),
    "tunelabs/Qwen2-1.5B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2-1.5B-Instruct",
        "Qwen/Qwen2-1.5B-Instruct",
    ),
    "tunelabs/Qwen2-7B-bnb-4bit" : (
        "tunelabs/Qwen2-7B",
        "Qwen/Qwen2-7B",
    ),
    "tunelabs/Qwen2-7B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2-7B-Instruct",
        "Qwen/Qwen2-7B-Instruct",
    ),
    "tunelabs/Qwen2-70B-bnb-4bit" : (
        "Qwen/Qwen2-70B",
    ),
    "tunelabs/Qwen2-70B-Instruct-bnb-4bit" : (
        "Qwen/Qwen2-70B-Instruct",
    ),
    "mistralai/Codestral-22B-v0.1" : (
        "mistral-community/Codestral-22B-v0.1",
    ),
    "tunelabs/gemma-2-9b-bnb-4bit" : (
        "tunelabs/gemma-2-9b",
        "google/gemma-2-9b",
    ),
    "tunelabs/gemma-2-27b-bnb-4bit" : (
        "tunelabs/gemma-2-27b",
        "google/gemma-2-27b",
    ),
    "tunelabs/gemma-2-9b-it-bnb-4bit" : (
        "tunelabs/gemma-2-9b-it",
        "google/gemma-2-9b-it",
    ),
    "tunelabs/gemma-2-27b-it-bnb-4bit" : (
        "tunelabs/gemma-2-27b-it",
        "google/gemma-2-27b-it",
    ),
    "tunelabs/Phi-3-mini-4k-instruct-v0-bnb-4bit" : ( # Old Phi pre July
        "tunelabs/Phi-3-mini-4k-instruct-v0",
    ),
    "tunelabs/Mistral-Nemo-Instruct-2407-bnb-4bit" : ( # New 12b Mistral models
        "tunelabs/Mistral-Nemo-Instruct-2407",
        "mistralai/Mistral-Nemo-Instruct-2407",
    ),
    "tunelabs/Mistral-Nemo-Base-2407-bnb-4bit" : ( # New 12b Mistral models
        "tunelabs/Mistral-Nemo-Base-2407",
        "mistralai/Mistral-Nemo-Base-2407",
    ),
    "tunelabs/Meta-Llama-3.1-8B-tunelabs-bnb-4bit" : (
        "tunelabs/Meta-Llama-3.1-8B",
        "meta-llama/Meta-Llama-3.1-8B",
        "tunelabs/Meta-Llama-3.1-8B-bnb-4bit",
    ),
    "tunelabs/Meta-Llama-3.1-8B-Instruct-tunelabs-bnb-4bit" : {
        "8" : (
            "RedHatAI/Llama-3.1-8B-Instruct-FP8",
            "tunelabs/Llama-3.1-8B-Instruct-FP8-Block",
            "tunelabs/Llama-3.1-8B-Instruct-FP8-Dynamic",
        ),
        "16" : (
            "tunelabs/Meta-Llama-3.1-8B-Instruct",
            "meta-llama/Meta-Llama-3.1-8B-Instruct",
            "tunelabs/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/Llama-3.1-8B-tunelabs-bnb-4bit" : (
        "tunelabs/Llama-3.1-8B",
        "meta-llama/Llama-3.1-8B",
        "tunelabs/Llama-3.1-8B-bnb-4bit",
    ),
    "tunelabs/Llama-3.1-8B-Instruct-tunelabs-bnb-4bit" : {
        "8" : (
            "RedHatAI/Llama-3.1-8B-Instruct-FP8",
            "tunelabs/Llama-3.1-8B-Instruct-FP8-Block",
            "tunelabs/Llama-3.1-8B-Instruct-FP8-Dynamic",
        ),
        "16" : (
            "tunelabs/Llama-3.1-8B-Instruct",
            "meta-llama/Llama-3.1-8B-Instruct",
            "tunelabs/Llama-3.1-8B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/Meta-Llama-3.1-70B-bnb-4bit" : (
        "tunelabs/Meta-Llama-3.1-70B",
        "meta-llama/Meta-Llama-3.1-70B",
    ),
    "tunelabs/Meta-Llama-3.1-405B-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-405B",
    ),
    "tunelabs/Meta-Llama-3.1-405B-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-405B-Instruct",
    ),
    "tunelabs/Meta-Llama-3.1-70B-Instruct-bnb-4bit" : (
        "tunelabs/Meta-Llama-3.1-70B-Instruct",
        "meta-llama/Meta-Llama-3.1-70B-Instruct",
    ),
    "tunelabs/Mistral-Large-Instruct-2407-bnb-4bit" : (
        "mistralai/Mistral-Large-Instruct-2407",
    ),
    "tunelabs/gemma-2-2b-bnb-4bit" : (
        "tunelabs/gemma-2-2b",
        "google/gemma-2-2b",
    ),
    "tunelabs/gemma-2-2b-it-bnb-4bit" : (
        "tunelabs/gemma-2-2b-it",
        "google/gemma-2-2b-it",
    ),
    "tunelabs/Phi-3.5-mini-instruct-bnb-4bit" : (
        "tunelabs/Phi-3.5-mini-instruct",
        "microsoft/Phi-3.5-mini-instruct",
    ),
    "tunelabs/c4ai-command-r-08-2024-bnb-4bit" : (
        "CohereForAI/c4ai-command-r-08-2024",
    ),
    "tunelabs/c4ai-command-r-plus-08-2024-bnb-4bit" : (
        "CohereForAI/c4ai-command-r-plus-08-2024",
    ),
    "tunelabs/Llama-3.1-Storm-8B-bnb-4bit" : (
        "tunelabs/Llama-3.1-Storm-8B",
        "akjindal53244/Llama-3.1-Storm-8B",
    ),
    "tunelabs/Hermes-3-Llama-3.1-8B-bnb-4bit" : (
        "tunelabs/Hermes-3-Llama-3.1-8B",
        "NousResearch/Hermes-3-Llama-3.1-8B",
    ),
    "tunelabs/Hermes-3-Llama-3.1-70B-bnb-4bit" : (
        "tunelabs/Hermes-3-Llama-3.1-70B",
        "NousResearch/Hermes-3-Llama-3.1-70B",
    ),
    "tunelabs/Hermes-3-Llama-3.1-405B-bnb-4bit" : (
        "NousResearch/Hermes-3-Llama-3.1-405B",
    ),
    "tunelabs/SmolLM-135M-bnb-4bit" : (
        "tunelabs/SmolLM-135M",
        "HuggingFaceTB/SmolLM-135M",
    ),
    "tunelabs/SmolLM-360M-bnb-4bit" : (
        "tunelabs/SmolLM-360M",
        "HuggingFaceTB/SmolLM-360M",
    ),
    "tunelabs/SmolLM-1.7B-bnb-4bit" : (
        "tunelabs/SmolLM-1.7B",
        "HuggingFaceTB/SmolLM-1.7B",
    ),
    "tunelabs/SmolLM-135M-Instruct-bnb-4bit" : (
        "tunelabs/SmolLM-135M-Instruct",
        "HuggingFaceTB/SmolLM-135M-Instruct",
    ),
    "tunelabs/SmolLM-360M-Instruct-bnb-4bit" : (
        "tunelabs/SmolLM-360M-Instruct",
        "HuggingFaceTB/SmolLM-360M-Instruct",
    ),
    "tunelabs/SmolLM-1.7B-Instruct-bnb-4bit" : (
        "tunelabs/SmolLM-1.7B-Instruct",
        "HuggingFaceTB/SmolLM-1.7B-Instruct",
    ),
    "tunelabs/Mistral-Small-Instruct-2409-bnb-4bit" : (
        "tunelabs/Mistral-Small-Instruct-2409",
        "mistralai/Mistral-Small-Instruct-2409",
    ),
    "tunelabs/Qwen2.5-0.5B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-0.5B-Instruct",
        "Qwen/Qwen2.5-0.5B-Instruct",
        "tunelabs/Qwen2.5-0.5B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-1.5B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-1.5B-Instruct",
        "Qwen/Qwen2.5-1.5B-Instruct",
        "tunelabs/Qwen2.5-1.5B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-3B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-3B-Instruct",
        "Qwen/Qwen2.5-3B-Instruct",
        "tunelabs/Qwen2.5-3B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-7B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-7B-Instruct",
        "Qwen/Qwen2.5-7B-Instruct",
        "tunelabs/Qwen2.5-7B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-14B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-14B-Instruct",
        "Qwen/Qwen2.5-14B-Instruct",
        "tunelabs/Qwen2.5-14B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-32B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-32B-Instruct",
        "Qwen/Qwen2.5-32B-Instruct",
    ),
    "tunelabs/Qwen2.5-72B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-72B-Instruct",
        "Qwen/Qwen2.5-72B-Instruct",
    ),
    "tunelabs/Qwen2.5-0.5B-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-0.5B",
        "Qwen/Qwen2.5-0.5B",
        "tunelabs/Qwen2.5-0.5B-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-1.5B-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-1.5B",
        "Qwen/Qwen2.5-1.5B",
        "tunelabs/Qwen2.5-1.5B-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-3B-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-3B",
        "Qwen/Qwen2.5-3B",
        "tunelabs/Qwen2.5-3B-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-7B-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-7B",
        "Qwen/Qwen2.5-7B",
        "tunelabs/Qwen2.5-7B-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-14B-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-14B",
        "Qwen/Qwen2.5-14B",
        "tunelabs/Qwen2.5-14B-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-32B-bnb-4bit" : (
        "tunelabs/Qwen2.5-32B",
        "Qwen/Qwen2.5-32B",
    ),
    "tunelabs/Qwen2.5-72B-bnb-4bit" : (
        "tunelabs/Qwen2.5-72B",
        "Qwen/Qwen2.5-72B",
    ),
    "tunelabs/Qwen2.5-Math-1.5B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Math-1.5B",
        "Qwen/Qwen2.5-Math-1.5B",
    ),
    "tunelabs/Qwen2.5-Math-7B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Math-7B",
        "Qwen/Qwen2.5-Math-7B",
    ),
    "tunelabs/Qwen2.5-Math-72B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Math-72B",
        "Qwen/Qwen2.5-Math-72B",
    ),
    "tunelabs/Qwen2.5-Math-1.5B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Math-1.5B-Instruct",
        "Qwen/Qwen2.5-Math-1.5B-Instruct",
    ),
    "tunelabs/Qwen2.5-Math-7B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Math-7B-Instruct",
        "Qwen/Qwen2.5-Math-7B-Instruct",
    ),
    "tunelabs/Qwen2.5-Math-72B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Math-72B-Instruct",
        "Qwen/Qwen2.5-Math-72B-Instruct",
    ),
    "tunelabs/Qwen2.5-Coder-0.5B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-0.5B",
        "Qwen/Qwen2.5-Coder-0.5B",
    ),
    "tunelabs/Qwen2.5-Coder-1.5B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-1.5B",
        "Qwen/Qwen2.5-Coder-1.5B",
    ),
    "tunelabs/Qwen2.5-Coder-3B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-3B",
        "Qwen/Qwen2.5-Coder-3B",
    ),
    "tunelabs/Qwen2.5-Coder-7B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-7B",
        "Qwen/Qwen2.5-Coder-7B",
    ),
    "tunelabs/Qwen2.5-Coder-14B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-14B",
        "Qwen/Qwen2.5-Coder-14B",
    ),
    "tunelabs/Qwen2.5-Coder-32B-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-32B",
        "Qwen/Qwen2.5-Coder-32B",
    ),
    "tunelabs/Qwen2.5-Coder-0.5B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-0.5B-Instruct",
        "Qwen/Qwen2.5-Coder-0.5B-Instruct",
    ),
    "tunelabs/Qwen2.5-Coder-1.5B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-1.5B-Instruct",
        "Qwen/Qwen2.5-Coder-1.5B-Instruct",
    ),
    "tunelabs/Qwen2.5-Coder-3B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-3B-Instruct",
        "Qwen/Qwen2.5-Coder-3B-Instruct",
    ),
    "tunelabs/Qwen2.5-Coder-7B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-7B-Instruct",
        "Qwen/Qwen2.5-Coder-7B-Instruct",
    ),
    "tunelabs/Qwen2.5-Coder-14B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-14B-Instruct",
        "Qwen/Qwen2.5-Coder-14B-Instruct",
    ),
    "tunelabs/Qwen2.5-Coder-32B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2.5-Coder-32B-Instruct",
        "Qwen/Qwen2.5-Coder-32B-Instruct",
    ),
    "tunelabs/Llama-3.2-1B-tunelabs-bnb-4bit" : (
        "tunelabs/Llama-3.2-1B",
        "meta-llama/Llama-3.2-1B",
        "tunelabs/Llama-3.2-1B-bnb-4bit",
    ),
    "tunelabs/Llama-3.2-3B-tunelabs-bnb-4bit" : (
        "tunelabs/Llama-3.2-3B",
        "meta-llama/Llama-3.2-3B",
        "tunelabs/Llama-3.2-3B-bnb-4bit",
    ),
    "tunelabs/Llama-3.2-1B-Instruct-tunelabs-bnb-4bit" : {
        "8": (
            "RedHatAI/Llama-3.2-1B-Instruct-FP8",
            "tunelabs/Llama-3.2-1B-Instruct-FP8-Block",
            "tunelabs/Llama-3.2-1B-Instruct-FP8-Dynamic",
        ),
        "16" : (
            "tunelabs/Llama-3.2-1B-Instruct",
            "meta-llama/Llama-3.2-1B-Instruct",
            "tunelabs/Llama-3.2-1B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/Llama-3.2-3B-Instruct-tunelabs-bnb-4bit" : {
        "8": (
            "RedHatAI/Llama-3.2-3B-Instruct-FP8",
            "tunelabs/Llama-3.2-3B-Instruct-FP8-Block",
            "tunelabs/Llama-3.2-3B-Instruct-FP8-Dynamic",
        ),
        "16" : (
            "tunelabs/Llama-3.2-3B-Instruct",
            "meta-llama/Llama-3.2-3B-Instruct",
            "tunelabs/Llama-3.2-3B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/Llama-3.1-Nemotron-70B-Instruct-bnb-4bit" : (
        "tunelabs/Llama-3.1-Nemotron-70B-Instruct",
        "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
    ),
    "tunelabs/Qwen2-VL-2B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2-VL-2B-Instruct",
        "Qwen/Qwen2-VL-2B-Instruct",
        "tunelabs/Qwen2-VL-2B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2-VL-7B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2-VL-7B-Instruct",
        "Qwen/Qwen2-VL-7B-Instruct",
        "tunelabs/Qwen2-VL-7B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2-VL-72B-Instruct-bnb-4bit" : (
        "tunelabs/Qwen2-VL-72B-Instruct",
        "Qwen/Qwen2-VL-72B-Instruct",
    ),
    "tunelabs/Qwen2-VL-2B-bnb-4bit" : (
        "tunelabs/Qwen2-VL-2B",
        "Qwen/Qwen2-VL-2B",
    ),
    "tunelabs/Qwen2-VL-7B-bnb-4bit" : (
        "tunelabs/Qwen2-VL-7B",
        "Qwen/Qwen2-VL-7B",
    ),
    "tunelabs/Qwen2-VL-72B-bnb-4bit" : (
        "tunelabs/Qwen2-VL-72B",
        "Qwen/Qwen2-VL-72B",
    ),
    "tunelabs/Llama-3.2-11B-Vision-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Llama-3.2-11B-Vision-Instruct",
        "meta-llama/Llama-3.2-11B-Vision-Instruct",
        "tunelabs/Llama-3.2-11B-Vision-Instruct-bnb-4bit",
    ),
    "tunelabs/Llama-3.2-90B-Vision-Instruct-bnb-4bit" : (
        "tunelabs/Llama-3.2-90B-Vision-Instruct",
        "meta-llama/Llama-3.2-90B-Vision-Instruct",
    ),
    "tunelabs/Llama-3.2-11B-Vision-tunelabs-bnb-4bit" : (
        "tunelabs/Llama-3.2-11B-Vision",
        "meta-llama/Llama-3.2-11B-Vision",
        "tunelabs/Llama-3.2-11B-Vision-bnb-4bit",
    ),
    "tunelabs/Llama-3.2-90B-Vision-bnb-4bit" : (
        "tunelabs/Llama-3.2-90B-Vision",
        "meta-llama/Llama-3.2-90B-Vision",
    ),
    "tunelabs/Pixtral-12B-2409-tunelabs-bnb-4bit" : (
        "tunelabs/Pixtral-12B-2409",
        "mistralai/Pixtral-12B-2409",
        "tunelabs/Pixtral-12B-2409-bnb-4bit",
    ),
    "tunelabs/Pixtral-12B-2409-Base-bnb-4bit" : (
        "tunelabs/Pixtral-12B-Base-2409",
        "mistralai/Pixtral-12B-Base-2409",
    ),
    "tunelabs/llava-1.5-7b-hf-bnb-4bit" : (
        "tunelabs/llava-1.5-7b-hf",
        "llava-hf/llava-1.5-7b-hf",
    ),
    "tunelabs/llava-v1.6-mistral-7b-hf-bnb-4bit" : (
        "tunelabs/llava-v1.6-mistral-7b-hf",
        "llava-hf/llava-v1.6-mistral-7b-hf",
    ),
    "tunelabs/Llama-3.1-Tulu-3-8B-bnb-4bit" : (
        "tunelabs/Llama-3.1-Tulu-3-8B",
        "allenai/Llama-3.1-Tulu-3-8B",
    ),
    "tunelabs/Llama-3.1-Tulu-3-70B-bnb-4bit" : (
        "tunelabs/Llama-3.1-Tulu-3-70B",
        "allenai/Llama-3.1-Tulu-3-70B",
    ),
    "tunelabs/QwQ-32B-Preview-bnb-4bit" : (
        "tunelabs/QwQ-32B-Preview",
        "Qwen/QwQ-32B-Preview",
    ),
    "tunelabs/Llama-3.3-70B-Instruct-tunelabs-bnb-4bit" : {
        "8" : (
            "RedHatAI/Llama-3.3-70B-Instruct-FP8",
            "tunelabs/Llama-3.3-70B-Instruct-FP8-Block",
            "tunelabs/Llama-3.3-70B-Instruct-FP8-Dynamic",
        ),
        "16" : (
            "tunelabs/Llama-3.3-70B-Instruct",
            "meta-llama/Llama-3.3-70B-Instruct",
            "tunelabs/Llama-3.3-70B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/phi-4-tunelabs-bnb-4bit" : (
        "tunelabs/phi-4",
        "microsoft/phi-4",
        "tunelabs/phi-4-bnb-4bit",
    ),
    "tunelabs/DeepSeek-R1-Distill-Qwen-32B-bnb-4bit" : (
        "tunelabs/DeepSeek-R1-Distill-Qwen-32B",
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    ),
    "tunelabs/DeepSeek-R1-Distill-Qwen-14B-tunelabs-bnb-4bit" : (
        "tunelabs/DeepSeek-R1-Distill-Qwen-14B",
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
        "tunelabs/DeepSeek-R1-Distill-Qwen-14B-bnb-4bit",
    ),
    "tunelabs/DeepSeek-R1-Distill-Qwen-7B-tunelabs-bnb-4bit" : (
        "tunelabs/DeepSeek-R1-Distill-Qwen-7B",
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
        "tunelabs/DeepSeek-R1-Distill-Qwen-7B-bnb-4bit",
    ),
    "tunelabs/DeepSeek-R1-Distill-Qwen-1.5B-tunelabs-bnb-4bit" : (
        "tunelabs/DeepSeek-R1-Distill-Qwen-1.5B",
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        "tunelabs/DeepSeek-R1-Distill-Qwen-1.5B-bnb-4bit",
    ),
    "tunelabs/DeepSeek-R1-Distill-Llama-8B-tunelabs-bnb-4bit" : (
        "tunelabs/DeepSeek-R1-Distill-Llama-8B",
        "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
        "tunelabs/DeepSeek-R1-Distill-Llama-8B-bnb-4bit",
    ),
    "tunelabs/DeepSeek-R1-Distill-Llama-70B-bnb-4bit" : (
        "tunelabs/DeepSeek-R1-Distill-Llama-70B",
        "deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
    ),
    "tunelabs/Mistral-Small-24B-Base-2501-tunelabs-bnb-4bit" : (
        "tunelabs/Mistral-Small-24B-Base-2501",
        "mistralai/Mistral-Small-24B-Base-2501",
        "tunelabs/Mistral-Small-24B-Base-2501-bnb-4bit",
    ),
    "tunelabs/Mistral-Small-24B-Instruct-2501-tunelabs-bnb-4bit" : (
        "tunelabs/Mistral-Small-24B-Instruct-2501",
        "mistralai/Mistral-Small-24B-Instruct-2501",
        "tunelabs/Mistral-Small-24B-Instruct-2501-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-VL-3B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-VL-3B-Instruct",
        "Qwen/Qwen2.5-VL-3B-Instruct",
        "tunelabs/Qwen2.5-VL-3B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-VL-7B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-VL-7B-Instruct",
        "Qwen/Qwen2.5-VL-7B-Instruct",
        "tunelabs/Qwen2.5-VL-7B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-VL-32B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-VL-32B-Instruct",
        "Qwen/Qwen2.5-VL-32B-Instruct",
        "tunelabs/Qwen2.5-VL-32B-Instruct-bnb-4bit",
    ),
    "tunelabs/Qwen2.5-VL-72B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen2.5-VL-72B-Instruct",
        "Qwen/Qwen2.5-VL-72B-Instruct",
        "tunelabs/Qwen2.5-VL-72B-Instruct-bnb-4bit",
    ),
    "tunelabs/DeepScaleR-1.5B-Preview-tunelabs-bnb-4bit" : (
        "tunelabs/DeepHermes-3-Llama-3-8B-Preview",
        "agentica-org/DeepScaleR-1.5B-Preview",
        "tunelabs/DeepScaleR-1.5B-Preview-bnb-4bit",
    ),
    "tunelabs/OpenThinker-7B-tunelabs-bnb-4bit" : (
        "tunelabs/OpenThinker-7B",
        "open-thoughts/OpenThinker-7B",
        "tunelabs/OpenThinker-7B-bnb-4bit",
    ),
    "tunelabs/granite-3.2-2b-instruct-tunelabs-bnb-4bit" : (
        "tunelabs/granite-3.2-2b-instruct",
        "ibm-granite/granite-3.2-2b-instruct",
        "tunelabs/granite-3.2-2b-instruct-bnb-4bit",
    ),
    "tunelabs/granite-3.2-8b-instruct-tunelabs-bnb-4bit" : (
        "tunelabs/granite-3.2-8b-instruct",
        "ibm-granite/granite-3.2-8b-instruct",
        "tunelabs/granite-3.2-8b-instruct-bnb-4bit",
    ),
    "tunelabs/QwQ-32B-tunelabs-bnb-4bit" : (
        "tunelabs/QwQ-32B",
        "Qwen/QwQ-32B",
        "tunelabs/QwQ-32B-bnb-4bit",
    ),
    "tunelabs/gemma-3-1b-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-1b-it",
        "google/gemma-3-1b-it",
        "tunelabs/gemma-3-1b-it-bnb-4bit",
    ),
    "tunelabs/gemma-3-4b-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-4b-it",
        "google/gemma-3-4b-it",
        "tunelabs/gemma-3-4b-it-bnb-4bit",
    ),
    "tunelabs/gemma-3-12b-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-12b-it",
        "google/gemma-3-12b-it",
        "tunelabs/gemma-3-12b-it-bnb-4bit",
    ),
    "tunelabs/gemma-3-27b-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-27b-it",
        "google/gemma-3-27b-it",
        "tunelabs/gemma-3-27b-it-bnb-4bit",
    ),
    "tunelabs/gemma-3-1b-pt-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-1b-pt",
        "google/gemma-3-1b-pt",
        "tunelabs/gemma-3-1b-pt-bnb-4bit",
    ),
    "tunelabs/gemma-3-4b-pt-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-4b-pt",
        "google/gemma-3-4b-pt",
        "tunelabs/gemma-3-4b-pt-bnb-4bit",
    ),
    "tunelabs/gemma-3-12b-pt-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-12b-pt",
        "google/gemma-3-12b-pt",
        "tunelabs/gemma-3-12b-pt-bnb-4bit",
    ),
    "tunelabs/gemma-3-27b-pt-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-27b-pt",
        "google/gemma-3-27b-pt",
        "tunelabs/gemma-3-27b-pt-bnb-4bit",
    ),
    "tunelabs/reka-flash-3-tunelabs-bnb-4bit" : (
        "tunelabs/reka-flash-3",
        "RekaAI/reka-flash-3",
        "tunelabs/reka-flash-3-bnb-4bit",
    ),
    "tunelabs/c4ai-command-a-03-2025-tunelabs-bnb-4bit" : (
        "tunelabs/c4ai-command-a-03-2025",
        "CohereForAI/c4ai-command-a-03-2025",
        "tunelabs/c4ai-command-a-03-2025-bnb-4bit",
    ),
    "tunelabs/aya-vision-32b-tunelabs-bnb-4bit" : (
        "tunelabs/aya-vision-32b",
        "CohereForAI/aya-vision-32b",
        "tunelabs/aya-vision-32b-bnb-4bit",
    ),
    "tunelabs/aya-vision-8b-tunelabs-bnb-4bit" : (
        "tunelabs/aya-vision-8b",
        "CohereForAI/aya-vision-8b",
        "tunelabs/aya-vision-8b-bnb-4bit",
    ),
    "tunelabs/granite-vision-3.2-2b-tunelabs-bnb-4bit" : (
        "tunelabs/granite-vision-3.2-2b",
        "ibm-granite/granite-vision-3.2-2b",
        "tunelabs/granite-vision-3.2-2b-bnb-4bit",
    ),
    "tunelabs/OLMo-2-0325-32B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/OLMo-2-0325-32B-Instruct",
        "allenai/OLMo-2-0325-32B-Instruct",
        "tunelabs/OLMo-2-0325-32B-Instruct-bnb-4bit",
    ),
    "tunelabs/Olmo-3-7B-Instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Olmo-3-7B-Instruct",
        "allenai/Olmo-3-7B-Instruct",
    ),
    "tunelabs/Olmo-3-7B-Think-tunelabs-bnb-4bit" : (
        "tunelabs/Olmo-3-7B-Think",
        "allenai/Olmo-3-7B-Think",
    ),
    "tunelabs/Olmo-3-32B-Think-tunelabs-bnb-4bit" : (
        "tunelabs/Olmo-3-32B-Think",
        "allenai/Olmo-3-32B-Think",
    ),
    "tunelabs/Mistral-Small-3.1-24B-Instruct-2503-tunelabs-bnb-4bit" : (
        "tunelabs/Mistral-Small-3.1-24B-Instruct-2503",
        "mistralai/Mistral-Small-3.1-24B-Instruct-2503",
        "tunelabs/Mistral-Small-3.1-24B-Instruct-2503-bnb-4bit",
    ),
    "tunelabs/Mistral-Small-3.1-24B-Base-2503-tunelabs-bnb-4bit" : (
        "tunelabs/Mistral-Small-3.1-24B-Base-2503",
        "mistralai/Mistral-Small-3.1-24B-Base-2503",
        "tunelabs/Mistral-Small-3.1-24B-Base-2503-bnb-4bit",
    ),
    "tunelabs/Qwen3-0.6B-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-0.6B-FP8",
            "tunelabs/Qwen3-0.6B-FP8",
            "tunelabs/Qwen3-0.6B-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-0.6B",
            "Qwen/Qwen3-0.6B",
            "tunelabs/Qwen3-0.6B-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-1.7B-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-1.7B-FP8",
            "tunelabs/Qwen3-1.7B-FP8",
            "tunelabs/Qwen3-1.7B-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-1.7B",
            "Qwen/Qwen3-1.7B",
            "tunelabs/Qwen3-1.7B-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-4B-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-4B-FP8",
            "tunelabs/Qwen3-4B-FP8",
            "tunelabs/Qwen3-4B-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-4B",
            "Qwen/Qwen3-4B",
            "tunelabs/Qwen3-4B-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-8B-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-8B-FP8",
            "tunelabs/Qwen3-8B-FP8",
            "tunelabs/Qwen3-8B-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-8B",
            "Qwen/Qwen3-8B",
            "tunelabs/Qwen3-8B-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-14B-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-14B-FP8",
            "tunelabs/Qwen3-14B-FP8",
            "tunelabs/Qwen3-14B-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-14B",
            "Qwen/Qwen3-14B",
            "tunelabs/Qwen3-14B-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-32B-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-32B-FP8",
            "tunelabs/Qwen3-32B-FP8",
            "tunelabs/Qwen3-32B-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-32B",
            "Qwen/Qwen3-32B",
            "tunelabs/Qwen3-32B-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-30B-A3B-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen3-30B-A3B",
        "Qwen/Qwen3-30B-A3B",
        "tunelabs/Qwen3-30B-A3B-bnb-4bit",
    ),
    "tunelabs/Qwen3-0.6B-Base-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen3-0.6B-Base",
        "Qwen/Qwen3-0.6B-Base",
        "tunelabs/Qwen3-0.6B-Base-bnb-4bit",
    ),
    "tunelabs/Qwen3-1.7B-Base-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen3-1.7B-Base",
        "Qwen/Qwen3-1.7B-Base",
        "tunelabs/Qwen3-1.7B-Base-bnb-4bit",
    ),
    "tunelabs/Qwen3-4B-Base-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen3-4B-Base",
        "Qwen/Qwen3-4B-Base",
        "tunelabs/Qwen3-4B-Base-bnb-4bit",
    ),
    "tunelabs/Qwen3-8B-Base-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen3-8B-Base",
        "Qwen/Qwen3-8B-Base",
        "tunelabs/Qwen3-8B-Base-bnb-4bit",
    ),
    "tunelabs/Qwen3-14B-Base-tunelabs-bnb-4bit" : (
        "tunelabs/Qwen3-14B-Base",
        "Qwen/Qwen3-14B-Base",
        "tunelabs/Qwen3-14B-Base-bnb-4bit",
    ),
    "tunelabs/Qwen3-30B-A3B-Base-bnb-4bit" : (
        "tunelabs/Qwen3-30B-A3B-Base",
        "Qwen/Qwen3-30B-A3B-Base",
    ),
    "tunelabs/phi-4-reasoning-tunelabs-bnb-4bit" : (
        "tunelabs/phi-4-reasoning",
        "microsoft/Phi-4-reasoning",
        "tunelabs/phi-4-reasoning-bnb-4bit",
    ),
    "tunelabs/phi-4-reasoning-plus-tunelabs-bnb-4bit" : (
        "tunelabs/phi-4-reasoning-plus",
        "microsoft/Phi-4-reasoning-plus",
        "tunelabs/phi-4-reasoning-plus-bnb-4bit",
    ),
    "tunelabs/phi-4-mini-reasoning-tunelabs-bnb-4bit" : (
        "tunelabs/phi-4-mini-reasoning",
        "microsoft/Phi-4-mini-reasoning",
        "tunelabs/phi-4-mini-reasoning-bnb-4bit",
    ),
    "tunelabs/Phi-4-mini-instruct-tunelabs-bnb-4bit" : (
        "tunelabs/Phi-4-mini-instruct",
        "microsoft/Phi-4-mini-instruct",
        "tunelabs/Phi-4-mini-instruct-bnb-4bit",
    ),
    "tunelabs/orpheus-3b-0.1-pretrained-tunelabs-bnb-4bit" : (
        "tunelabs/orpheus-3b-0.1-pretrained",
        "canopylabs/orpheus-3b-0.1-pretrained",
        "tunelabs/orpheus-3b-0.1-pretrained-bnb-4bit",
    ),
    "tunelabs/orpheus-3b-0.1-ft-tunelabs-bnb-4bit" : (
        "tunelabs/orpheus-3b-0.1-ft",
        "canopylabs/orpheus-3b-0.1-ft",
        "tunelabs/orpheus-3b-0.1-ft-bnb-4bit",
    ),
    "tunelabs/csm-1b" : (
        "tunelabs/csm-1b",
        "sesame/csm-1b",
    ),
    "tunelabs/whisper-large-v3" : (
        "tunelabs/whisper-large-v3",
        "openai/whisper-large-v3",
    ),
    "tunelabs/whisper-large-v3-turbo" : (
        "tunelabs/whisper-large-v3-turbo",
        "openai/whisper-large-v3-turbo",
    ),
    "tunelabs/whisper-small" : (
        "tunelabs/whisper-small",
        "openai/whisper-small",
    ),
    "tunelabs/CrisperWhisper" : (
        "tunelabs/CrisperWhisper",
        "nyrahealth/CrisperWhisper",
    ),
    "tunelabs/Llasa-1B" : (
        "tunelabs/Llasa-1B",
        "HKUSTAudio/Llasa-1B",
    ),
    "tunelabs/Spark-TTS-0.5B" : (
        "tunelabs/Spark-TTS-0.5B",
        "SparkAudio/Spark-TTS-0.5B",
    ),
    "tunelabs/Llama-OuteTTS-1.0-1B" : (
        "tunelabs/Llama-OuteTTS-1.0-1B",
        "OuteAI/Llama-OuteTTS-1.0-1B",
    ),
    "tunelabs/medgemma-4b-it-tunelabs-bnb-4bit" : (
        "tunelabs/medgemma-4b-it",
        "google/medgemma-4b-it",
        "tunelabs/medgemma-4b-it-bnb-4bit",
    ),
    "tunelabs/medgemma-27b-text-it-tunelabs-bnb-4bit" : (
        "tunelabs/medgemma-27b-text-it",
        "google/medgemma-27b-text-it",
        "tunelabs/medgemma-27b-text-it-bnb-4bit",
    ),
    "tunelabs/Devstral-Small-2505-tunelabs-bnb-4bit" : (
        "tunelabs/Devstral-Small-2505",
        "mistralai/Devstral-Small-2505",
        "tunelabs/Devstral-Small-2505-bnb-4bit",
    ),
    "tunelabs/DeepSeek-R1-0528-Qwen3-8B-tunelabs-bnb-4bit" : (
        "tunelabs/DeepSeek-R1-0528-Qwen3-8B",
        "deepseek-ai/DeepSeek-R1-0528-Qwen3-8B",
        "tunelabs/DeepSeek-R1-0528-Qwen3-8B-bnb-4bit",
    ),
    "tunelabs/Magistral-Small-2506-tunelabs-bnb-4bit" : (
        "tunelabs/Magistral-Small-2506",
        "mistralai/Magistral-Small-2506",
        "tunelabs/Magistral-Small-2506-bnb-4bit",
    ),
    "tunelabs/Mistral-Small-3.2-24B-Instruct-2506-tunelabs-bnb-4bit" : {
        "8" : (
            "mistralai/Mistral-Small-3.2-24B-Instruct-2506",
            "tunelabs/Mistral-Small-3.2-24B-Instruct-2506-FP8",
            "tunelabs/Mistral-Small-3.2-24B-Instruct-2506-FP8",
        ),
        "16" : (
            "tunelabs/Mistral-Small-3.2-24B-Instruct-2506",
            "mistralai/Mistral-Small-3.2-24B-Instruct-2506",
            "tunelabs/Mistral-Small-3.2-24B-Instruct-2506-bnb-4bit",
        ),
    },
    "tunelabs/gemma-3n-E4B-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3n-E4B-it",
        "google/gemma-3n-E4B-it",
        "tunelabs/gemma-3n-E4B-it-tunelabs-bnb-4bit",
    ),
    "tunelabs/gemma-3n-E2B-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3n-E2B-it",
        "google/gemma-3n-E2B-it",
        "tunelabs/gemma-3n-E2B-it-tunelabs-bnb-4bit",
    ),
    "tunelabs/gemma-3n-E4B-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3n-E4B",
        "google/gemma-3n-E4B",
        "tunelabs/gemma-3n-E4B-tunelabs-bnb-4bit",
    ),
    "tunelabs/gemma-3n-E2B-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3n-E2B",
        "google/gemma-3n-E2B",
        "tunelabs/gemma-3n-E2B-tunelabs-bnb-4bit",
    ),
    "tunelabs/Devstral-Small-2507-tunelabs-bnb-4bit" : (
        "tunelabs/Devstral-Small-2507",
        "mistralai/Devstral-Small-2507",
        "tunelabs/Devstral-Small-2507-bnb-4bit",
    ),
    "tunelabs/Qwen3-30B-A3B-Thinking-2507" : (
        "tunelabs/Qwen3-30B-A3B-Thinking-2507",
        "Qwen/Qwen3-30B-A3B-Thinking-2507",
    ),
    "tunelabs/Qwen3-30B-A3B-Instruct-2507" : (
        "tunelabs/Qwen3-30B-A3B-Instruct-2507",
        "Qwen/Qwen3-30B-A3B-Instruct-2507",
    ),
    "tunelabs/Qwen3-Coder-30B-A3B-Instruct" : (
        "tunelabs/Qwen3-Coder-30B-A3B-Instruct",
        "Qwen/Qwen3-Coder-30B-A3B-Instruct",
    ),
    "tunelabs/gpt-oss-20b-tunelabs-bnb-4bit" : (
        "tunelabs/gpt-oss-20b",
        "openai/gpt-oss-20b",
        "tunelabs/gpt-oss-20b-tunelabs-bnb-4bit",
    ),
    "tunelabs/gpt-oss-120b-tunelabs-bnb-4bit" : (
        "tunelabs/gpt-oss-120b",
        "openai/gpt-oss-120b",
        "tunelabs/gpt-oss-120b-tunelabs-bnb-4bit",
    ),
    "tunelabs/Qwen3-4B-Instruct-2507-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-4B-Instruct-2507-FP8",
            "tunelabs/Qwen3-4B-Instruct-2507-FP8",
            "tunelabs/Qwen3-4B-Instruct-2507-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-4B-Instruct-2507",
            "Qwen/Qwen3-4B-Instruct-2507",
            "tunelabs/Qwen3-4B-Instruct-2507-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-4B-Thinking-2507-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-4B-Thinking-2507-FP8",
            "tunelabs/Qwen3-4B-Thinking-2507-FP8",
            "tunelabs/Qwen3-4B-Thinking-2507-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-4B-Thinking-2507",
            "Qwen/Qwen3-4B-Thinking-2507",
            "tunelabs/Qwen3-4B-Thinking-2507-bnb-4bit",
        ),
    },
    "tunelabs/gemma-3-270m-it-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-270m-it",
        "google/gemma-3-270m-it",
        "tunelabs/gemma-3-270m-it-bnb-4bit",
    ),
    "tunelabs/gemma-3-270m-tunelabs-bnb-4bit" : (
        "tunelabs/gemma-3-270m",
        "google/gemma-3-270m",
        "tunelabs/gemma-3-270m-bnb-4bit",
    ),
    "tunelabs/Magistral-Small-2507-tunelabs-bnb-4bit" : (
        "tunelabs/Magistral-Small-2507",
        "mistralai/Magistral-Small-2507",
        "tunelabs/Magistral-Small-2507-bnb-4bit",
    ),
    "tunelabs/Magistral-Small-2509-tunelabs-bnb-4bit" : {
        "8" : (
            "mistralai/Magistral-Small-2509",
            "tunelabs/Magistral-Small-2509-FP8-Dynamic",
            "tunelabs/Magistral-Small-2509-FP8-Dynamic",
        ),
        "16" : (
            "tunelabs/Magistral-Small-2509",
            "mistralai/Magistral-Small-2509",
            "tunelabs/Magistral-Small-2509-bnb-4bit",
        ),
    },
    "tunelabs/Apertus-70B-Instruct-2509-tunelabs-bnb-4bit" : (
        "tunelabs/Apertus-70B-Instruct-2509",
        "swiss-ai/Apertus-70B-2509",
        "tunelabs/Apertus-70B-Instruct-2509-tunelabs-bnb-4bit",
    ),
    "tunelabs/Apertus-8B-Instruct-2509-tunelabs-bnb-4bit" : (
        "tunelabs/Apertus-8B-Instruct-2509",
        "swiss-ai/Apertus-8B-2509",
        "tunelabs/Apertus-8B-Instruct-2509-tunelabs-bnb-4bit",
    ),
    "tunelabs/granite-4.0-micro-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-micro",
        "ibm-granite/granite-4.0-micro",
        "tunelabs/granite-4.0-micro-bnb-4bit",
    ),
    "tunelabs/granite-4.0-h-micro-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-h-micro",
        "ibm-granite/granite-4.0-h-micro",
        "tunelabs/granite-4.0-h-micro-bnb-4bit",
    ),
    "tunelabs/granite-4.0-micro-base-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-micro-base",
        "ibm-granite/granite-4.0-micro-base",
        "tunelabs/granite-4.0-micro-base-bnb-4bit",
    ),
    "tunelabs/granite-4.0-h-micro-base-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-h-micro-base",
        "ibm-granite/granite-4.0-h-micro-base",
        "tunelabs/granite-4.0-h-micro-base-bnb-4bit",
    ),
    "tunelabs/granite-4.0-h-tiny" : (
        "tunelabs/granite-4.0-h-tiny",
        "ibm-granite/granite-4.0-h-tiny",
    ),
    "tunelabs/granite-4.0-h-small" : (
        "tunelabs/granite-4.0-h-small",
        "ibm-granite/granite-4.0-h-small",
    ),
    "tunelabs/granite-4.0-h-tiny-base" : (
        "tunelabs/granite-4.0-h-tiny-base",
        "ibm-granite/granite-4.0-h-tiny-base",
    ),
    "tunelabs/granite-4.0-h-small-base" : (
        "tunelabs/granite-4.0-h-small-base",
        "ibm-granite/granite-4.0-h-small-base",
    ),
    "tunelabs/Qwen3-VL-4B-Thinking-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-4B-Thinking-FP8",
            "tunelabs/Qwen3-VL-4B-Thinking-FP8",
            "tunelabs/Qwen3-VL-4B-Thinking-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-4B-Thinking",
            "Qwen/Qwen3-VL-4B-Thinking",
            "tunelabs/Qwen3-VL-4B-Thinking-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-VL-8B-Thinking-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-8B-Thinking-FP8",
            "tunelabs/Qwen3-VL-8B-Thinking-FP8",
            "tunelabs/Qwen3-VL-8B-Thinking-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-8B-Thinking",
            "Qwen/Qwen3-VL-8B-Thinking",
            "tunelabs/Qwen3-VL-8B-Thinking-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-VL-4B-Instruct-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-4B-Instruct-FP8",
            "tunelabs/Qwen3-VL-4B-Instruct-FP8",
            "tunelabs/Qwen3-VL-4B-Instruct-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-4B-Instruct",
            "Qwen/Qwen3-VL-4B-Instruct",
            "tunelabs/Qwen3-VL-4B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-VL-8B-Instruct-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-8B-Instruct-FP8",
            "tunelabs/Qwen3-VL-8B-Instruct-FP8",
            "tunelabs/Qwen3-VL-8B-Instruct-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-8B-Instruct",
            "Qwen/Qwen3-VL-8B-Instruct",
            "tunelabs/Qwen3-VL-8B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-VL-2B-Thinking-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-2B-Thinking-FP8",
            "tunelabs/Qwen3-VL-2B-Thinking-FP8",
            "tunelabs/Qwen3-VL-2B-Thinking-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-2B-Thinking",
            "Qwen/Qwen3-VL-2B-Thinking",
            "tunelabs/Qwen3-VL-2B-Thinking-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-VL-32B-Thinking-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-32B-Thinking-FP8",
            "tunelabs/Qwen3-VL-32B-Thinking-FP8",
            "tunelabs/Qwen3-VL-32B-Thinking-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-32B-Thinking",
            "Qwen/Qwen3-VL-32B-Thinking",
            "tunelabs/Qwen3-VL-32B-Thinking-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-VL-2B-Instruct-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-2B-Instruct-FP8",
            "tunelabs/Qwen3-VL-2B-Instruct-FP8",
            "tunelabs/Qwen3-VL-2B-Instruct-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-2B-Instruct",
            "Qwen/Qwen3-VL-2B-Instruct",
            "tunelabs/Qwen3-VL-2B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/Qwen3-VL-32B-Instruct-tunelabs-bnb-4bit" : {
        "8" : (
            "Qwen/Qwen3-VL-32B-Instruct-FP8",
            "tunelabs/Qwen3-VL-32B-Instruct-FP8",
            "tunelabs/Qwen3-VL-32B-Instruct-FP8",
        ),
        "16" : (
            "tunelabs/Qwen3-VL-32B-Instruct",
            "Qwen/Qwen3-VL-32B-Instruct",
            "tunelabs/Qwen3-VL-32B-Instruct-bnb-4bit",
        ),
    },
    "tunelabs/granite-4.0-350m-base-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-350m-base",
        "ibm-granite/granite-4.0-350m-base",
        "tunelabs/granite-4.0-350m-base-bnb-4bit",
    ),
    "tunelabs/granite-4.0-350m-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-350m",
        "ibm-granite/granite-4.0-350m",
        "tunelabs/granite-4.0-350m-bnb-4bit",
    ),
    "tunelabs/granite-4.0-h-350m-base-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-h-350m-base",
        "ibm-granite/granite-4.0-h-350m-base",
        "tunelabs/granite-4.0-h-350m-base-bnb-4bit",
    ),
    "tunelabs/granite-4.0-h-350m-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-h-350m",
        "ibm-granite/granite-4.0-h-350m",
        "tunelabs/granite-4.0-h-350m-bnb-4bit",
    ),
    "tunelabs/granite-4.0-1b-base-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-1b-base",
        "ibm-granite/granite-4.0-1b-base",
        "tunelabs/granite-4.0-1b-base-bnb-4bit",
    ),
    "tunelabs/granite-4.0-1b-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-1b",
        "ibm-granite/granite-4.0-1b",
        "tunelabs/granite-4.0-1b-bnb-4bit",
    ),
    "tunelabs/granite-4.0-h-1b-base-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-h-1b-base",
        "ibm-granite/granite-4.0-h-1b-base",
        "tunelabs/granite-4.0-h-1b-base-bnb-4bit",
    ),
    "tunelabs/granite-4.0-h-1b-tunelabs-bnb-4bit" : (
        "tunelabs/granite-4.0-h-1b",
        "ibm-granite/granite-4.0-h-1b",
        "tunelabs/granite-4.0-h-1b-bnb-4bit",
    ),
    "tunelabs/gpt-oss-safeguard-20b" : (
        "tunelabs/gpt-oss-safeguard-20b",
        "openai/gpt-oss-safeguard-20b",
    ),
    "tunelabs/gpt-oss-safeguard-120b" : (
        "tunelabs/gpt-oss-safeguard-120b",
        "openai/gpt-oss-safeguard-120b",
    ),
    "tunelabs/functiongemma-270m-it-tunelabs-bnb-4bit" : (
        "tunelabs/functiongemma-270m-it",
        "google/functiongemma-270m-it",
        "tunelabs/functiongemma-270m-it-tunelabs-bnb-4bit",
    ),
    # Ministral 3 models
    "tunelabs/Ministral-3-3B-Instruct-2512-tunelabs-bnb-4bit" : {
        "8" : (
            "mistralai/Ministral-3-3B-Instruct-2512",
            "tunelabs/Ministral-3-3B-Instruct-2512-FP8",
            "tunelabs/Ministral-3-3B-Instruct-2512-FP8",
        ),
        "16" : (
            "tunelabs/Ministral-3-3B-Instruct-2512",
            "mistralai/Ministral-3-3B-Instruct-2512",
            "tunelabs/Ministral-3-3B-Instruct-2512-bnb-4bit",
        ),
    },
    "tunelabs/Ministral-3-3B-Base-2512-tunelabs-bnb-4bit" : (
        "tunelabs/Ministral-3-3B-Base-2512",
        "mistralai/Ministral-3-3B-Base-2512",
        "tunelabs/Ministral-3-3B-Base-2512-bnb-4bit",
    ),
    "tunelabs/Ministral-3-3B-Reasoning-2512-tunelabs-bnb-4bit" : (
        "tunelabs/Ministral-3-3B-Reasoning-2512",
        "mistralai/Ministral-3-3B-Reasoning-2512",
        "tunelabs/Ministral-3-3B-Reasoning-2512-bnb-4bit",
    ),
    "tunelabs/Ministral-3-8B-Instruct-2512-tunelabs-bnb-4bit" : {
        "8" : (
            "mistralai/Ministral-3-8B-Instruct-2512",
            "tunelabs/Ministral-3-8B-Instruct-2512-FP8",
            "tunelabs/Ministral-3-8B-Instruct-2512-FP8",
        ),
        "16" : (
            "tunelabs/Ministral-3-8B-Instruct-2512",
            "mistralai/Ministral-3-8B-Instruct-2512",
            "tunelabs/Ministral-3-8B-Instruct-2512-bnb-4bit",
        ),
    },
    "tunelabs/Ministral-3-8B-Base-2512-tunelabs-bnb-4bit" : (
        "tunelabs/Ministral-3-8B-Base-2512",
        "mistralai/Ministral-3-8B-Base-2512",
        "tunelabs/Ministral-3-8B-Base-2512-bnb-4bit",
    ),
    "tunelabs/Ministral-3-8B-Reasoning-2512-tunelabs-bnb-4bit" : (
        "tunelabs/Ministral-3-8B-Reasoning-2512",
        "mistralai/Ministral-3-8B-Reasoning-2512",
        "tunelabs/Ministral-3-8B-Reasoning-2512-bnb-4bit",
    ),
    "tunelabs/Ministral-3-14B-Instruct-2512-tunelabs-bnb-4bit" : {
        "8" : (
            "mistralai/Ministral-3-14B-Instruct-2512",
            "tunelabs/Ministral-3-14B-Instruct-2512-FP8",
            "tunelabs/Ministral-3-14B-Instruct-2512-FP8",
        ),
        "16" : (
            "tunelabs/Ministral-3-14B-Instruct-2512",
            "mistralai/Ministral-3-14B-Instruct-2512",
            "tunelabs/Ministral-3-14B-Instruct-2512-bnb-4bit",
        ),
    },
    "tunelabs/Ministral-3-14B-Base-2512-tunelabs-bnb-4bit" : (
        "tunelabs/Ministral-3-14B-Base-2512",
        "mistralai/Ministral-3-14B-Base-2512",
        "tunelabs/Ministral-3-14B-Base-2512-bnb-4bit",
    ),
    "tunelabs/Ministral-3-14B-Reasoning-2512-tunelabs-bnb-4bit" : (
        "tunelabs/Ministral-3-14B-Reasoning-2512",
        "mistralai/Ministral-3-14B-Reasoning-2512",
        "tunelabs/Ministral-3-14B-Reasoning-2512-bnb-4bit",
    ),
    "tunelabs/Kimi-K2-Instruct-BF16" : (
        "tunelabs/Kimi-K2-Instruct",
    ),
}

INT_TO_FLOAT_MAPPER  = {}
FLOAT_TO_INT_MAPPER  = {}
MAP_TO_TUNELABS_16bit = {}
FLOAT_TO_FP8_BLOCK_MAPPER = {}
FLOAT_TO_FP8_ROW_MAPPER   = {}


def _add_with_lower(mapper, key, value):
    if key is None:
        return
    mapper[key] = value
    mapper[key.lower()] = value


def _add_lower_only(mapper, key, value):
    if key is None:
        return
    mapper[key.lower()] = value

for key, values in __INT_TO_FLOAT_MAPPER.items():
    block, row = None, None
    if type(values) is dict:
        assert "16" in values
        float16_values = values["16"]
        # Float8 and other quantized types
        if "8" in values:
            float8_values = values["8"]
            assert len(float8_values) == 3
            official, block, row = float8_values
            _add_lower_only(FLOAT_TO_FP8_BLOCK_MAPPER, key, block)
            _add_lower_only(FLOAT_TO_FP8_ROW_MAPPER, key, row)
            _add_lower_only(FLOAT_TO_FP8_BLOCK_MAPPER, official + "-dynamic", block)
            _add_lower_only(FLOAT_TO_FP8_ROW_MAPPER, official, row)
            _add_lower_only(FLOAT_TO_FP8_ROW_MAPPER, official + "-dynamic", row)
            for k in float8_values + float16_values:
                _add_lower_only(FLOAT_TO_FP8_BLOCK_MAPPER, k, block)
                _add_lower_only(FLOAT_TO_FP8_ROW_MAPPER, k, row)

            if float8_values[1] is not None and float8_values[1].startswith("tunelabs"):
                for value in float8_values:
                    if value is not None:
                        _add_with_lower(MAP_TO_TUNELABS_16bit, value, float8_values[1])

            for value in float8_values:
                if value is not None:
                    FLOAT_TO_INT_MAPPER[value] = key
                    FLOAT_TO_INT_MAPPER[value.lower()] = key.lower()
        values = float16_values
    INT_TO_FLOAT_MAPPER[key] = values[0]

    for value in values:
        FLOAT_TO_INT_MAPPER[value] = key

    # Map to TuneLabs version for 16bit versions
    if len(values) == 2:
        if values[0].startswith("tunelabs"):
            _add_with_lower(MAP_TO_TUNELABS_16bit, values[1], values[0])
            _add_with_lower(MAP_TO_TUNELABS_16bit, block, values[0])
            _add_with_lower(MAP_TO_TUNELABS_16bit, row, values[0])
    elif len(values) == 3:
        # Dynamic TuneLabs quantization
        if values[0].startswith("tunelabs"):
            _add_with_lower(MAP_TO_TUNELABS_16bit, values[1], values[0])
            _add_with_lower(MAP_TO_TUNELABS_16bit, values[2], values[0])
            _add_with_lower(MAP_TO_TUNELABS_16bit, block, values[0])
            _add_with_lower(MAP_TO_TUNELABS_16bit, row, values[0])
        pass

    # Get lowercased
    lowered_key = key.lower()
    INT_TO_FLOAT_MAPPER[lowered_key] = values[0].lower()

    for value in values:
        FLOAT_TO_INT_MAPPER[value.lower()] = lowered_key

_add_with_lower(MAP_TO_TUNELABS_16bit, "google/gemma-4-26B-A4B", "tunelabs/gemma-4-26B-A4B")
_add_with_lower(MAP_TO_TUNELABS_16bit, "LiquidAI/LFM2.5-1.2B-Instruct", "tunelabs/LFM2.5-1.2B-Instruct")
