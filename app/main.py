from flask import Flask
from flask import jsonify
from newspaper import Article

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return "build 3"

@app.route("/noticia/<path:url>")
def noticia(url):
    article = Article(url)
    article.download()
    article.parse()

    resp = {'title': article.title, 'summary': article.summary, 'text':article.text, 'publish_date': article.publish_date, 
    'top_image': article.top_image}

    return jsonify(resp)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)