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