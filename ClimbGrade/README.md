## Server
docker build -t climb:v1 .
kubectl create deployment server --image=climb:v1
kubectl expose deployment server --port=5000
kubectl port-forward svc/server 5000:5000 &


## Html
docker build -t html:v1 .
kubectl create deployment html --image=html:v1
kubectl expose deployment html --port=80
kubectl port-forward svc/html 8080:80 &

