import os

for i in range(1, 10):
    if os.path.exists("dir_"+str(i)):
        continue
    else:
        os.mkdir("dir_"+str(i))

for i in range(1, 10):
    if os.path.exists("dir_"+str(i)):
        os.rmdir("dir_"+str(i))
    else:
        continue
