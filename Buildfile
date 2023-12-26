# Build the Flask application image
docker build -t acobley/flaskapp .

# Tag the image for pushing to a registry
docker tag acobley/flaskapp acobley/flaskapp

# Push the image to Docker Hub
docker push acobley/flaskapp

# Stop and remove the existing Flask and MySQL containers if they exist
docker stop flaskapp || true
docker rm flaskapp || true
docker stop some-mysql || true
docker rm some-mysql || true

# Start MySQL container
docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=dacjd156n. -d mysql:8.0

# Start Flask application container, linking it to the MySQL container
docker run -p 80:5000 -d --name flaskapp --link some-mysql:some-mysql acobley/flaskapp
