<h1 align="center" style="margin:0;">
  <a href="https://tunelabs.ai/docs"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tunelabsai/tunelabs/main/images/tunelabs%20logo%20white%20text.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tunelabsai/tunelabs/main/images/tunelabs%20logo%20black%20text.png">
    <img alt="TuneLabs logo" src="https://raw.githubusercontent.com/tunelabsai/tunelabs/main/images/tunelabs%20logo%20black%20text.png" height="80" style="max-width:100%;">
  </picture></a>
</h1>
<h3 align="center" style="margin: 0; margin-top: 0;">
TuneLabs Studio lets you run and train models locally.
</h3>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-install">Quickstart</a> •
  <a href="#-free-notebooks">Notebooks</a> •
  <a href="https://tunelabs.ai/docs">Documentation</a>
</p>
<br>
<a href="https://tunelabs.ai/docs/new/studio">
<img alt="tunelabs studio ui homepage" src="https://github.com/user-attachments/assets/53ae17a9-d975-44ef-9686-efb4ebd0454d" style="max-width: 100%; margin-bottom: 0;"></a>

## ⚡ Get started

#### macOS, Linux, WSL:
```bash
curl -fsSL https://tunelabs.ai/install.sh | sh
```
#### Windows:
```powershell
irm https://tunelabs.ai/install.ps1 | iex
```
#### Community:

