import requests as req,json
import urllib.parse

from flask import Flask , jsonify ,request, send_file , render_template
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def page_not_found(e):
    
    return "Wkwkwkw", 404


@app.route("/unscramble/<hint>")
def unscramble(hint):

	url = f"http://www.anagramica.com/all/{hint}"

	fetch = req.get(url).json()

	word = fetch['all'][0]

	if(len(word) == len(hint)){
		result = {"result":True,"word":word.upper()}
	}else{
		result = {"result":False,"word":"None"}
	}

	return jsonify(result)


@app.route("/")
def hello_world():
  
  return 'Hello Ecandl.net'



  