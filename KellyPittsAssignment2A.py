def readFile(filepath):                             #Open and closes the file to read.
    file = open(filepath, "rt")
    outText = file.read()
    file.close()
    return outText

def stripChars(inText):                             #Strips all the special characters from the file
    sChars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'    #Runs through the 'list' and replaces every occurrence
    outText = ""                                    #of the characters displayed in 'sChars' with a space
    for i in inText:
        if (i in sChars):
            i = ' '
        outText += i
    return outText

def displayStats(text):                             #This function counts the amount of occurrences each word appears in the file
    uniqueList = []
    countlist = []
    word = ''
    for item in text:                               #This loop loads the empty list 'uniqueList'
        for j in text:                              #'uniqueList' creates an empty list which appends a single word occurrence
            if item in uniqueList:                  #so that there are no double ups.
                continue
            elif item == j:
                uniqueList.append(item)

    number = 1                                      #'number' displays the number in the print statement #eg. #1, #2, #3
    for item in uniqueList:                         #This loop counts how many words there are in the uniqueList against the
        count = 0                                   #original text file by checking if they are equal to each other.
        for j in text:                              #Then appends them to a new list which holds the count and the unique word
            if item == j:
                count += 1
                word = item
        countlist.append([count, word])
    countlist.sort()                                #This sorts the list, then reverses the order so it is in decreasing order.
    countlist.reverse()

    for i in range(10):                             #This loop runs 10 times so it prints the top 10 words only.
        print("#{0} \"{1}\" used {2} times.".format(number, countlist[i][1], countlist[i][0]))
        number += 1

def main(text):                                     #the main function which calls all other functions and makes changes
    text = stripChars(text)                         #to the file.
    text = text.lower()                             #Makes all letters in the file lowercase
    print(text)                                     #Prints the text as a string
    text = text.split()                             #Changes the string into a list of individual words
    print("\nTop 10 most frequently used words:")
    displayStats(text)

if __name__ == '__main__':
    text = readFile('pythonwiki.txt')               #reads the file
    main(text)                                      #calls the main function