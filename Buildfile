docker rm -f flaskapp

docker build -t flaskapp .

docker run -d -p 8080:8080 -p 80:80 -p 5000:5000 --name flaskapp flaskapp