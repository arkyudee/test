import os

response1 = os.system("ping -c 1 8.8.8.8")
response2 = os.system("ping -c 1 8.8.8.4")
response3 = os.system("ping -c 1 192.168.1.1")
response4 = os.system("ping -c 1 192.168.1.2")


if response1 == 256:
    print("8.8.8.8: Unreacheable")
else:
    print("8.8.8.8: Reacheable")
if response2 == 256:
    print("8.8.8.4: Unreacheable")
else:
    print("8.8.8.4: Reacheable")
if response3 == 256:
    print("192.168.1.1: Unreacheable")
else:
    print("192.168.1.1: Reacheable")
if response4 == 256:
    print("192.168.1.2: Unreacheable")
else:
    print("192.168.1.2: Reacheable")
