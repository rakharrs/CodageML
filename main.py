from flask import Flask, jsonify

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Lancement du Débogueur
app.config["DEBUG"] = True


@app.route('/test', methods=['GET'])
def api_():
    return jsonify("YOO")


app.run(host='0.0.0.0', port=8889)
