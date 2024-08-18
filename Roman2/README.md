
docker build -t roman:v1 .
kubectl create deployment roman --image=roman:v1 --replicas=1
kubectl expose deployment roman --port=5000 --type=LoadBalancer
kubectl port-forward svc/roman 5000:5000 &


docker build -t html:v1 .
kubectl create deployment html --image=html:v1 --replicas=1
kubectl expose deployment html --port=80 --type=LoadBalancer
kubectl port-forward svc/html 8080:80 &