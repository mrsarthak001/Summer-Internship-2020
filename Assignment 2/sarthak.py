
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
