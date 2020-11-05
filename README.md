# cloud-hw3
## installation
> git clone https://github.com/big-data-europe/docker-hadoop.git<br>
> cp Dockerfile docker-hadoop/namenode/Dockerfile<br>

## run hadoop
> cd docker-hadoop<br>
> docker-compose up<br>

## find hadoop streaming jar
> find / -name \*streaming\*.jar<br>
> stream="path to hadoop streaming jar"

## run task
> docker cp ./mapper.py namenode:/home/<br>
> docker cp ./reducer.py namenode:/home/<br>
> docker cp ./access_log.txt namenode:/home/<br>
> docker exec -it namenode /bin/bash<br>
> hadoop fs -mkdir /poodah<br>
> hadoop fs -mkdir /poodah/in<br>
> hdfs dfs -put access_log.txt /poodah/in<br>
> hadoop jar $stream -file mapper.py -mapper mapper.py --file reducer.py -reducer reducer.py -input /poodah/in -output /poodah/out<br>
> hdfs dfs -get /poodah/out/ ./