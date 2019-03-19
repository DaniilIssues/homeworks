def make_dict(key, value):
    dict_ = {key: value}
    return dict_

a = make_dict(input("Key input:"), input("Value input:"))

def make_file(dict_):
    for i in dict_.keys():
        a = open(f"{i}.txt", "w+")
        for i in dict_.values():
            for j in i.split(","):
                a.write(j)
                a.write("\n")
        a.close()

b = make_file(a)
