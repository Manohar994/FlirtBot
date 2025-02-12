from flask import Flask, render_template, request, jsonify
import random
from pickup_lines import pickup_lines

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_pickup_line", methods=["POST"])
def get_pickup_line():
    data = request.get_json()
    name = data.get("name", "Crush")  # Default name if none provided
    line = random.choice(pickup_lines).replace("{name}", name)
    return jsonify({"line": line})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

