# TuneLabs

Run and fine-tune LLMs locally on your own hardware. No cloud required.

## Install

**macOS / Linux / WSL:**

```bash
curl -fsSL https://tunelabs.ai/install.sh | sh
```

**Windows (PowerShell):**

```powershell
irm https://tunelabs.ai/install.ps1 | iex
```

**pip (Python package, no UI):**

```bash
pip install tunelabs
```

**Launch:**

```bash
tunelabs studio -p 8888
```

Open `http://localhost:8888` in your browser.

## About

TuneLabs provides everything you need to work with LLMs locally:

- **Inference** – Search, download, and run GGUF, LoRA, and safetensor models. Chat with images, audio, PDFs, and code. Connect API providers (OpenAI, Anthropic) or local servers (vLLM, Ollama).
- **Training** – Fine-tune 500+ models up to 2x faster using 70% less VRAM. Supports full fine-tuning, RL (GRPO), LoRA/QLoRA, and FP8 training. Multi-GPU supported.
- **Data Recipes** – Auto-create training datasets from PDFs, CSVs, DOCX, and more.
- **Export** – Save models to GGUF, 16-bit safetensors, and other formats.

## Links

- [Documentation](https://tunelabs.ai/docs)
- [Discord](https://discord.gg/tunelabs)
- [Twitter / X](https://x.com/TuneLabsAI)
- [Reddit](https://reddit.com/r/tunelabs)
- [GitHub](https://github.com/chiragborse1/TuneLabs)
