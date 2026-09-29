
from flask import Flask, jsonify

from flask import Flask, request, redirect, url_for
from prediction import predict
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Lancement du Débogueur
app.config["DEBUG"] = True




@app.route('/test', methods=['GET'])
def test():
    return jsonify("YOO")

@app.route('/api/predict', methods=['GET'])
def api_predict():
    code = request.args.get('code')
    pred = predict(code)
    return jsonify(pred)


app.run(host='0.0.0.0', port=8889)
