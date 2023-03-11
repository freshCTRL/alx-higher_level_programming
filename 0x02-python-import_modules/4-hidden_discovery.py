#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    names = dir(hidden_4)
    names = list(names)
    names = names.sort()

    for i in names:
        if i[:2] != "__":
            print(i)
        else:
            continue
