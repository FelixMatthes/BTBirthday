# Step by Step 
Nice to know for building web apps with python.   
(I'm writing this application to get familiar with normal backend tasks)
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
1. install flask-sqlalchemy, SQLAlchemy
2. init DB with:
```
from yourapp import db, create_app 
db.create_all(app=create_app())
```



## History
1. install Flask
2. use Docker
3. use flask blueprints for routes
4. use a app factory for creating the the flask app

      