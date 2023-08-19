# Python_snippets
tInY cOdE sNiPpEtS



## Requirement : Add operation
### Folders and Files
 1. Add Folder
	 1. python
		 1. add.py ( GCP ) [TESTED - unit test]
		 2. server.py	[TESTED - Canary and Integration]
		 3. requirements.txt
		 4. dockerfile
		 5. **[templates for jinja ]
	 2. html
		 1. index.html
		 2. script.js
		 3. style.css
		 4. dockerfile
	 3. docker-compose.yml [TESTED]

### Sequence :

	 2011  cd html/
	 2011  docker build -t html:v1 .
	 2012  kubectl create deployment html --image=html:v1
	 2013  kubectl expose deployment html --port=80
	 2014  kubectl port-forward svc/html 8080:80 &

	 2018  cd python/
	 2019  docker build -t subset:v1 .
	 2020  kubectl create deployment subset --image=subset:v1
	 2021  kubectl expose deployment subset --port=5000
	 2023  kubectl port-forward svc/subset 5000:5000 &
	 2024  fg
	 2025  jobs
	 2026  kill %1
	 2027  jobs
	 2028  bg
	 2029  kill %2
	 2030  kubectl get services
	 2031  kubectl delete service html subset
	 2032  kubectl delete deployment html service
	 2033  kubectl delete deployment html subset
	 2034  docker images
	 2035  docker rmi 0005b47407bd 40b93f1a0778
	 2036  docker system prune


