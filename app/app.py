from flask import Flask, jsonify, render_template
import random
import time
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [INFO] - %(message)s')

@app.route('/')
def home():
    logging.info("Dashboard viewed")
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    statuses = ["Running", "Deploying", "Failed", "Pending"]
    jenkins_status = random.choice(["Passed", "Running", "Failed"])
    kubernetes_status = random.choice(["Healthy", "Warning", "Degraded"])
    docker_tags = ["latest", "v1.1", "v2.0", "stable"]

    data = {
        "status": random.choice(statuses),
        "jenkins": jenkins_status,
        "kubernetes": kubernetes_status,
        "docker_image": f"tariqueali1731/flask-app:{random.choice(docker_tags)}",
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "developer": "Tarique Ali"
    }

    logging.info(f"API /status accessed: {data}")
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
