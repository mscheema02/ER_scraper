import pandas as pdLib
import xdrlib as xLib
import numpy as numLib
import seaborn as sbLib
import selenium as smLib
import chromedriver_binary as cdLib
import PyPDF2
import re

class mainScrape:

    def __init__ (self, fileName):
        self.pdf_file = open(fileName, "rb")
        self.pdf_reader = PyPDF2.PdfFileReader(self.pdf_file)
    
    def extract_Text(self):
        text = ""
        for i in range (self.pdf_reader.getNumPages()):
            page = self.pdf_reader.getPage(i)
            text += page.extractText()
        return text

    def search_Pattern(self, pattern):
        text = self.extract_Text()
        return re.findall(pattern, text)

    def fclose(self):
        self.pdf_file.close()

#Static void main args
scrapeObj = mainScrape('C:/Projs/project_Scrape_ER//20220427_alphabet_10Q.pdf')

# Search for dates in the format YYYY-MM-DD
dates = scrapeObj.search_Pattern(r'\d{4}')

print(dates)
scrapeObj.fclose()



