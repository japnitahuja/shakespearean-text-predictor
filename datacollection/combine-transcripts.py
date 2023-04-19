import os
from TextPreprocessor import TextPreprocessor

allcontent = ""
preprocessor = TextPreprocessor()
path = "C:/Users/lenovo/Desktop/GithubRepos/text-prediction/scenes"
for dirPath, dirNames, fileNames in os.walk(path):
    for fileName in fileNames:
        file = open(path + "/" + fileName, 'r')
        content = ""
        for line in file:

            content += line

        content = preprocessor(content)
        allcontent += content + "\n"

with open('monoromeo.txt', 'w') as f:
    f.write(allcontent)
