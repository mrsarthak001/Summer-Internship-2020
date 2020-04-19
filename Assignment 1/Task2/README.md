## Assignment 1  
# Task 2 (Creating user with date persission)

We need to create a user having permission of date command only and no other permission. Also, other users should not be able to access date command.

First of all, we need to remove execution permission from all the users, including root, it can be done with the help of

chmod a-x /bin/date

Then, further we need to add a user with shell permission of date
```\
useradd -s FILE_TO_EXECUTE USER_NAME
useradd -s /bin/date s1
```
Also, as we have removed the execute perission from all the users so we need to add the same for the specified user.

```\
setfacl -m u:USER_NAME:rwx FILE_TO_EXECUTE
setfacl -m u:s1:rwx /bin/date
```

![alt text](https://github.com/mrsarthak001/Summer-Internship-2020/blob/master/Assignment%201/Task2/Task2.PNG)
