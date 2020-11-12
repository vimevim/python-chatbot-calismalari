#https://blog.ekbana.com/the-easiest-way-to-create-a-chatbot-using-aiml-ec09b12dd2e1
#!/usr/bin/python3
import os
import aiml
BRAIN_FILE="brain.dump"
k = aiml.Kernel()
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    k.bootstrap(learnFiles="learningFileList.aiml", commands="LEARN AIML")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)
while True:
    input_text = input("USER > ")
    response = k.respond(input_text)
    print(response)
