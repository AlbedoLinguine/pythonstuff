# comment

inputty = input("hello world? ")
error = False #bool

def HelloWorld():
    global inputty
    if (inputty == "yes"):
        print("hello world")
        error = False
    elif (inputty == "no"):
        print("bye world")
        error = False
    else:
        inputty = input("hello world? ")
        error = True
        HelloWorld()

#actual stuff

HelloWorld()