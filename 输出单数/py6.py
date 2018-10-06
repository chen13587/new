#!/usr/bin/env python
a=0
sum=0
while a <100:
    a += 1

    if a%2==0:
        print (a)

        continue

    sum+=a
else:
    print (sum)
