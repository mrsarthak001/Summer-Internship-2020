## Assignment 1  
# Task 3 (Copying User Data)

For copying user data, first of all we need to create two users which can be created using adduser command
```\
adduser USER_NAME
```
![alt text](https://github.com/mrsarthak001/Summer-Internship-2020/blob/master/Assignment%201/Task3/Task3.1.PNG)

Further, we need to create user data in both the users, the users can be switched using, su command whereas the folder and file can be created with mkdir snd touch command respectively.
```\
su - USER_NAME)
mkdir DIRECTORY_NAME
touch FILE_NAME
```
![alt text](https://github.com/mrsarthak001/Summer-Internship-2020/blob/master/Assignment%201/Task3/Task3.2.PNG)

We need to change back our user to first user and copy files of second user using cp command
```\
cp -r /home/user2/DIRECTORY /home/user1/
```
![alt text](https://github.com/mrsarthak001/Summer-Internship-2020/blob/master/Assignment%201/Task3/Task3.3.PNG)
