import sys

def checkArguments():
    if len(sys.argv) == 1:
        print("no argument given")
        return False
    return True

def checkPath():
    ...
    return True

def getImagePath():
    if not checkArguments():
        return False

    if not checkPath():
        return False

    image = sys.argv[1]
    return image
