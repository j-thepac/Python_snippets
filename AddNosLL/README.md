# Kubernetes Deployment in Containers

```
cd into python
docker build -t addnos:v1 .
kubectl create deployment addnos --image=addnos:v1 --replicas=1
kubectl expose deployment addnos --port=5000 --type=LoadBalancer
kubectl port-forward svc/addnos 5000:5000&
```


Html
```
cd into html
docker build -t html:v1 .
kubectl create deployment html --image=html:v1 --replicas=1
kubectl expose deployment html --port=80 --type=LoadBalancer
kubectl port-forward svc/html 8080:80&
```