# Step by Step 
Nice to know for building web apps with python.   
(I'm writing this application to gset familiar with normal backend tasks)
## First Steps
1. initialize git  
* `git init .`
* set GitHub remote
2. creat virtual environment
* python3 -m venv env
* source env/bin/activate
* pip freeze > requirements.txt
* pip install -r requirements.txt
or use docker
* docker build -t btbirthday:latest .
* docker run -d -p 5000:5000 btbirthday
* docker logs -f <mycontainer>
* docker exec -it <mycontainer> bash

## Database
1. install flask-sqlalchemy


## History
1. install Flask
2. use Docker
3. use flask blueprints for routes
      