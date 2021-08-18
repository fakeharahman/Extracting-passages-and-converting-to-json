# Extracting-passages-and-converting-to-json

Here I have used python and regex to convert a text file (.txt) that contains passages, thier mcqs, month and year of publishing and the source. I have used regex to extract the text and converted it to json so that it can be dynamically rendered on a website.

## File structure
Comprehensions_ny.txt -> Comprehensions and mcqs for the new york Comprehensive English Regents Examinations. Link - https://www.nysedregents.org/ComprehensiveEnglish/. I have added symbols around different parts like the source, year, etc for easier extraction using regex.<br>
data.json-> contains the converted json<br>
txt.py-> Contains the code to convert from .txt to json
