# Simple Flask Application

This project is a simple python application written using flask framework to greet users. The main objective of this project is focused on creating a python flask application, containerize it and deploy it on a Kubernetes cluster. The application is containerized/packaged using Docker and deployed on a Minikube cluster. 

### To run application locally
#### Create and Activate Virtual Environment to install Python packages.
```
python -m venv venv
source vnev/bin/activate
```
#### Run Python application
```
python3 simple.py
```
The application can be accessed at `http://localhost/5000`
#### Deactivate Virtual Enivronment
```
deactivate
```

### To containerize application using Docker
#### Build Docker Image
```
docker build -t simple-app:0.1 .
```
#### Run Docker Container
```
docker run -p 5000:5000 simple-app:0.1
```

### Deploy application on Minikube Kubernetes Cluster
#### Start Minikube
```
minikube start --driver=docker
```
#### To deploy/apply application service on Kubernetes Cluster
```
kubectl apply -f deployment.yaml
```
#### To get a list of deployments and services
```
kubectl get deployment
kubectl get service
```
#### Start the application service
```
minikube service simple-app-service
```
The application can be accessed at `http://<EXTERNAL_IP>/<PORT>`