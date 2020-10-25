# $ sudo apt-get install espeak
# $ pip install <package-name>

import pyttsx3
import PyPDF2

book = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init('espeak')

for num in range(0, pages):
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

print('done')
