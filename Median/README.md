# Median

```
cd python
docker build -t median:v1 .
cd ..
kubectl create deployment median --image=median:v1 --replicas=1
kubectl expose deployment median --port=5000 --type=LoadBalancer
kubectl port-forward svc/median 5000:5000&

cd html
docker build -t html:v1 .
cd ..
kubectl create deployment html --image=html:v1 --replicas=1
kubectl expose deployment html --port=80 --type=LoadBalancer
kubectl port-forward svc/html 8080:80&




```