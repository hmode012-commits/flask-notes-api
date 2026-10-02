from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home() -> jsonify:
    """Welcome endpoint for the backend API."""
    return jsonify(
        {
            "message": "Welcome to my mohammed basim professional backend API!",
            "status": "success",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
