from pdf2docx import Converter
from tkinter import filedialog as fd, simpledialog

pdf_file = fd.askopenfilename()
name = simpledialog.askstring(title="XLSX", prompt="Qual nome salvar o arquivo? ")
pasta = fd.askdirectory()
docx_file = pasta + '/' +name +'.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()