import os

f = open("adjectives.freaky")
w = open("adjectiveslist.freaky", "w")

things = f.read().split("\n")
otherthings = []

for i in things:
    otherthings.append('"' + i + '"')

w.write(str(things))