''''

ssh root@192.168.1.22 "cd /opt/data/04/; fast-archive -c data --exclude=data/\*.pid" | fast-archiver -x
ssh root@192.168.1.26 "cd /opt/data/04/; fast-archive -c data --exclude=data/\*.pid" | fast-archiver -x

tar -cf - /opt/data/04 | ssh root@192.168.1.26 'tar -xvf - -C /opt/'



stack overflow
- K

heap G








'''