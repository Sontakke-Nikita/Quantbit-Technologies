#Task3 Find the first non repeating character

str1=input("enter a string")
def uniqueChar(s1):
    for i in range(len(s1)):
        if s1.count(s1[i])==1:
            return s1[i]
    return "None"
print(uniqueChar(str1))   

