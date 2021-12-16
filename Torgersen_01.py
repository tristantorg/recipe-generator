"""
Assignment 1 Tristan Torgersen
"""

x = input('Type any singular English noun to see its plural form:')
x = x.lower() # Make the input word fully lower case
# Irregular/Latin based words
if x == 'cactus':
   print('Cacti')
elif x == 'fungus':
   print('Fungi')
elif x == 'nucleus':
   print('Nuclei') # There are more words that follow this pattern, but these are the most common
elif x [-2:] == 'um':
 print((x.title() [:-2]) + 'a')
# More irregular words
# Words ending in 'f' or 'fe' that go to 'ves'
elif x [-1] == 'f':
   print( x.title() [:-1] + 'ves')
elif x [-2:] == 'fe':
   print( x.title() [:-2] + 'ves')
# Words ending in 'y', including 'consonant + y'
elif x[-1] == 'y':
 if x[-2] in 'aeiou':
    print(x.title() + 's') # For words with a vowel before 'y'
 else: print((x.title()[:-1]) + 'ies') # For words with a consonant before 'y'
# Words ending in 'o'
elif x [-1] == 'o':
 print(x.title() + 'es')
# Words ending in 'ch'
elif x [-2:] == 'ch':
 print(x.title() + 'es')
# Words ending in 'x', 's', or 'z'
elif x [-1] == 'x':
 print(x.title() + 'es')
elif x [-1] == 's':
 print(x.title() + 'es')
elif x [-1] == 'z':
 print(x.title() + 'es')
# Everything else
else:
 print(x.title() + 's')
