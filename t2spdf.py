# importing required modules
from gtts import gTTS
import PyPDF2


def extract_text(fname, pagenum, mode='rb'):
    with open(fname, mode) as fp:
        reader = PyPDF2.PdfFileReader(fp)
        page = reader.getPage(pagenum)  # 0
        return page.extractText()


def get_meta(path):
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        info = pdf.getDocumentInfo()
        nop = pdf.getNumPages()
    print(info)
    print(nop)


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    # print(txt)
    return information, number_of_pages

# info, pages = extract_information(
#     'Practical Docker with Python_ Build, Release and Distribute Your Python App with Docker.pdf')
# print(pages)


myText = ' '
Language = 'en'
startPage = 14
endPage = 18

for p in range(startPage, endPage+1):
    pageText = extract_text(
        'Practical Docker with Python_ Build, Release and Distribute Your Python App with Docker.pdf', p)
    # print(pageText)
    myText += pageText

# print(myText)
myObj = gTTS(text=myText, lang=Language, slow=False)
myObj.save("t2spdf.mp3")
