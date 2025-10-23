# 🚀 Jenkins CI/CD Flask App on Kubernetes

A complete **CI/CD pipeline** project using **Jenkins**, **Docker**, and **Kubernetes**, built by *Tarique Ali*.

---

## 📘 Overview
This project demonstrates an automated pipeline to:
1. Build a Docker image for a Flask app
2. Push it to DockerHub
3. Deploy automatically to a Kubernetes cluster

---

## 🧱 Project Structure
```
jenkins-cicd-flask-k8s/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── requirements.txt
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── Jenkinsfile
└── README.md
```

---

## ⚙️ Jenkins Pipeline Flow

1. **Clone Repository** – Pulls the latest code from GitHub  
2. **Build Docker Image** – Builds app image using Dockerfile  
3. **Push to DockerHub** – Publishes image to your DockerHub registry  
4. **Deploy to Kubernetes** – Applies manifests via `kubectl apply`  

---

## 🧠 Technologies Used
- Jenkins 🧩  
- Docker 🐳  
- Kubernetes ☸️  
- Python Flask 🐍  
- GitHub Actions (Optional for webhook triggers)

---

## 🌐 Access the App
Once deployed, access via NodePort:
```
http://<node-ip>:30080
```

---

👨‍💻 **Author:** Tarique Ali  
🔗 **GitHub:** [Tariqueali17](https://github.com/Tariqueali17)  
🐳 **DockerHub:** [tariqueali1731](https://hub.docker.com/u/tariqueali1731)
🌍 **Website:** [https://devopswithtarique.online](https://devopswithtarique.online)
