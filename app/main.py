from flask import Flask, jsonify, request, Response
from newspaper import Article
from functools import wraps

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return "build 3"

def check_auth(username, password):
    return username == 'admin' and password == '123456'  

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})  

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated    

@app.route("/noticia/<path:url>")
@requires_auth
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