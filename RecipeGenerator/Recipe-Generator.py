
import json, re, os
ingr1 = input("Type an ingredient that you have and press 'Enter':") # ask the user for ingredients as input and save them to a value
ingr2 = input("Type another ingredient that you have and press 'Enter':")
ingr3 = input("Type another ingredient that you have and press 'Enter':")
directory = __file__[:-19]
os.chdir(directory+'recipes_raw copy')
filenames = [f for f in os.listdir() if re.search(r"\.json", f, flags=re.IGNORECASE)]
for filename in filenames: #for loop between the 3 .json recipe data files
    with open(filename) as infile:
        recipe_json = json.load(infile) #load as .json file
        recipe_values = recipe_json.values() #returns values of first dictionary (gets rid of 31-digit recipe code)
        for recipe in recipe_values: #for loop runs through the values
            try:
                if ingr1 in str(recipe["ingredients"]) and ingr2 in str(recipe["ingredients"]) and ingr3 in str(recipe["ingredients"]):
                    print("---------------------------------------------------------------------\n")
                    bolded_title = "\033[1m" + recipe["title"] + "\033[0m"
                    print(bolded_title)
                    ingredients = "\n".join(recipe["ingredients"])
                    print("\n ---Ingredients---\n" + ingredients)
                    instructions = recipe["instructions"]
                    print("\n ---Instructions---\n" + instructions)
            except KeyError:
                print("")
