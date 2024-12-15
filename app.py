from flask import Flask, request, jsonify
from langchain.document_loaders import PyPDFLoader
from langchain_openai.embeddings import OpenAIEmbeddings
import os
import json

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key not found. Set it as an environment variable.")
PDF_FILE_PATH = os.getenv("PDF_FILE_PATH", "s65.pdf")
EMBEDDINGS_FILE = "embeddings.json"

# Create embeddings and store them in JSON
def create_embeddings():
    loader = PyPDFLoader(PDF_FILE_PATH)
    documents = loader.load()
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    embedding_data = [
        {"content": doc.page_content, "embedding": embeddings.embed_query(doc.page_content)}
        for doc in documents
    ]

    with open(EMBEDDINGS_FILE, "w") as f:
        json.dump(embedding_data, f)
    return embedding_data

# Load embeddings
if not os.path.exists(EMBEDDINGS_FILE):
    embedding_data = create_embeddings()
else:
    with open(EMBEDDINGS_FILE, "r") as f:
        embedding_data = json.load(f)

@app.route('/query', methods=['POST'])
def query_pdf():
    try:
        data = request.json
        query = data.get('query', '')
        if not query:
            return jsonify({'error': 'Query not provided'}), 400

        # Embed the query
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        query_embedding = embeddings.embed_query(query)

        # Compute similarities
        results = sorted(
            embedding_data,
            key=lambda x: cosine_similarity(query_embedding, x["embedding"]),
            reverse=True
        )[:3]

        return jsonify({'results': [result["content"] for result in results]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cosine_similarity(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2)) / (sum(x**2 for x in vec1)**0.5 * sum(y**2 for y in vec2)**0.5)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
