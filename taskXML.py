 # reading xlm file
import xml.etree.ElementTree as ET # import package
tree = ET.parse('movie.xml') # parse file
root = tree.getroot() # get root
print(root.tag) # print tag
print(root.attrib) # print root attribute
for child in root: # for loop through nodes
  print(child.tag, child.attrib) # print tags and attributes
print(iter(child)) # print object
print("".join(root.itertext())) # print text

counter_f = 0 # make a counter for favorite movies
counter_u = 0 # make a counter for non-favorite movies
for child in root:
  for item in child: # for loops to find info we need
      for ite in item.findall("movie"): # focus on movie tag
          for i in ite.attrib.values(): # get values within attribute
            if i == 'True': # if value is true
              counter_f+=1 # show as favorite
            if i == 'False': # if value is false
              counter_u+=1 # show as non-favorite
print("\n")
print(f'There are {counter_f} favorite movies.') #format print
print(f"There are {counter_f} movies that aren't favorites.") #format print