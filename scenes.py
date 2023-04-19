import os
from TextPreprocessor import TextPreprocessor
import re

allmonologues = ""
preprocessor = TextPreprocessor()
path = "C:/Users/lenovo/Desktop/GithubRepos/shakespearean-bot/scenes"

# Go through all the scene files
for dirPath, dirNames, fileNames in os.walk(path):
    for fileName in fileNames:
        file = open(path + "/" + fileName, 'r')
        # add up each separate monologue here
        mono = ""
        for line in file:
            # If it matches Name. format then its a new dialogue
            if (re.search("^[a-zA-Z]+\s?[a-zA-Z]*[.]{1}.+", line)):
                # add previous monologue to all monologues
                if mono:
                    # preprocess the monologue
                    mono = preprocessor(mono)
                    allmonologues += mono + "\n"
                # start collecting the new monologue
                line = line.strip("\n")
                line = line.split(".")[1]
                mono = line
            # if continuation of the same monologue
            else:
                line = line.strip("\n")
                mono += " "+line
with open('allmonologues.txt', 'w') as f:
    f.write(allmonologues)
