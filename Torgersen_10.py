"""
Assignment 10 Tristan Torgersen

https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-
in-python/
"""
### GET ALL FILES IN LIST ###
def file2str(pathway):
    with open(pathway, encoding="utf8") as infile:
        return infile.read().replace("\n", " ")

import os, re
os.chdir("/Users/tristan/Downloads/news_universe/")
filenames = [i for i in os.listdir() if re.search(r"\.txt", i)]

doc_complete = [file2str(i) for i in filenames]

### CLEAN UP LIST OF FILES ###
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = stopwords.words('english')
exclude = string.punctuation
exclude = "".join([ch for ch in exclude if not re.search(r"[-']", ch)])
exclude += "”"
exclude += "“"
lemma = WordNetLemmatizer()
def clean(doc):
    doc = ''.join(ch for ch in doc if ch not in exclude)
    doc = " ".join(i for i in doc.lower().split() if i not in stop)
    doc = re.sub(r"([a-z]+)\d+", r"\1", doc)
    doc = " ".join(lemma.lemmatize(word) for word in doc.split())
    return doc

doc_clean = [clean(doc).split() for doc in doc_complete]
doc_clean = [[wd for wd in doc if wd != "u"] for doc in doc_clean]

### GET TOPICS ###
import gensim
from gensim import corpora

# Creating the term dictionary of our corpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
num_topics = 10
num_words = 10
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word = dictionary, passes=50)
results = ldamodel.print_topics(num_topics=num_topics, num_words=num_words)
for r in results:
    print(r)

with open("/Users/tristan/Downloads/results.csv", mode="w") as fout:
    for result in results:
        output = str(result[0]+1) + ","
        words = re.findall(r'"([^"]+)"', result[1])
        for word in words:
            output += word + ","
        output = output[:-1]
        output += "\n"
        fout.write(output)


### VISUALIZE THE TOPICS ###
import pyLDAvis.gensim_models
visualization = pyLDAvis.gensim_models.prepare(ldamodel, doc_term_matrix, dictionary)
pyLDAvis.save_html(visualization, "/Users/tristan/Downloads/visualization.html")
