#Library to read text
import pyttsx3
#Library to read/parse pdf files
import PyPDF2

#Open and read the pdf
book = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init('espeak')

#Iterate through each page and read aloud
for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

print('done')
