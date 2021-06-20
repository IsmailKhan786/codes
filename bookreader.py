import pyttsx3
import PyPDF2
book = open('richdadpoordad.pdf','rb')
#call pdf read func
pdfReader = PyPDF2.PdfFileReader(book)
#to know pages
pages = pdfReader.numPages
print(pages)
speak = pyttsx3.init()
page = pdfReader.getPage(30)
text = page.extractText()
speak.say(text)
#speak.say('hello al')
speak.runAndWait()

#now we will get pdf file and read
#download any pdf onine
#to read pdf we need to intsall another package
#PyPDF2
#now book create
#to start reading from any page we do
#page = pdfReader.getpage
#inmdex starte with b0 if page is 8 we do 7