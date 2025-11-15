# Real-Time Multilingual Query Handler

This is a small, local Streamlit app that detects the language of an input text, translates it into English (by default) using `deep-translator`'s Google translator backend, and offers a short neutral suggested response. The app is intentionally simple and framework-free.

## Clone the repository

Clone this repository locally using `git`. Replace `OWNER` and `REPO` with the correct values, or copy the URL from your remote provider (GitHub, GitLab, etc.). Example (GitHub):

```bash
git clone https://github.com/spabhijna/Real-Time-Multilingual-Query-Handler_HiDevs.git
cd Real-Time-Multilingual-Query-Handler_HiDevs
```

If you already have the remote configured and want to fetch the latest changes:

```bash
git pull origin main
```

**Notes:**
- The project requires Python >= 3.12 (see `pyproject.toml`).
- You said you use `uv` for dependency control — instructions for `uv` are below. A `pip` fallback is also provided.

## Quick start (using `uv`)

1. Create or activate your Python environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies with `uv` (your environment may vary). If your `uv` setup reads `pyproject.toml`, run:

```bash
uv install
```

If your `uv` workflow requires a different command (for example `uv sync` or `uv run`), use the appropriate `uv` command you normally run to install from `pyproject.toml`.

## Fallback: install with pip

If you don't have `uv` available, install dependencies with `pip`:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r <(python3 - <<'PY'
from pathlib import Path
import tomllib
data = tomllib.loads(Path('pyproject.toml').read_text())
deps = data.get('project', {}).get('dependencies', [])
print('\n'.join(deps))
PY
)
```

Or a simpler approach (manual):

```bash
python3 -m pip install deep-translator langdetect openai pandas streamlit
```

## Run the app

Start Streamlit from the repository root:

```bash
streamlit run main.py
```

Open the URL printed by Streamlit (usually http://localhost:8501) in your browser.



## Troubleshooting

- If Streamlit errors mention `st.session_state` modifications: ensure you are using the latest edited `main.py` and that the `Clear input` button is the one provided by this repo.
- If translation fails with `deep-translator`, check your internet connection — the GoogleTranslator backend relies on network access.
- If you have Python version issues, verify `python --version` and use Python 3.12+.

## Development notes

- To run a quick syntax check locally:

```bash
python3 -m py_compile main.py
```

- The dependencies are listed in `pyproject.toml` under the `[project].dependencies` key.



Credits: original repository owner.

