Comandos Docker

-> docker pull mysql:latest <br>
-> docker build --tag docker-python <br>
-> docker run -d --name botdidb --rm -v botdiVolume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=discordia --network botdinet -p 3307:3306 mysql<br>
-> docker run --name botdi --rm --network botdinet docker-python<br>

DOCKER COMPOSE<br>
-> docker-compose -f docker-compose.yml up --build


