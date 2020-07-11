import os
from os.path import isfile, join


def searchfile(filePath, fileName):

    print("Checking", filePath)
    if fileName in filePath:
        print("Found it")
        return True

    if isfile(filePath):

        return False

    for file in os.listdir(filePath):

        found = searchfile(join(filePath, file), fileName)

        if found:
            return True

    return False


print(searchfile("/Users/aushakanuz/Desktop", "1839622.jpg"))

