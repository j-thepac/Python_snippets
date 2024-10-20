docker build -t revint:v1 .
kubectl create deployment revint --image=revint:v1 --replicas=1
kubectl expose deployment revint --port=5000 --type=LoadBalancer 
kubectl port-forward svc/revint 5000:5000 &



docker build -t html:v1 .
kubectl create deployment html --image=html:v1 --replicas=1
kubectl expose deployment html --port=80 --type=LoadBalancer 
kubectl port-forward svc/html 8080:80 &