# Assignment 2

## Task 1 (Creating 100 Containers using Python)

```
import os

for num in range(1,101):
	if num<=25:
		os.system("docker run -itd --restart unless-stopped --name adhocnw{} alpine".format(num))
	elif num<=50:
		os.system("docker run -itd --restart unless-stopped --name adhocnw{} fedora".format(num))
	elif num<=75:
		os.system("docker run -itd --restart unless-stopped --name adhocnw{} centos".format(num))
	elif num<=100:
		os.system("docker run -itd --restart unless-stopped --name adhocnw{} java".format(num))
os.system("docker ps")
```

## Task 2 (Storing Container Name and Date Created in a File)
```
docker ps -a --format "table {{.Names}}\t{{.Created}}" > container_list.txt
```

## Task 3 (Container with firefox as parent process)
Dockerfile
```
FROM ubuntu
RUN sudo apt install firefox -y
CMD ["/usr/bin/firefox"]
```
Further, we can need to build the Dockerfile with build command
```
docker build -t firefox .
```

## Task 4 (Storing Memory and CPU usage of container in a file)
```
docker stats --all --no-repeat --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}" > file.txt
```
