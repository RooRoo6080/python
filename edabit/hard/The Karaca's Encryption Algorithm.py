def the_karacas_encryption_algorithm(string):
    reverse = ""
    for i in string:
        if i == "a":
            i = "0"
        elif i == "e":
            i = "1"
        elif i == "o":
            i = "2"
        elif i == "u":
            i = "3"
        reverse = i + reverse
    return reverse + "aca"


a = raw_input("Enter a word | ex: apple")
print the_karacas_encryption_algorithm(a)
