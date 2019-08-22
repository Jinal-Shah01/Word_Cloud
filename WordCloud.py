"""

@author Jinal Shah

1. Create a word cloud from a given text in python(use existing modules)

"""
import wordcloud

text = ''
height = int(input('Height of wordcloud: '))
width = int(input("Width of wordcloud: "))

cloud = wordcloud.WordCloud(height=height,width=width)
res = input("Do you have a file with all your text?(Yes/No): ")

if res == 'No':
    words = []

    response = 'Yes'
    word = input("First Word: ")

    while response == 'Yes':
        words.append(word)
        word = input("Next Word: ")
        response = input("Would you like to add another word?(Yes/No) ")

    for x in words:
        text += x + " "

    cloud.generate_from_text(text=text)

    cloud.to_file('wordcloud.png')

else:
    fileName = input("Enter the filename: ")
    file = open(file=fileName,mode='r')

    for x in file.readlines():
        text += x + " "

    cloud.generate_from_text(text=text)

    cloud.to_file('wordcloud.png')