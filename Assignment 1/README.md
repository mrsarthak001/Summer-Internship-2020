# Assignment 1

First Assignment of Summer Internship

## Task 1

Creating Directory Structure
```\
mkdir -p A/{B/{D/{I/M/Z,J/L/Z},E/H/L/Z},C/{F/H/L/Z,G/K/L/Z}}
tree A
```
[ClICK FOR MORE INFO](https://github.com/mrsarthak001/Summer-Internship-2020/tree/master/Assignment%201/Task1)

## Task 2 
Creating user with date persission
```\
sudo -i
date
which date
chmod a-x /bin/date
ls -al /bin/date
date
exit
whoami
date
sudo su
useradd -s /bin/date s1
su - k1
setfacl -m u:s1:rwx /bin/date
su - k1
chmod a-x /bin/date
```
[ClICK FOR MORE INFO](https://github.com/mrsarthak001/Summer-Internship-2020/tree/master/Assignment%201/Task2)

## Task 3 
Copying User Data

```\
sudo su
adduser user1
adduser user2
su - user1
ls
mkdir adhoc1
cd adhoc1
touch adhoc1.txt
exit
su - user2
ls
mkdir adhoc2
cd adhoc2
touch adhoc2.txt
exit
su - user1
ls
cp -r /home/user_2/DIRECTORY /home/user_1/
ls
```
[ClICK FOR MORE INFO](https://github.com/mrsarthak001/Summer-Internship-2020/tree/master/Assignment%201/Task3)

## Task 4 

Running cal command for 10sec and storing in text file

```\
#/bin/bash

a=$( date +%S )

if [ $a -lt 50 ];
then
    range=10
    limit=$(( a + range ))
else
    range=-50
    limit=$(( a + range ))
fi

while [ $a -ne $limit ]
do
    a=$( date +%S )
    cal>>/tmp/a.txt
done
```
[ClICK FOR MORE INFO](https://github.com/mrsarthak001/Summer-Internship-2020/tree/master/Assignment%201/Task4)
