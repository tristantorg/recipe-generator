"""
Assignment 3 Tristan Torgersen
"""
import re
import os

# Accessing the directory where the files are stored and the creating a for loop between the two files
os.chdir("/Users/tristan/Downloads/ling_360_assgn_3/")
filenames = [f for f in os.listdir() if re.search(r"\.txt", f, flags=re.IGNORECASE)]

# For loop for the txt files in the directory
for filename in filenames:
   with open(filename, encoding="utf8") as infile:
      txt_as_string = infile.read()  # Opening up the file and reading it in order to prep for the regex findall in the next step
      # Creating the regexes as variables for the next for loop
      regex_subj_pro = r"\bI\b|\byou\b|\bs?he\b|\bthey\b|\bwe\b|\bit\b"                             # Subject Pronouns
      regex_cntrct = r"\w+n['’]t|\w+['’]d|\w+['’]ll|\w+['’]ve|\w+['’]re|\w+['’]m|\w+['’]s"   # Contractions
      regex_modal_vb = r"\bcan\b|\bmight\b|\bmust\b|\b[sh|w|c]ould\b|\bwill\b"               # Modal Verbs
      regexes = [regex_subj_pro, regex_cntrct, regex_modal_vb]
      for regex in regexes:
         results = re.findall(regex, txt_as_string, flags=re.IGNORECASE) # Using the regex variables to search through the texts to find the results
         n_results = len(results) # Counting the instances
         print(results)
         print(n_results)
