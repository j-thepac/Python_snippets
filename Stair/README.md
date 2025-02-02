
docker build -t app:v1 python/.
kubectl create deployment app --image=app:v1 --replicas=1
kubectl expose deployment app --port=5000 --type=LoadBalancer
kubectl port-forward svc/app 5000:5000&



docker build -t html:v1 html/.
kubectl create deployment html --image=html:v1 --replicas=1
kubectl expose deployment html --port=80 --type=LoadBalancer
kubectl port-forward svc/html 8080:80&


kubectl get deployments
kubectl get services
kubectl delete services
kubectl delete deployment app html


