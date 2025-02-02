
docker build -t app:v1 python/.
kubectl create deployment middle --image=app:v1 --replicas=1
kubectl expose deployment middle --port=5000 --type=LoadBalancer
kubectl port-forward svc/middle 5000:5000&

#kubectl get services
#kubectl delete service  <>


docker build -t html:v1 html/.
kubectl create deployment html --image=html --replicas=1
kubectl expose deployment html --port=80
kubectl port-forward svc/html 8080:80&

