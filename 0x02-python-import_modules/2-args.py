#!/usr/bin/python3
if __name__=="__main__":
    import sys

if (len(sys.argv) == 1):
    print("0 arguments .")
elif (len(sys.argv) > 1):
     if (len(sys.argv) == 2):
         print(f"{len(sys.argv) - 1} argument:")
         print(f"{len(sys.argv) - 1}: {sys.argv[1]}")

     else:
         print(f"{len(sys.argv) - 1} arguments")
         for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")

            


