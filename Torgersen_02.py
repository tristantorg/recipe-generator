"""
Assignment 2 Tristan Torgersen
"""

import re

#Here is my text. It is from chapter 1 of the novel TARZAN OF THE APES

txt = "I HAD this story from one who had no business to tell it to me, or to any other. I may credit the seductive influence of an old vintage upon the narrator for the beginning of it, and my own skeptical incredulity during the days that followed for the balance of the strange tale. When my convivial host discovered that he had told me so much, and that I was prone to doubtfulness, his foolish pride assumed the task the old vintage had commenced, and so he un- earthed written evidence in the form of musty manuscript, and dry official records of the British Colonial Office to support many of the salient features of his remarkable narrative. I do not say the story is true, for I did not witness the happenings which it portrays, but the fact that in the telling of it to you I have taken fictitious names for the principal characters quite sufficiently evidences the sincerity of my own belief that it may be true. The yellow, mildewed pages of the diary of a man long dead, and the records of the Colonial Office dovetail perfectly with the narrative of my convivial host, and so I give you the story as I painstakingly pieced it out from these several various agencies. If you do not find it credible you will at least be as one with me in acknowledging that it is unique, remarkable, and interesting. From the records of the Colonial Office and from the dead mans diary we learn that a certain young English nobleman, whom we shall call John Clayton, Lord Greystoke, was commissioned to make a peculiarly delicate investigation of conditions in a British West Coast African Colony from whose simple native inhabitants another European power was known to be recruiting soldiers for its native army, which it used solely for the forcible collection of rubber and ivory from the savage tribes along the Congo and the Aruwimi. The natives of the British Colony complained that many of their young men were enticed away through the medium of fair and glowing promises, but that few if any ever returned to their families."


# Searching for and counting the various nominalizations.

# -ing
ing = re.findall(r"\w+ings?\b", txt, flags=re.I)
print("Number of '-ing' nominalizaitons: " + str(len(ing)))
print(ing)

# -tion and -sion
tion = re.findall(r"\w+[st]ions?\b", txt, flags=re.I)
print("Number of '-tion' and '-sion' nominalizations: " + str(len(tion)))
print(tion)

# -er and -or
er = re.findall(r"\w+[eo]rs?\b", txt, flags=re.I)
print("Number of '-er' and '-or' nominalizations: " + str(len(er)))
print(er)

# -ee
ee = re.findall(r"\w+ees?\b", txt, flags=re.I)
print("Number of '-ee' nominalizations: " + str(len(ee)))
print(ee)

# -ment
ment = re.findall(r"\w+ments?\b", txt, flags=re.I)
print("Number of '-ment' nominalizations: " + str(len(ment)))
print(ment)

# -sal
sal = re.findall(r"\w+sals?\b", txt, flags=re.I)
print("Number of '-sal' nominalizations: " + str(len(sal)))
print(sal)

# -ance and -ence
ance = re.findall(r"\w+[ea]nces?\b", txt, flags=re.I)
print("Number of '-ance' and '-ence' nominalizations: " + str(len(ance)))
print(ance)

# Print the total number of nominalizaitons
total = len(ing) + len(tion) + len(er) + len(ee) + len(ment) + len(sal) + len(ance)
print("Total number of nominalizations: " + str(total))