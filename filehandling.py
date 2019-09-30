from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from CStringIO import StringIO

def readpdf(mypdf):
  rsrcmgr = PDFResourceManager()
  sio = StringIO()
  codec = 'utf-8'
  laparms = LAParams()
  device = TextConverter(rsrcmgr,sio,codec = codec, laparms)