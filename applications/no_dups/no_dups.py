def no_dups(s):
    # Your code here
    #store the values
    cache = {}
    new_arr = []
    #loop through strings
    for word in s.split():

        if word not in cache:
            cache[word] = 1
            new_arr.append(word)
            #join empty/extra spaces between words
    return ' '.join(new_arr)       
        
        
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))