- [Discord](https://discord.gg/tunelabs)
- [𝕏 (Twitter)](https://x.com/TuneLabsAI)
- [Reddit](https://reddit.com/r/tunelabs)

## ⭐ Features
TuneLabs Studio (Beta) lets you run and train text, [audio](https://tunelabs.ai/docs/basics/text-to-speech-tts-fine-tuning), [embedding](https://tunelabs.ai/docs/new/embedding-finetuning), [vision](https://tunelabs.ai/docs/basics/vision-fine-tuning) models on Windows, Linux and macOS.

### Inference
* **Search + download + run models** including GGUF, LoRA adapters, safetensors
* **Export models**: [Save or export](https://tunelabs.ai/docs/new/studio/export) models to GGUF, 16-bit safetensors and other formats.
* **Tool calling**: Support for [self-healing tool calling](https://tunelabs.ai/docs/new/studio/chat#auto-healing-tool-calling) and web search
* **[Code execution](https://tunelabs.ai/docs/new/studio/chat#code-execution)**: lets LLMs test code in Claude artifacts and sandbox environments
* **[API inference endpoint](https://tunelabs.ai/docs/basics/api)**: Deploy and run local LLMs in Claude Code, Codex tools with TuneLabs
* [Auto set inference settings](https://tunelabs.ai/docs/new/studio/chat#auto-parameter-tuning) and customize chat templates.
* We work directly with teams behind [gpt-oss](https://docs.tunelabs.ai/new/gpt-oss-how-to-run-and-fine-tune#tunelabs-fixes-for-gpt-oss), [Qwen3](https://www.reddit.com/r/LocalLLaMA/comments/1kaodxu/qwen3_tunelabs_dynamic_ggufs_128k_context_bug_fixes/), [Llama 4](https://github.com/ggml-org/llama.cpp/pull/12889), [Mistral](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/discussions/18), [Gemma 1-3](https://news.ycombinator.com/item?id=39671146), and [Phi-4](https://tunelabs.ai/blog/phi4), where we’ve fixed bugs that improve model accuracy.
* Chat with images, audio, PDFs, code, DOCX and more. [Connect API providers](https://tunelabs.ai/docs/integrations/connections) (OpenAI, Anthropic) or servers (vLLM, Ollama).
### Training
* Train and RL **500+ models** up to **2x faster** with up to **70% less VRAM**, with no accuracy loss.
* Custom Triton and mathematical **kernels**. See some collabs we did with [PyTorch](https://tunelabs.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) and [Hugging Face](https://tunelabs.ai/docs/new/faster-moe).
* **Data Recipes**: [Auto-create datasets](https://tunelabs.ai/docs/new/studio/data-recipe) from **PDF, CSV, DOCX** etc. Edit data in a visual-node workflow.
* **[Reinforcement Learning](https://tunelabs.ai/docs/get-started/reinforcement-learning-rl-guide)** (RL): The most efficient [RL](https://tunelabs.ai/docs/get-started/reinforcement-learning-rl-guide) library, using **80% less VRAM** for GRPO, [FP8](https://tunelabs.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) etc.
* Supports full fine-tuning, RL, pretraining, 4-bit, 16-bit and, FP8 training.
* **Observability**: Monitor training live, track loss and GPU usage and customize graphs.
* [Multi-GPU](https://tunelabs.ai/docs/basics/multi-gpu-training-with-tunelabs) training is supported, with major improvements coming soon.

## 📥 Install
TuneLabs can be used in two ways: through **[TuneLabs Studio](https://tunelabs.ai/docs/new/studio/)**, the web UI, or through **TuneLabs Core**, the code-based version. Each has different requirements.

### TuneLabs Studio (web UI)
TuneLabs Studio (Beta) works on **Windows, Linux, WSL** and **macOS**.

* **CPU:** Supported for Chat and Data Recipes currently
* **NVIDIA:** Training works on RTX 30/40/50, Blackwell, DGX Spark, Station and more
* **macOS:** Training, MLX and GGUF inference are ALL supported.
* **AMD:** Chat + Data works. Train with [TuneLabs Core](#tunelabs-core-code-based). Studio support is out soon.
* **Multi-GPU:** Available now, with a major upgrade on the way

#### macOS, Linux, WSL:
```bash
curl -fsSL https://tunelabs.ai/install.sh | sh
```
Use the same command to update.

#### Windows:
```powershell
irm https://tunelabs.ai/install.ps1 | iex
```
Use the same command to update.

#### Launch
```bash
tunelabs studio -p 8888
```
For cloud or global access, add `-H 0.0.0.0`. By default, TuneLabs is accessible only locally.

For a secure HTTPS link instead of a raw network port, use `tunelabs studio --secure`. Studio stays bound to localhost and is served only through a free Cloudflare HTTPS tunnel (it fails closed if the tunnel can't start, so the raw port is never exposed).

#### Docker
Use our [Docker image](https://hub.docker.com/r/tunelabs/tunelabs) ```tunelabs/tunelabs``` container. Run:
```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  tunelabs/tunelabs
  ```

#### Developer, Nightly, Uninstall
To see developer, nightly and uninstallation etc. instructions, see [advanced installation](#-advanced-installation).

### TuneLabs Core (code-based)
#### Linux, WSL:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv tunelabs_env --python 3.13
source tunelabs_env/bin/activate
uv pip install tunelabs --torch-backend=auto
```
#### Windows:
```powershell
winget install -e --id Python.Python.3.13
winget install --id=astral-sh.uv  -e
uv venv tunelabs_env --python 3.13
.\tunelabs_env\Scripts\activate
uv pip install tunelabs --torch-backend=auto
```
For Windows, `pip install tunelabs` works only if you have PyTorch installed. Read our [Windows Guide](https://tunelabs.ai/docs/get-started/install/windows-installation).
You can use the same Docker image as TuneLabs Studio.

#### AMD, Intel:
For RTX 50x, B200, 6000 GPUs: `uv pip install tunelabs --torch-backend=auto`. Read our guides for: [Blackwell](https://tunelabs.ai/docs/blog/fine-tuning-llms-with-blackwell-rtx-50-series-and-tunelabs) and [DGX Spark](https://tunelabs.ai/docs/blog/fine-tuning-llms-with-nvidia-dgx-spark-and-tunelabs). <br>
To install TuneLabs on **AMD** and **Intel** GPUs, follow our [AMD Guide](https://tunelabs.ai/docs/get-started/install/amd) and [Intel Guide](https://tunelabs.ai/docs/get-started/install/intel).

## 📒 Free Notebooks

Train for free with our notebooks. You can use our new [free TuneLabs Studio notebook](https://colab.research.google.com/github/tunelabsai/tunelabs/blob/main/studio/TuneLabs_Studio_Colab.ipynb) to run and train models for free in a web UI.
Read our [guide](https://tunelabs.ai/docs/get-started/fine-tuning-llms-guide). Add dataset, run, then deploy your trained model.

| Model | Free Notebooks | Performance | Memory use |
|-----------|---------|--------|----------|
| **Gemma 4 (E2B)**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Gemma4_(E2B)-Vision.ipynb)               | 1.5x faster | 50% less |
| **Qwen3.5 (4B)**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Qwen3_5_(4B)_Vision.ipynb)               | 1.5x faster | 60% less |
| **gpt-oss (20B)**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/gpt-oss-(20B)-Fine-tuning.ipynb)               | 2x faster | 70% less |
| **Qwen3.5 GSPO**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Qwen3_5_(4B)_Vision_GRPO.ipynb)               | 2x faster | 70% less |
| **gpt-oss (20B): GRPO**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/gpt-oss-(20B)-GRPO.ipynb)               | 2x faster | 80% less |
| **Qwen3: Advanced GRPO**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Qwen3_(4B)-GRPO.ipynb)               | 2x faster | 70% less |
| **embeddinggemma (300M)**    | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/EmbeddingGemma_(300M).ipynb)               | 2x faster | 20% less |
| **Mistral Ministral 3 (3B)**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Ministral_3_VL_(3B)_Vision.ipynb)               | 1.5x faster | 60% less |
| **Llama 3.1 (8B) Alpaca**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb)               | 2x faster | 70% less |
| **Llama 3.2 Conversational**      | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Llama3.2_(1B_and_3B)-Conversational.ipynb)               | 2x faster | 70% less |
| **Orpheus-TTS (3B)**     | [▶️ Start for free](https://colab.research.google.com/github/tunelabsai/notebooks/blob/main/nb/Orpheus_(3B)-TTS.ipynb)               | 1.5x faster | 50% less |

- See all our notebooks for: [Kaggle](https://github.com/tunelabsai/notebooks?tab=readme-ov-file#-kaggle-notebooks), [GRPO](https://tunelabs.ai/docs/get-started/tunelabs-notebooks#grpo-reasoning-rl-notebooks), [TTS](https://tunelabs.ai/docs/get-started/tunelabs-notebooks#text-to-speech-tts-notebooks), [embedding](https://tunelabs.ai/docs/new/embedding-finetuning) & [Vision](https://tunelabs.ai/docs/get-started/tunelabs-notebooks#vision-multimodal-notebooks)
- See [all our models](https://tunelabs.ai/docs/get-started/tunelabs-model-catalog) and [all our notebooks](https://tunelabs.ai/docs/get-started/tunelabs-notebooks)
- See detailed documentation for TuneLabs [here](https://tunelabs.ai/docs)

## 🦥 TuneLabs News
- **Connections**: Connect any API provider (OpenAI, Anthropic) or server (vLLM, Ollama). [Guide](https://tunelabs.ai/docs/integrations/connections)
- **MTP**: Run Qwen3.6 MTP in TuneLabs. MTP settings are autoset specific to your hardware. [Guide](https://tunelabs.ai/docs/models/qwen3.6#mtp-guide)
- **API inference endpoint**: Deploy and run local LLMs in Claude Code, Codex tools. [Guide](https://tunelabs.ai/docs/basics/api)
- **Qwen3.6**: Qwen3.6-35B-A3B can now be trained and run in TuneLabs Studio. [Blog](https://tunelabs.ai/docs/models/qwen3.6)
- **Gemma 4**: Run and train Google’s new models directly in TuneLabs. [Blog](https://tunelabs.ai/docs/models/gemma-4)
- **Introducing TuneLabs Studio**: our new web UI for running and training LLMs. [Blog](https://tunelabs.ai/docs/new/studio)
- **Qwen3.5** - 0.8B, 2B, 4B, 9B, 27B, 35-A3B, 112B-A10B are now supported. [Guide + notebooks](https://tunelabs.ai/docs/models/qwen3.5/fine-tune)
- Train **MoE LLMs 12x faster** with 35% less VRAM - DeepSeek, GLM, Qwen and gpt-oss. [Blog](https://tunelabs.ai/docs/new/faster-moe)
- **Embedding models**: TuneLabs now supports ~1.8-3.3x faster embedding fine-tuning. [Blog](https://tunelabs.ai/docs/new/embedding-finetuning) • [Notebooks](https://tunelabs.ai/docs/get-started/tunelabs-notebooks#embedding-models)
- New **7x longer context RL** vs. all other setups, via our new batching algorithms. [Blog](https://tunelabs.ai/docs/new/grpo-long-context)
- New RoPE & MLP **Triton Kernels** & **Padding Free + Packing**: 3x faster training & 30% less VRAM. [Blog](https://tunelabs.ai/docs/new/3x-faster-training-packing)
- **500K Context**: Training a 20B model with >500K context is now possible on an 80GB GPU. [Blog](https://tunelabs.ai/docs/blog/500k-context-length-fine-tuning)
- **FP8 & Vision RL**: You can now do FP8 & VLM GRPO on consumer GPUs. [FP8 Blog](https://tunelabs.ai/docs/get-started/reinforcement-learning-rl-guide/fp8-reinforcement-learning) • [Vision RL](https://tunelabs.ai/docs/get-started/reinforcement-learning-rl-guide/vision-reinforcement-learning-vlm-rl)

## 📥 Advanced Installation
The below advanced instructions are for TuneLabs Studio. For TuneLabs Core advanced installation, [view our docs](https://tunelabs.ai/docs/get-started/install/pip-install#advanced-pip-installation).
#### Developer / Nightly / Experimental installs: macOS, Linux, WSL:
The developer install builds from the `main` branch, which is the latest (nightly) source.
```bash
git clone https://github.com/tunelabsai/tunelabs
cd tunelabs
./install.sh --local
tunelabs studio -p 8888
```
To install into an isolated location (its own virtual env, `auth/`, `studio.db`, cache and llama.cpp build), set `TUNELABS_STUDIO_HOME` and pass it again at launch:
```bash
TUNELABS_STUDIO_HOME="$PWD/.studio" ./install.sh --local
TUNELABS_STUDIO_HOME="$PWD/.studio" tunelabs studio -p 8888
```
Then to update :
```bash
cd tunelabs && git pull
./install.sh --local
tunelabs studio -p 8888
```

#### Developer / Nightly / Experimental installs: Windows PowerShell:
The developer install builds from the `main` branch, which is the latest (nightly) source.
```powershell
git clone https://github.com/tunelabsai/tunelabs.git
cd tunelabs
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
tunelabs studio -p 8888
```
To install into an isolated location (its own virtual env, `auth/`, `studio.db`, cache and llama.cpp build), set `TUNELABS_STUDIO_HOME` and pass it again at launch:
```powershell
$env:TUNELABS_STUDIO_HOME="$PWD\.studio"; .\install.ps1 --local
$env:TUNELABS_STUDIO_HOME="$PWD\.studio"; tunelabs studio -p 8888
```
Then to update :
```powershell
cd tunelabs; git pull
.\install.ps1 --local
tunelabs studio -p 8888
```

#### Remote access: `--secure` (HTTPS tunnel) vs raw port
By default `tunelabs studio` binds to `127.0.0.1` (this machine only). To reach it from another device, pick one of:

- `--secure` (recommended): serve **only** through a free Cloudflare HTTPS link. Studio stays bound to localhost and the tunnel provides the public URL; it fails closed (does not start) if the tunnel can't come up, so the raw port is never exposed.
```bash
tunelabs studio --secure -p 8888
```
- `-H 0.0.0.0`: bind the raw port on all network interfaces, reachable from anywhere on the network. Only use this on a trusted network.
```bash
tunelabs studio -H 0.0.0.0 -p 8888
```

Server-side tools (web search, Python and terminal code execution) run as your user and are on by default. Anyone who can reach the server with the API key can run code on this machine, so keep your API key private and pass `--disable-tools` when exposing Studio.

#### Advanced launch options
Installer options can be passed as environment variables. On macOS, Linux and WSL place the variable after the pipe so the shell passes it to `sh`; on Windows set it with `$env:` before piping to `iex`.

Skip PyTorch (GGUF-only mode):
```bash
curl -fsSL https://tunelabs.ai/install.sh | TUNELABS_NO_TORCH=1 sh
```
```powershell
$env:TUNELABS_NO_TORCH=1; irm https://tunelabs.ai/install.ps1 | iex
```

Pin the Python version:
```bash
curl -fsSL https://tunelabs.ai/install.sh | TUNELABS_PYTHON=3.12 sh
```
```powershell
$env:TUNELABS_PYTHON='3.12'; irm https://tunelabs.ai/install.ps1 | iex
```

Install to a custom location with `TUNELABS_STUDIO_HOME`:
```bash
curl -fsSL https://tunelabs.ai/install.sh | TUNELABS_STUDIO_HOME=/abs/path sh
```
```powershell
$env:TUNELABS_STUDIO_HOME='C:\path'; irm https://tunelabs.ai/install.ps1 | iex
```

Cap Studio's native CPU thread pools on high-core hosts: `TUNELABS_CPU_THREADS=8 tunelabs studio -p 8888`.

#### Uninstall
The recommended way to fully remove TuneLabs Studio is the matching uninstall script for your OS. It stops any running servers, removes the install dir, the launcher data dir, the desktop shortcut, and any platform-specific entries (macOS `.app` bundle + Launch Services on Mac; Start Menu, `HKCU\Software\TuneLabs` registry key and user `PATH` entries on Windows):

* ​ **MacOS, WSL, Linux:** `curl -fsSL https://raw.githubusercontent.com/tunelabsai/tunelabs/main/scripts/uninstall.sh | sh`
* ​ **Windows (PowerShell):** `irm https://raw.githubusercontent.com/tunelabsai/tunelabs/main/scripts/uninstall.ps1 | iex`

If you only want to drop the install dir and keep the launcher/shortcut for a later reinstall, you can instead run `rm -rf ~/.tunelabs/studio` (Mac/Linux/WSL) or `Remove-Item -Recurse -Force "$HOME\.tunelabs\studio"` (Windows). The model cache at `~/.cache/huggingface` is not touched by any of these.

For more info, [see our docs](https://tunelabs.ai/docs/new/studio/install#uninstall).

#### Deleting model files

You can delete old model files either from the bin icon in model search or by removing the relevant cached model folder from the default Hugging Face cache directory. By default, HF uses:

* ​ **MacOS, Linux, WSL:** `~/.cache/huggingface/hub/`
* ​ **Windows:** `%USERPROFILE%\.cache\huggingface\hub\`

## 💚 Community and Links
| Type                                                                                                                                      | Links                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| <img width="16" src="https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/66e3d80db9971f10a9757c99_Symbol.svg" />  **Discord**                       | [Join Discord server](https://discord.com/invite/tunelabs)                          |
| <img width="15" src="https://redditinc.com/hs-fs/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png" />  **r/tunelabs Reddit**                       | [Join Reddit community](https://reddit.com/r/tunelabs)                          |
| 📚 **Documentation & Wiki**                                                                                                               | [Read Our Docs](https://tunelabs.ai/docs)                                       |
| <img width="13" src="https://upload.wikimedia.org/wikipedia/commons/0/09/X_(formerly_Twitter)_logo_late_2025.svg" />  **Twitter (aka X)** | [Follow us on X](https://twitter.com/tunelabsai)                                |
| 🔮 **Our Models**                                                                                                                         | [TuneLabs Catalog](https://tunelabs.ai/docs/get-started/tunelabs-model-catalog)   |
| ✍️ **Blog**                                                                                                                               | [Read our Blogs](https://tunelabs.ai/blog)                                      |

### Citation

You can cite the TuneLabs repo as follows:
```bibtex
@software{tunelabs,
  author = {Daniel Han, Michael Han and TuneLabs team},
  title = {TuneLabs},
  url = {https://github.com/tunelabsai/tunelabs},
  year = {2023}
}
```
If you trained a model with 🦥TuneLabs, you can use this cool sticker!   <img src="https://raw.githubusercontent.com/tunelabsai/tunelabs/main/images/made with tunelabs.png" width="200" align="center" />

### License
TuneLabs uses a dual-licensing model of Apache 2.0 and AGPL-3.0. The core TuneLabs package remains licensed under **[Apache 2.0](https://github.com/tunelabsai/tunelabs?tab=Apache-2.0-1-ov-file)**, while certain optional components, such as the TuneLabs Studio UI are licensed under the open-source license **[AGPL-3.0](https://github.com/tunelabsai/tunelabs?tab=AGPL-3.0-2-ov-file)**.

This structure helps support ongoing TuneLabs development while keeping the project open source and enabling the broader ecosystem to continue growing.

### Thank You to
- The [llama.cpp library](https://github.com/ggml-org/llama.cpp) that lets users run and save models with TuneLabs
- The Hugging Face team and their libraries: [transformers](https://github.com/huggingface/transformers) and [TRL](https://github.com/huggingface/trl)
- The Pytorch and [Torch AO](https://github.com/tunelabsai/tunelabs/pull/3391) team for their contributions
- NVIDIA for their [NeMo DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner) library and their contributions
- And of course for every single person who has contributed or has used TuneLabs!
