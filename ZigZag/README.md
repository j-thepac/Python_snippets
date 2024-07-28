# ZIGZAG

```
docker build -t zigzag:v1 .
kubectl create deployment zigzag --image=zigzag:v1 --replicas=1
kubectl expose deployment zigzag --port=5000 --type=loadBalancer
kubectl port-forward svc/zigzag 5000:5000&

docker build -t html:v1 .
kubectl create deployment html --image=html:v1 --replicas=1
kubectl expose deployment html --port=80 --type=LoadBalancer
kubectl port-forward svc/html 8080:80&



```
