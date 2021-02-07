from urban import getDef
maxlength=10
print("Welcome to the urban dictionary cli tool, press ^C to exit at any time.")
def getInput():
    word = input("Enter a word to search: ")
    if word.strip()=='':
        print("You can't put nothing! Try again!")
        getInput()
    wordlist = getDef(word)
    if len(wordlist)<=0 or word == None:
        print("We didn't find any results! Try again!")
        getInput()
    else:
        print("We found "+str(len(wordlist))+" matches for "+word+":\n ")
        def listWords(wordlist):
            defnum=0
            # Listing out all the words when a user enters a search query
            for word in wordlist:
                # Get the definition key from the word dictionary
                definition=word["definition"]
                # If the length is greater than 10 words, we need to cut it off
                if len(definition.split(' ')) >maxlength:
                    definition=definition.split(' ')
                    definition=' '.join(definition[0:maxlength])+"..."
                # Print the definit
                print("["+str(defnum)+"] : "+definition+"\n\n")
                defnum+=1
            select=input("Enter a definiton number to see a definition in more detail, or enter anything else to go back to search: ")
            try:
                if int(select) <len(wordlist):
                    word = wordlist[int(select)]
                    print("\nFull definition of "+word["word"]+":\n")
                    print("Definition: "+word["definition"]+"\n")
                    print("Example: "+word["example"]+"\n")
                    print("Thumbs up: "+str(word["thumbs_up"])+", Thumbs down: "+str(word["thumbs_down"])+"\n")
                    print("Author: "+word["author"]+"\n")
                    print("Written on: "+word["written_on"]+"\n")
                    print("Permalink: "+word["permalink"]+"\n")
                    print("Definition id: "+str(word["definition_id"]))
                    select = input("Type 'r' to go back to results or anything else to go back to search: ")
                    print("\n\n")
                    if select == 'r':
                        listWords(wordlist)
                    else:
                        getInput()
                else:
                    getInput()
            except ValueError:
                getInput()
        listWords(wordlist)

try:
    getInput()
except KeyboardInterrupt:
    print("\nExiting")
    exit(0)