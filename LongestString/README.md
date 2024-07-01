# LONGEST STRING
```
cd python
docker build -t longest:v1 .
kubectl create deployment longeststring --image=longeststring:v1 --replicas=1
kubectl expose deployment longeststring --port=5000 --type=LoadBalancer
kubectl port-forward svc/longeststring 5000:5000&


```