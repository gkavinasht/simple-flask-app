
## To run application locally
### Create and Activate Virtual Environment to install Python packages.
python -m venv venv
source vnev/bin/activate

### Run Python application
python3 simple.py
To access the application locally, go to http://localhost/5000 in the browser

### Deactivate Virtual Enivronment
deactivate


## To containerize application using Docker
### Build Docker Image
docker build -t simple-app:0.1 .

### Run Docker Container
docker run -p 5000:5000 simple-app:0.1


## Deploy application on Minikube Kubernetes Cluster
### Start Minikube
minikube start --driver=docker

### To deploy/apply deployment and service on Kubernetes Cluster
kubectl apply -f deployment.yaml

### To get a list of deployments and services
kubectl get deployment
kubectl get service

### Start the application service
minikube service simple-app-service
To access the application, go to <EXTERNAL_IP>/<PORT> in the browser