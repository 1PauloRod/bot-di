Comandos Docker

-> docker pull mysql:latest br
-> docker build --tag docker-python .
-> docker run -d --name botdidb --rm -v botdiVolume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=discordia --network botdinet -p 3307:3306 mysql
-> docker run --name botdi --rm --network botdinet docker-python

DOCKER COMPOSE
-> docker-compose -f docker-compose.yml up --build


