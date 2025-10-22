# indexing syntax: string_name[startindex:endindex:step]
myname = "abcdefghij"
print(len(myname))
print(myname[-1])      # last character
print(myname[-1:-8:-1])  # slicing with negative step

# converting negative slicing to positive slicing
print(myname[9:2:-1])