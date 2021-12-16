"""
Assignment 9 Tristan Torgersen
"""
import requests, urllib.parse, random, justext, os
from bs4 import BeautifulSoup as bs

os.chdir("/Users/tristan/Downloads/")

url = "https://en.wikipedia.org/wiki/Pterosaur"  # define the url to be used as the starting page
response = requests.get(url)  # pull text from the url
soup = bs(response.content, "html.parser")
anchors = soup.find_all("a")
links = []  # create an empty list to store the links
for anchor in anchors:  # loop through the anchor tags
    try:
        links.append(anchor.attrs['href'])  # add it to the 'links' list if it has an href attribute
    except KeyError:
        print("skipping this anchor because it doesn't have an href attribute")

links = [l for l in links if len(l) > 0]  # get rid of any empty links
links = set(links)
links = [l for l in links if l[0] != "#"]  # get rid of links with an initial #

def get_absolute_path_link(url, relative_link):
    parsed_url = urllib.parse.urlparse(url)
    return urllib.parse.urljoin(parsed_url.scheme + "://" + parsed_url.netloc, relative_link)

links = [get_absolute_path_link(url, l) for l in links]
random.shuffle(links)  # randomly shuffles links

num_links = 10  # only select 10 of the randomly sorted links
if len(links) < num_links:  # if there are less than 10 links, use all of them
    num_links = len(links)

for i in range(num_links):  # loop through each link
    current_url = links[i]
    with open('%s.txt' %i, 'w', encoding='utf-8') as outfile:  # open a new outfile named after the number of link
        try:
            response = requests.get(current_url)  # pull text from the url of the link
        except:
            continue
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        for paragraph in paragraphs:
            if not paragraph.is_boilerplate:  # just take the text
                outfile.write(paragraph.text)  # print text to outfile

