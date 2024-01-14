# CIDR-Sort
A Toolkit for better CIDR sorting, Works with IP addresses and CIDR blocks


Sorts CIDR or IP Adresses as is if the preceding 0's where not trimmed, but returns the values as originaly given.

Time comparrision for 1k runs on a set of 309 address


```
Time taken for fancy sort function : 0.733680009841919 seconds 
proccessed 309 addresses 1000 times
Time taken for basic sort function: 0.03343319892883301 seconds
proccessed 309 addresses 1000 times
```

Example input output:

``` 
my unsorted list is: ['192.168.0.1', '10.45.67.45', '10.66.66.0/24', '10.200.200.3', '172.16.0.0/16', '172.32.254.0/24', '172.18.248.36', '192.168.0.0/24', '192.168.10.15', '192.168.10.0/23', '10.0.1.0/24', '10.0.0.0/8', '10.255.255.0/24']

my sorted list is: [10.0.0.0/8, 10.0.1.0/24, 10.45.67.45, 10.66.66.0/24, 10.200.200.3, 10.255.255.0/24, 172.16.0.0/16, 172.18.248.36, 172.32.254.0/24, 192.168.0.0/24, 192.168.0.1, 192.168.10.0/23, 192.168.10.15]
```

import sort_list from cidr_sort.py and feed it any list of IP addresses or CIDR blocks as strings and it will return a list of those same strings sorted.

Dependencies: None