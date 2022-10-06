from gtts import gTTS

myText = []
with open('sample.txt') as f:
    [myText.append(line) for line in f.readlines()]

print(myText)
Language = 'en'

newText = ' '
for t in myText:
    newText += ' '+t

print(newText)

myObj = gTTS(text=newText, lang=Language, slow=False)
myObj.save("t2s4rmfile.mp3")
