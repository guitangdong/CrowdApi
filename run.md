通过dockerfile构建镜像
docker build -t crowdapi .
运行docker
docker run -it --net=host --name crowdapi crowdapi
or
docker run -it -p 8000:8000 --name crowdapi crowdapi

docker exec -it crowdapi /bin/bash


docker port crowdapi 8000
docker network ls
docker network inspect host
