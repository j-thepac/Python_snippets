

'''
cd 
docker build -t longeststr:v1 .
docker run -d -p 8000:8000 longeststr:v1


kubectl create deployment longeststr --image=longeststr:v1 --replicas=1
kubectl expose deployment longeststr --port=8000 --type=LoadBalancer
kubectl port-forward svc/longeststr 8000:8000&


kubectl delete service longeststr
kubectl delete deployment longeststr
'''