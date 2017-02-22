#!/usr/bin/python
# Find mango sellers in your (Facebook) network
from collections import deque

graph           = {}
graph["you"]    = ["alice", "bob", "claire"]
graph["bob"]    = ["anuj", "peggy"]
graph["alice"]  = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"]   = []
graph["peggy"]  = []
graph["thom"]   = []
graph["jonny"]  = []

def is_mango_seller(person):
    # NOTE: modify this to play with the program results
    if person == "anuj":
        return True
    else:
        return False

# Keep a queue of people to check
queue   = deque()
queue  += graph["you"]
checked = [] # prevent double checking or infinite loops

while queue:
    # Pop (dequeue) a persone of the queue
    person = queue.popleft()

    # Only check the person if you haven't checked them before
    if not person in checked:

        print "debug: checking " + person

        # Check if this person is a mango seller ...
        if is_mango_seller(person):
            # ... yes: you are done
            print person + " is a mango seller"
            exit()
        else:
            # ... no: add all their neighbors to the queue
            queue += graph[person]
            checked.append(person)

print "there are no mango sellers in you network"
