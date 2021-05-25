import PyPDF2
from pdfreader import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer


pdfFileObj = open('input.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

no_of_pages = pdfReader.numPages
print('Number of Pages:',no_of_pages)


# def parse_obj(objs):
#     for obj in objs:
#         if isinstance(obj, pdfminer.layout.LTTextBox):
#             for o in obj._objs:
#                 if isinstance(o,pdfminer.layout.LTTextLine):
#                     text=o.get_text()
#                     if text.strip():
#                         for c in  o._objs:
#                             if isinstance(c, pdfminer.layout.LTChar):
#                                 print ("fontname %s"%c.fontname)
#         # if it's a container, recurse
#         elif isinstance(obj, pdfminer.layout.LTFigure):
#             parse_obj(obj._objs)
#         else:
#             pass



for i in range(no_of_pages):
    pageObj = pdfReader.getPage(i)
    print('FONTS:', pageObj.Resources.Font)
    print('pageObj:', pageObj)
    text = pageObj.extractText()
    print('TEXT:',text)


