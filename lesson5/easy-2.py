import os

dir = input("Input directory:")

for i in os.listdir(dir):
    print(i)