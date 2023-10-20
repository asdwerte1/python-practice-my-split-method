#Task - write a funciton that behaves like the split method
#Function should return a list of words created from an input string
#The list should divide the words whenever there is a space
#If the string is empty -the function should return an empty list

def mysplit(strng):
    result = []
    if len(strng) == 0:
        return result
    else:
        #Create a tmep variable to store each word until a space is created
        #Add word to list end then reset each time
        word = ""
        for char in strng:
            if char.isspace():
                if word == "":
                    continue
                else:
                    result.append(word.strip())
                    word = ""
            else:
                word += char
        #add the final word
        if result != "":
            result.append(word)

        #Check through list items - if any empty strings remove them
        for item in result:
            if len(item) == 0:
                result.remove(item)
        return result

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))