"""
Assignment 4 Tristan Torgersen
"""
import os
import re

# Get filenames
os.chdir("/Users/tristan/Downloads/Mini-CORE_new/")
filenames = [f for f in os.listdir() if re.search(r"\.txt", f, flags=re.IGNORECASE)]
# Open connection to outfile
# outfile = open("outfile.csv", "w")
with open('outfile.csv', 'w', encoding='utf-8') as outfile:
    outfile.write("Register,Modal Verbs,Exclamation Points,1st Person Pronouns\n")
    # Loop over 8 registers
    registers = ["HI", "ID", "IN", "IP", "LY", "NA", "OP", "SP"]
    for register in registers:
# Create counters for the total words and linguistic features
            count_total_wds = 0
            count_modal_verbs = 0
            count_exclamation = 0
            count_1st_pron = 0
# Loop over 1600 files
            for filename in filenames:
# If the current file belongs to the current register
                if filename[2:4] == register:
                    with open(filename, encoding="cp437") as txt:
                        file_as_string = txt.read()
# Disregard the header
                        file_as_string = re.sub(r"<.*?>", "", file_as_string)
# Split it into words
                        wds_in_file = len(file_as_string.split())
# Add number of words in current file to total number of words counter
                        count_total_wds = count_total_wds + wds_in_file
# Add number of linguistic features to their counters
                        modal_in_file = (len(re.findall(r"\bcan\b|\bmight\b|\bmust\b|\b[sh|w|c]ould\b|\bwill\b", file_as_string, flags=re.IGNORECASE)))
                        exclamation_in_file = (len(re.findall(r"!+", file_as_string, flags=re.IGNORECASE)))
                        pron_in_file = (len(re.findall(r"\bI\b|\bwe\b|\bme\b|\bus\b|\bmine\b|\bours\b|\bmyself\b|\bourselves\b|\bmy\b|\bour\b", file_as_string, flags=re.IGNORECASE)))
                        count_modal_verbs = count_modal_verbs + modal_in_file
                        count_exclamation = count_exclamation + exclamation_in_file
                        count_1st_pron = count_1st_pron + pron_in_file
# Normalize counts of the linguistic features to 1000
            count1 = round((count_modal_verbs/count_total_wds) * 1000, 1)
            count2 = round((count_exclamation/count_total_wds) * 1000, 1)
            count3 = round((count_1st_pron/count_total_wds) * 1000, 1)
# Write out normalized counts to csv file
            outfile.write(f"{register},{count1},{count2},{count3}\n")