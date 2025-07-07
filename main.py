from flask import Flask, request, jsonify
from aliexpress_api import AliexpressAPI

app = Flask(__name__)
api = AliexpressAPI()

@app.route("/generate", methods=["GET"])
def generate():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing URL parameter"}), 400
    try:
        result = api.generate_affiliate_link(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
