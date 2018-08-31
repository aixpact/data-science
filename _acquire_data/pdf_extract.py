# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('sample.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()

# ---------------------------------------------> tika works well <-------------------------------------------- #
# https://github.com/chrismattmann/tika-python

from tika import parser
raw = parser.from_file('sample.pdf')
print(raw["metadata"])
print(raw['content'])

#!/usr/bin/env python
from tika import language, translate, unpack
# print(language.from_file('sample.pdf'))
print(translate.from_file('sample.pdf', 'es', 'en'))
raw
# print(raw['content'].translate)
# !tika.py translate en:fr sample.pdf

parsed = unpack.from_file('sample.pdf')



# ---------------------------------------------> xpdf-python <-------------------------------------------- #
#
# does not work
from xpdf_python import to_text
import xpdf_python

pdf_location = 'sample.pdf'
text = to_text(pdf_location)

# ---------------------------------------------> pytesseract <-------------------------------------------- #

# https://pypi.python.org/pypi/pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

# brew upgrade
# brew doctor
# brew install tesseract
# pip3 install pytesseract
# change pytesseract.py file:
# CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
# tesseract_cmd = 'tesseract' =>
# tesseract_cmd = '/usr/local/bin/tesseract'

# pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('sample.png')))

# ---------------------------------------------> tesserocr <-------------------------------------------- #

# import tesserocr
# from PIL import Image
#
# print(tesserocr.tesseract_version())  # print tesseract-ocr version
# print(tesserocr.get_languages())  # prints tessdata path and list of available languages
#
# image = Image.open('sample.jpg')
# print(tesserocr.image_to_text(image))  # print ocr text from image
# # or
# print(tesserocr.file_to_text('sample.jpg'))

# ---------------------------------------------> googletrans <-------------------------------------------- #

from googletrans import Translator

# Redelijk goede vertaling
txt = 'why is this a good translator at all'
txt2 = 'why do I give a shit anyway'

translator = Translator()
print(translator.translate('안녕하세요.'))
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
translator.translate('안녕하세요.', dest='ja')
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
translator.translate('veritas lux mea', src='la')
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
print(translator.translate(txt2, dest='nl', src='en'))
print(translator.translate(txt, dest='la', src='en'))

# ---------------------------------------------> translate <-------------------------------------------- #

# Slechte vertaling!
from translate import Translator
chinese = Translator(to_lang="zh")
dutch = Translator(to_lang="nl")
txt = 'why is this a good translator'
chinese.translate(txt)
dutch.translate(txt)

# --------------------------------------------->  <-------------------------------------------- #