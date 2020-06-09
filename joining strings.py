str_one = "Happy"
str_two = "Day"

print(str_one + " " + str_two)

print("%s %s" % (str_one, str_two))

print("{0} {1}".format(str_one, str_two))

print("{first} {second_str}".format(first=str_one, second_str=str_two))

print(f"{str_one} {str_two}")