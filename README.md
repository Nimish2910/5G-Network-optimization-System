

__CSCI5253/ECEN 5033: Datacenter Scale Computing Final Project  Team 45__

__Title: 5G Network Optimization System__

__Participants: Darsh Thakkar and Nimish Sabnis__

This repository contains all necessary files and resources for the final project. The project includes a Web UI, Kubernetes Helm Charts, MongoDB configurations, and supporting scripts. Follow the instructions below to set up the environment.


__Demonstration Video__

Link: https://drive.google.com/drive/folders/1m2XJOouI6xhBuIfY9w1dLXf-tDZBNKT3?usp=sharing

__Prerequisites__
*	Tested on: Ubuntu 20.04 using Multipass on MacOS
*	Minimum system requirements: 8 CPUs and 16GB RAM
*	Will also work on GCP if used with above configuration
  
__Installation Steps__

1. Install Docker

You can install Docker Engine by following the official Docker installation guide: https://docs.docker.com/engine/install/ubuntu/
	•	After installation, test Docker using:
```bash
docker ps
```

This command lists the running Docker containers.

•	If you encounter the following error:

permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock

Resolve it by running:

 ```bash
 sudo usermod -aG docker $USER 
 newgrp docker
 ```
These steps grant the current user access to the Docker daemon socket at /var/run/docker.sock.

2. Install Helm

Helm is a package manager for Kubernetes. Follow these steps to install Helm:
•	Download and install Helm by running:

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```
or use https://helm.sh/docs/intro/install/



•	Verify the installation:
```bash
helm version
```
3. Install Minikube

Minikube sets up a local Kubernetes cluster for development. To install Minikube:
•	Download the Minikube binary:
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

•	Move the binary to /usr/local/bin:

```bash
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

•	Verify the installation:
```bash
minikube version
```

•	Start Minikube:

```bash
minikube start --driver=docker
```

4. Deploy Project Components

a. Deploy MongoDB
•	Install MongoDB using Helm:
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install mongodb bitnami/mongodb
```

•	Verify MongoDB deployment:
```bash
kubectl get pods
```
b. Get Multus Cni:


Clone this GitHub repository
```bash
git clone https://github.com/k8snetworkplumbingwg/multus-cni.git
```
Apply a daemonset which installs Multus using kubectl. From the root directory of the clone, apply the daemonset YAML file:

```bash
cat ./deployments/multus-daemonset-thick.yml | kubectl apply -f -
```

c. Deploy the 5G Core
```bash
helm install open5gs ./charts/open5gs --values ./charts/open5gs/5gSA-values.yaml
```

d. Deploy UERANSIM:
```bash
helm install ueransim-gnb ./charts/ueransim-gnb --values ./charts/ueransim-gnb/gnb-ues-values.yaml
```

e. Access the Web UI:

•	Expose the Web UI using a NodePort service:
```bash
kubectl expose deployment webui --type=NodePort --name=webui-service
```

•	Get the external IP and port:
```bash
kubectl get svc webui-service
```

Access the UI using the external IP and assigned port.  

or directly run by going in webUI directory.


Folder Structure
*	WebUI: Contains the frontend code for the user interface.
*	Charts: Kubernetes Helm charts for deploying the application.
*	MongoDB: Database configurations and scripts.
*	Scripts: Utility scripts for managing the deployment.
*	README: Project documentation.

__References__:
* https://docs.srsran.com/projects/4g/en/hoverxref_test/app_notes/source/zeromq/source/index.html
* https://5g.systemsapproach.org/
* https://open5gs.org/open5gs/docs/guide/01-quickstart/



