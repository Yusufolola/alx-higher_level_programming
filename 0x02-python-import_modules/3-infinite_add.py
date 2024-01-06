#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = len(sys.argv)
add = 0

if ((argv) == 1):
    print("0")
elif ((argv) > 1):
    for i in range(1, argv):
        add += int(sys.argv[i])
    print(add)
