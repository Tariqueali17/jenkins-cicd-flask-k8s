from flask import Flask, render_template, jsonify
import logging
import os

app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] - %(message)s")

@app.route("/")
def home():
    logging.info("Home endpoint accessed")
    environment = os.getenv("APP_ENV", "development")
    return render_template("index.html", environment=environment)

@app.route("/api/status")
def api_status():
    logging.info("API status endpoint accessed")
    return jsonify({
        "environment": os.getenv("APP_ENV", "development"),
        "message": "🚀 Flask CI/CD App is Running Successfully!",
        "status": "success"
    })

if __name__ == "__main__":
    logging.info("Starting Flask App on 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)
