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
<<<<<<< HEAD
│   ├── app.py                     # Main Flask application
=======
<<<<<<< HEAD
│   ├── app.py                     # Flask application entry point
>>>>>>> 47e501e (Update README.md)
│   ├── requirements.txt           # Python dependencies
│   │
│   ├── static/                    # Static assets (CSS, JS, Images)
│   │   ├── style.css              # UI styling for the Flask app
│   │   └── script.js              # (optional) For animations or live updates
│   │
│   └── templates/                 # HTML templates
│       └── index.html             # Main dashboard UI (with “Tarique Ali” branding)
│
├── k8s/                           # Kubernetes manifests
│   ├── deployment.yaml            # K8s deployment configuration
│   └── service.yaml               # K8s service definition (NodePort/LoadBalancer)
│
<<<<<<< HEAD
=======
├── Dockerfile                     # Docker build instructions
├── Jenkinsfile                    # CI/CD pipeline (build → test → deploy)
├── .gitignore                     # Ignore unnecessary files
└── README.md                      # Documentation
=======
│   ├── app.py                     # Main Flask application
│   ├── requirements.txt           # Python dependencies
│   │
│   ├── static/                    # Static assets (CSS, JS, Images)
│   │   ├── style.css              # UI styling for the Flask app
│   │   └── script.js              # (optional) For animations or live updates
│   │
│   └── templates/                 # HTML templates
│       └── index.html             # Main dashboard UI (with “Tarique Ali” branding)
│
├── k8s/                           # Kubernetes manifests
│   ├── deployment.yaml            # K8s deployment configuration
│   └── service.yaml               # K8s service definition (NodePort/LoadBalancer)
│
>>>>>>> 47e501e (Update README.md)
├── Dockerfile                     # Docker image build instructions
│
├── Jenkinsfile                    # CI/CD pipeline for Jenkins
│
├── .gitignore                     # Ignore virtual env, __pycache__, etc.
│
└── README.md                      # Project overview and setup guide
<<<<<<< HEAD
=======
>>>>>>> 63ca4f9 (Update README.md)
>>>>>>> 47e501e (Update README.md)

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
