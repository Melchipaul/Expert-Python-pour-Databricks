import os
# jabber = open(os.path.join(os.path.dirname(__file__), "Jabberwocky.txt"), "r", encoding="utf-8")
# poem = jabber.read()
# print(poem)
# jabber.close()

with open(os.path.join(os.path.dirname(__file__), "Jabberwocky.txt"), "r", encoding="utf-8") as jabber:
    poem = jabber.read()
    print(poem)