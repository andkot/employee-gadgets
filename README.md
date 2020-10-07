# employee-gadgets
Application with the ability to issue technical equipment to an employee
# Run app on docker:
linux comands:
1. sudo docker build .
2. sudo docker-compose build
3. sudo docker-compose exec web python src/manage.py makemigrations --noinput
4. sudo docker-compose exec web python src/manage.py migrate --noinput
5. sudo docker-compose up -d --buildt

