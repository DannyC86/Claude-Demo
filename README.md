# Flowly AI Docs Assistant

A working proof-of-concept for AI-powered product knowledge — built with Claude and the Anthropic API.

## What This Is

Most product documentation goes unread. Users either can't find what they need or give up before they do.

This project explores a simple idea: **what if your product docs could answer questions directly?**

Instead of a search bar that returns pages, users get a conversational interface that reads your documentation and responds in plain English — instantly, accurately, and only based on what your docs actually say.

## Demo

Ask it anything about Flowly (a fictional SaaS product):

> *"What does Flowly do?"*
> *"How much does it cost?"*
> *"Does it integrate with Slack?"*

Claude reads the documentation at startup and uses it as the only source of truth for every answer.

## Why This Pattern Matters

This is a lightweight implementation of **Retrieval-Augmented Generation (RAG)** — a core pattern in production AI products. Rather than relying on a model's general knowledge, the AI is grounded in specific, controlled content.

This matters for product teams because:
- Answers stay accurate and on-brand
- Hallucinations are reduced — Claude only answers from the docs
- The docs folder can be updated without changing any code
- **Prompt caching** is built in, reducing API costs on repeated queries

## Tech Stack

- **Claude Sonnet** (Anthropic API) — the AI backbone
- **Flask** — lightweight Python backend
- **Vanilla HTML/CSS/JS** — clean chat UI, no frameworks needed

## How to Run It

**Prerequisites:** Python 3.10+, an Anthropic API key from [console.anthropic.com](https://console.anthropic.com)

```bash
# Clone the repo
git clone https://github.com/DannyC86/Claude-Demo.git
cd Claude-Demo

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask anthropic

# Set your API key
export ANTHROPIC_API_KEY=your-key-here

# Run the app
python server.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Customising It

To point this at a real product, just replace the contents of the `docs/` folder with your own markdown files. The backend loads all `.md` files at startup automatically — no code changes needed.

## What I Learned

This project was my first hands-on experience with:
- **Claude Code** — using AI to scaffold and build a working app end to end
- **Prompt engineering** — grounding model responses in specific source material
- **The Anthropic API** — integrating Claude into a real product flow
- **Prompt caching** — a practical cost optimisation for production AI apps

Built as a demonstration of how quickly a meaningful AI-powered product experience can be prototyped — from zero to working demo in a single session.

---

*Built with [Claude Code](https://claude.ai/product/claude-code) and the [Anthropic API](https://www.anthropic.com)*
