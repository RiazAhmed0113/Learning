# String Slicing = create a substring by extracting elements from another string
#                  indexing[] or slice()
#                  [start:stop:step]

name = "Riaz Ahmed"

first_name = name[0:4]
last_name = name[5:10]

funky_name = name[0:10:2]

reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
