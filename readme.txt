Very very basic flask-celery-redis example

# Run app
docker-compose build; docker-compose up -d

http://localhost:5000/<any_text_you_want>

# Cleanup
docker-compose down; docker rmi python_app_image; docker rmi redis