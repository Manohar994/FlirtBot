from flask import Flask, render_template, request, jsonify
import random
from pickup_lines import pickup_lines

app = Flask(__name__)

# Home route to render the main page
@app.route("/")
def home():
    return render_template("index.html")

# API route to get a random pickup line
@app.route("/get_pickup_line", methods=["POST"])
def get_pickup_line():
    data = request.get_json()
    name = data.get("name", "Crush")  # Default to "Crush" if no name is provided
    line = random.choice(pickup_lines).replace("{name}", name)
    return jsonify({"line": line})

# Health check route (for debugging and deployment verification)
@app.route("/health")
def health():
    return "Hello, FlirtBot is live!"

# Main entry point for running the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


