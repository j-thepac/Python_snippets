
docker build -t buyshare:v1 python/.
kubectl create deployment buyshare --image=buyshare:v1 --replicas=1
kubectl expose deployment buyshare --ports=5000 --type=LoadBalancer
kubectl port-forward svc/buyshare 5000:5000&


docker build -t html:v1 html/.
kubectl create deployment html --image=html:v1 --replicas=1
kubectl expose deployment html --ports=80 --type=LoadBalancer
kubectl port-forward svc/html 8080:80&