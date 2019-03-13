import os

BASE_PATH = "C:/Users/User/Desktop/"

ext = set()
for i in os.listdir(BASE_PATH):
    if os.path.isdir(os.path.join(BASE_PATH, i)):
        ext.add(os.path.splitext(i)[0])

for e in ext:
    if "." in e:
        for r in os.listdir(os.path.join(BASE_PATH,e)):
            os.rename(os.path.join(BASE_PATH, e, r), os.path.join(BASE_PATH,r))
        os.rmdir(os.path.join(BASE_PATH, e))

