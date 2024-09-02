```bash
docker compose up -d
```

```bash
docker exec -it hadoop-master /bin/bash
```

```bash
jps
```

```bash
docker exec -it hadoop-slave1 /bin/bash
```

```bash
jps
```

```bash
docker cp mapper.py hadoop-master:usr/local/hadoop/mapreduce/wordcount
docker cp reducer.py hadoop-master:usr/local/hadoop/mapreduce/wordcount
docker cp SalesJan2009.csv hadoop-master:usr/local/hadoop/mapreduce/wordcount/input
```

```bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -input /mapreduce/wordcount/input/SalesJan2009.csv \
    -output /mapreduce/wordcount/output \
    -mapper /usr/local/hadoop/mapreduce/wordcount/mapper.py \
    -reducer /usr/local/hadoop/mapreduce/wordcount/reducer.py \
    -file /usr/local/hadoop/mapreduce/wordcount/mapper.py \
    -file /usr/local/hadoop/mapreduce/wordcount/reducer.py
```
