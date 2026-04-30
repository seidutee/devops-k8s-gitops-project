# devops-k8s-gitops-project
Production-style Kubernetes DevOps platform featuring CI/CD pipelines, GitOps with Argo CD, and full observability using Prometheus and Grafana.

#to exec/ssh into a pod
fashion-store-deployment-94db7885b-l54sl

kubectl get pods
kubectl exec -it fashion-store-deployment-5796c77bcb-m8zz5 -- sh
kubectl exec -it fashion-store-deployment-5796c77bcb-m8zz5 -n apps -- sh

#Set a default namespace:
kubectl config set-context --current --namespace=apps 
Verify before exec
kubectl get pods -n apps
Then copy the exact pod name (they can change after redeploys).
#If sh fails
Some images don’t have sh, try:
kubectl exec -it <pod> -n apps -- /bin/bash

netstat -tlnp

kubectl logs -f <pod-name>



#to build an image
docker build -t docker:v2 . #don't forget the dot, it tells the system to access all content in folder
#run container
docker run -d -p 8080:80 --name fashion-store docker:v2 

kubectl port-forward svc/fashion-store-service -n apps  8080:80

kubectl port-forward svc/daycare-app-service -n apps  3000:80

to install argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
B9Qh3goDq5uwxNyB