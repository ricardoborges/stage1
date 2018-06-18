from flask import Flask, jsonify, request, abort
from newspaper import Article
from functools import wraps

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

def require_appkey(apifunction):
    @wraps(apifunction)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.args.get('key') and request.args.get('key') == "698dc19d489c4e4db73e28a713eab07b":
            return apifunction(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

@app.route("/")
def hello():
    return "build 4"

@app.route("/noticia/<path:url>")
@require_appkey
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