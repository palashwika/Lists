#function to check whether
#first an last character of words match
def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

    print("List of words with first and last character name\n", lst)
    return ctr
count =match_words(['abc','cfd','xyz','aba','1222','ddd'])
print("Number of words having first and last character same: ", count)