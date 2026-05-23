from flask import Flask, request, jsonify
from pathlib import Path
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic()

def load_docs():
    docs_dir = Path("docs")
    parts = []
    for doc_file in sorted(docs_dir.glob("*.md")):
        parts.append(doc_file.read_text())
    return "\n\n---\n\n".join(parts)

DOCS = load_docs()

SYSTEM_PROMPT = f"""You are a helpful documentation assistant for Flowly, a project management platform.

Answer questions using ONLY the documentation provided below. If the answer is not found in the documentation, say so clearly — do not use outside knowledge.

<documentation>
{DOCS}
</documentation>"""


@app.route("/")
def index():
    return Path("index.html").read_text()


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": question}],
    )

    return jsonify({"answer": response.content[0].text})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
