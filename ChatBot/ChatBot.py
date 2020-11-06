from aiml import Kernel

kernel = Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

while True:
    inputText = input(">Human: ")
    response = kernel.respond(inputText)
    print(">Bot: "+response)