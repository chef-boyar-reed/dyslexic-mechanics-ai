from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
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
            input[type=text] {
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
        </style>
    </head>
    <body>
        <h1>Dyslexic Mechanics AI</h1>
        <form action=/search method=POST>
            <input type=text name=query placeholder=Search manuals...>
            <button type=submit>Search</button>
        </form>
    </body>
    </html>
    '''
    return html_content

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '')
    if not query:
        return '<h2>No query entered.</h2>', 400
    return f'<h2>Searching for: {query}</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

