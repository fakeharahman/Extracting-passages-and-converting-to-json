# import pdfminer 
import re
from pdfminer.high_level import extract_text
# print(pdfminer.__version__) 
text = extract_text('English test ny.pdf')
# print(repr(text))
# print(text)
print(type(text))
print(type("hjd"))
p1=re.findall(r'[0-9] ([\s\S]*?)\(', str(text))

# print(p1)
for i in p1:
    print(i)
dpath="English test ny.pdf"

# import pyPdf  
# def get_pdf_content(pdf_file_path):
#     with open(pdf_file_path) as f:
#         pdf_reader = PdfFileReader(f)
#         content = "\n".join(page.extractText().strip() for page in pdf_reader.pages)
#         content = ' '.join(content.split())
#         return content


# print(get_pdf_content('/path/to/file.pdf'))

# # test=re.search(k)
# test=open('test.txt')
# print(test)

# for line in test:
#     line=line.rstrip()
#     # if line.startswith("Reading Comprehension Passage A"):
#     if re.search('Reading Comprehension Passage A', line):
#         print(line)