from random import randint

def __main__():
    files = ["first", "last"]
    names = ["",""]
    for i in [0,1]:
        names[i] = pick_one(file_to_list(files[i]))
    print(names[0], names[1])

def pick_one(arr):
    n = len(arr) - 1
    return arr[randint(0,n)]

def file_to_list(filename):
    f = open(filename)
    r = list(map(lambda s: s[:-1], f))
    f.close()
    return r

__main__()
