"""
Assignment 7 Tristan Torgersen
"""
import nltk, os, re

# Get filenames
os.chdir("/Users/tristan/Downloads/AWE_untagd/")
filenames = [i for i in os.listdir() if re.search(r"\.txt$", i, flags=re.IGNORECASE)]
# Loop over 6 registers
registers = ['JA_BI', 'JA_HI', 'PS_BI', 'PS_HI', 'TB_BI', 'TB_HI']
for register in registers:
    #Create empty dictionary
    freqs = {}
    # Loop over 150 files
    for filename in filenames:
        # If current file belongs to current register
        if filename[:5] == register:
            with open(filename, encoding="cp437") as txt:
                file_as_string = txt.read()
                # Disregard the header
                file_as_string = re.sub(r"<.*?>", "", file_as_string)
                # Tokenize into words
                tokens = nltk.word_tokenize(file_as_string)
                # Tag for part of speech
                tagged = nltk.pos_tag(tokens)
                # print(tagged)
                # Loop over indexes of tagged words (tuples)
                for words in range(len(tagged)):
                    # If the current word is a common noun and the following word is a common noun
                    try:
                        if re.search(r'^NNS?$', tagged[words][1]) and re.search(r"^NNS?$", tagged[words + 1][1]):
                            noun1 = tagged[words][0].upper()
                            noun2 = tagged[words + 1][0].upper()
                            noun_noun = noun1 + " " + noun2
                            freqs[noun_noun] = freqs.get(noun_noun, 0) + 1
                    except IndexError:
                        print("End of document")
    # Sort words in descending order
    freq_list = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    # Open connection to outfile
    with open("/Users/tristan/Downloads/%s_freqs_noun_noun.csv" % register, 'w') as fout:
        fout.write("Bigram,Frequency\n")
        # Loop over sorted words and frequencies
        for k, v in freq_list:
            # Write out to the current csv file
            fout.write(f'{k},{v}\n')



