from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dyslexic Mechanics AI</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #ffffff;
                color: #000000;
                text-align: center;
            }
            input[type="text"] {
                padding: 10px;
                width: 300px;
                margin: 10px;
                border: 1px solid #000;
            }
            button {
                padding: 10px 20px;
                background-color: #000;
                color: #fff;
                border: none;
                cursor: pointer;
            }
            #result {
                margin-top: 20px;
                font-weight: bold;
            }
        </style>
        <script>
            async function 
cat > app.py <<EOF
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dyslexic Mechanics AI</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #ffffff;
                color: #000000;
                text-align: center;
            }
            input[type="text"] {
                padding: 10px;
                width: 300px;
                margin: 10px;
                border: 1px solid #000;
            }
            button {
                padding: 10px 20px;
                background-color: #000;
                color: #fff;
                border: none;
                cursor: pointer;
            }
            #result {
                margin-top: 20px;
                font-weight: bold;
            }
        </style>
        <script>
            async function search() {
                const query = document.getElementById('query').value;
                if (!query) {
                    document.getElementById('result').innerText = 'Please enter a query.';
                    return;
                }
                const response = await fetch('/search', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query })
                });
                if (!response.ok) {
                    document.getElementById('result').innerText = 'Error performing search. Please try again.';
                    return;
                }
                const data = await response.json();
                document.getElementById('result').innerText = data.result || 'No results found.';
            }
        </script>
    </head>
    <body>
        <h1>Dyslexic Mechanics AI</h1>
        <input type="text" id="query" placeholder="Search manuals...">
        <button onclick="search()">Search</button>
        <div id="result"></div>
    </body>
    </html>
    '''
    return html_content

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'result': 'Please provide a valid query.'}), 400

    # Replace this placeholder logic with your actual search logic.
    example_manuals = [
        'Example Manual 1',
        'Example Manual 2',
        'Example Manual 3'
    ]
    filtered_results = [manual for manual in example_manuals if query.lower() in manual.lower()]

    if not filtered_results:
        return jsonify({'result': f'No results found for "{query}".'}), 200

    return jsonify({'result': f'Results for "{query}": {", ".join(filtered_results)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
