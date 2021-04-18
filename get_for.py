'''
export https_proxy=https://192.168.1.57:1080
export http_proxy=http://192.168.1.57:1080

git config --global http.proxy http://192.168.1.57:1080
git config --global https.proxy https://192.168.1.57:1080
git config --global --unset http.proxy
git config --global --unset https.proxy

cd /home/newdata

mkdir -p /usr/local/oracle/data_temp  && chmod 777 /usr/local/oracle/data_temp


docker run --privileged --restart always -d -p 8080:8080 -p 1521:1521 -v /home/newdata/:/data/ -v /home/newdata/data_temp/:/home/oracle/data_temp/  --name orac truevoly/oracle-12c /bin/bash /data/run.sh
docker pull docker.io/truevoly/oracle-12c

cd /


sqlplus system/oracle@//localhost:1521/xe





'''





