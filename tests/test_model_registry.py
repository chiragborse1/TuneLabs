"""Register each model set and check the registered ids exist on the HF Hub."""

from dataclasses import dataclass

import pytest
from huggingface_hub import ModelInfo as HfModelInfo

from tunelabs.registry import register_models, search_models
from tunelabs.registry._deepseek import register_deepseek_models
from tunelabs.registry._gemma import register_gemma_models
from tunelabs.registry._llama import register_llama_models
from tunelabs.registry._mistral import register_mistral_models
from tunelabs.registry._phi import register_phi_models
from tunelabs.registry._qwen import register_qwen_models
from tunelabs.registry.registry import MODEL_REGISTRY, QUANT_TAG_MAP, QuantType
from tunelabs.utils.hf_hub import get_model_info

MODEL_NAMES = [
    "llama",
    "qwen",
    "mistral",
    "phi",
    "gemma",
    "deepseek",
]
MODEL_REGISTRATION_METHODS = [
    register_llama_models,
    register_qwen_models,
    register_mistral_models,
    register_phi_models,
    register_gemma_models,
    register_deepseek_models,
]


@dataclass
class ModelTestParam:
    name: str
    register_models: callable


def _test_model_uploaded(model_ids: list[str]):
    missing_models = []
    for _id in model_ids:
        model_info: HfModelInfo = get_model_info(_id)
        if not model_info:
            missing_models.append(_id)

    return missing_models


TestParams = [
    ModelTestParam(name, models) for name, models in zip(MODEL_NAMES, MODEL_REGISTRATION_METHODS)
]


@pytest.mark.parametrize("model_test_param", TestParams, ids = lambda param: param.name)
def test_model_registration(model_test_param: ModelTestParam):
    MODEL_REGISTRY.clear()
    registration_method = model_test_param.register_models
    registration_method()
    registered_models = MODEL_REGISTRY.keys()
    missing_models = _test_model_uploaded(registered_models)
    assert not missing_models, f"{model_test_param.name} missing following models: {missing_models}"


def test_all_model_registration():
    register_models()
    registered_models = MODEL_REGISTRY.keys()
    missing_models = _test_model_uploaded(registered_models)
    assert not missing_models, f"Missing following models: {missing_models}"


def test_quant_type():
    # NOTE: for org="tunelabs" models, QuantType.NONE aliases QuantType.TUNELABS
    dynamic_quant_models = search_models(quant_types = [QuantType.TUNELABS])
    assert all(m.quant_type == QuantType.TUNELABS for m in dynamic_quant_models)
    quant_tag = QUANT_TAG_MAP[QuantType.TUNELABS]
    assert all(quant_tag in m.model_path for m in dynamic_quant_models)
