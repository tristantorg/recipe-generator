"""
Assignment 5 Tristan Torgersen
"""
import os
import re

# Get filenames
os.chdir("/Users/tristan/Downloads/Mini-CORE_new/")
filenames = [f for f in os.listdir() if re.search(r"\.txt", f, flags=re.IGNORECASE)]
# Loop over 8 registers
registers = ["HI", "ID", "IN", "IP", "LY", "NA", "OP", "SP"]
for register in registers:
    # Open connection to outfile
    with open("%s_results.csv" % register, 'w', encoding='utf-8') as out_file:
        # Create empty dictionary
        word_freq = dict()
        # Loop over 1600 files
        for filename in filenames:
         # If current file belongs to current register
            if filename[2:4] == register:
                with open(filename, encoding="cp437") as txt:
                    file_as_string = txt.read()
                    # Disregard the header
                    file_as_string = re.sub(r"<.*?>", "", file_as_string)
                    file_as_string = re.sub(r"[?,!.-]", "", file_as_string)
                    # Split into words and make all lower case
                    file_as_string = file_as_string.lower()
                    wds_in_file = file_as_string.split()
        #Loop over words to remove stopwords and populate dictionary
                    stopwords = ['i', 'me', 'THE', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
                    wds_to_keep = [word for word in wds_in_file if word not in stopwords]
                    for word in wds_to_keep:
                        if word not in word_freq:
                            word_freq[word] = 1
                        else:
                            word_freq[word] = word_freq[word] + 1
        # Sort words in descending order
        word_list = list(word_freq.items())
        sorted_list = sorted(word_list, key=lambda x: x[1], reverse=True)
        # Write results to outfile
        out_file.write("Word,Frequency\n")
        for k, v in sorted_list:
            out_file.write(f"{k},{v}\n")