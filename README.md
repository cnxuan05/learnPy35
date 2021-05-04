# learnPy35

```
 docker run --privileged --name orac  --restart always -d -p 8080:8080 -p 1521:1521 -v /opt/newdata/:/data/ -v /opt/newdata/data_temp/:/data/oracle_data/    -e oracle_allow_remote=true oracleinanutshell/oracle-xe-11g  /bin/bash /data/run.sh

docker pull wnameless/oracle-xe-11g
-e ORACLE_ALLOW_REMOTE=true

docker pull oracleinanutshell/oracle-xe-11g

 docker run -h "oraclehost" --name "oracle" -d -p 1521:1521 oracleinanutshell/oracle-xe-11g

docker run --privileged --name shop --restart always -d -p 8181:8181 -p 3222:22 -v /opt/newdata/:/data/ ubuntu:18.04  /bin/bash /data/run.sh



```
