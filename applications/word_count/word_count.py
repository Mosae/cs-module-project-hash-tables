def word_count(s):
    # Your code here
    #store key values
    cache = {}
    #turn words to lower case
    lower_case = s.lower()
    #ignore said char
    ignore_char = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    #print(ignore_char)
    #loop through above string
    for c in ignore_char:
        #if its not a word - replace with white space
        lower_case = lower_case.replace(c, '')
        #print(lower_case)
    #separate the words
    for word in lower_case.split():
        #print(word)
        #if word is empty, return empty dict
        if word == '':
            return
        #if word is not in the cache add 1
        if word not in cache:
            cache[word] = 1
            #print(word)
        # else increase by 1    
        else:
            cache[word] += 1  
            #print(cache)
    return cache  
    #split string in key words on white space
    #output to lower case



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))