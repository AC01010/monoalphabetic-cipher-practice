import string
import random
import time

def keyStringRandom():
    A = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while not testValid(A):
        random.shuffle(A)
    return "".join(A)
    
def testValid(l):
    for i in range(26):
        if ord(l[i])-65==i:
            return False
    return True

def display(quote, replace):
    print(chr(27)+"[2J")
    print(u"\u001b[1m\u001b[31mCiphertext: ")
    print()
    words = quote.split(" ")
    lines = []
    while len(words)>0:
        line = ""
        while len(line)<50:
            if len(words)>0:
                line+=(words.pop(0)+" ")
            else: break
        lines.append(line[0:-1])
    replacement = quote.lower()
    for i in range(0,26):
        if replace[i]!=" ":
            replacement = replacement.replace(chr(i+97),replace[i])
    for i in list(string.ascii_lowercase):
        replacement = replacement.replace(i,"_")
    words2 = replacement.split(" ")
    lines2 = []
    while len(words2)>0:
        line = ""
        while len(line)<50:
            if len(words2)>0:
                line+=(words2.pop(0)+" ")
            else: break
        lines2.append(line[0:-1])
    for i in range(len(lines)):
        print(u"\u001b[37m"+lines[i])
        print(u"\u001b[33m"+lines2[i])
        print()
    print(u"\u001b[1m\u001b[31mFrequency Table: ")
    print()
    freqtable = [list(string.ascii_uppercase)]
    freqs = []
    for i in freqtable[0]:
        freqs.append(quote.count(i))
    freqtable.append(freqs)
    freqtable.append(list(replace))
    l = u"\u001b[37m\t\t"
    for i in range(26):
        l+=freqtable[0][i]+" "*len(str(freqtable[1][i]))
    print(l)
    l = "Frequency\t"
    for i in range(26):
        l+=str(freqtable[1][i])+" "
    print(l)
    l = "Replacement\t"
    for i in range(26):
        l+=freqtable[2][i]+" "*len(str(freqtable[1][i]))
    print(l)
    print()
    return replacement

def chooseMode(mode, l):
    if mode in ["list", "l"]:
        print(chr(27)+"[2J")
        print("Here are the list of available modes:")
        print("List/l")
        print("Help/h")
        print("Aristocrat/aristo/a")
        print("Patristocrat/patristo/pat/p")
        print("Quit/q\n")
    if mode in ["help", "h"]:
        print(chr(27)+"[2J")
        print("To replace a letter, input two characters: the ciphertext character and your plaintext replacement.")
        print("To remove a letter, type the ciphertext character whose replacements you would like to remove.")
        print("To give yourself a hint, type the word 'hint', followed by the letter which you would like to reveal.") 
        print("A ciphertext, your replacement plaintext, and a frequency table will be printed out in the terminal.")
        print("To quit, type 'quit'.\n")
    if mode in ["aristocrat", "aristo", "a", "patristocrat", "patristo", "pat", "p"]:
        print(chr(27)+"[2J")
        key = keyStringRandom()
        r = random.randint(0,40568)
        while len(l[r])<65 or len(l[r])>160:
            r = random.randint(0,40568)
        quote = l[r].upper()
        if mode in ["patristocrat", "patristo", "pat", "p"]:
            quote2 = ""
            for ch in quote:
                if ch in string.ascii_uppercase:
                    quote2+=ch
            quote = " ".join(quote2[i:i+5] for i in range(0,len(quote2),5))    
        ct = ""
        for ch in quote:
            if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                ct+=key["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(ch)]
            else: ct+=ch
        replacements = "                          "
        begin = time.time()
        hints = 0
        while display(ct,replacements)!=quote:
            inp = input("Replacement characters? ")
            if inp.lower()[0:4]=="hint":
                replacements = replacements[:(ord(inp[-1].upper())-65)]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[key.index(inp[-1].upper())]+replacements[(ord(inp[-1].upper())-64):]
                hints+=1
            if inp.lower()[0:4]=="quit": break
            if len(inp)==1 and inp.isalpha(): 
                replacements = replacements[:(ord(inp[0].upper())-65)]+" "+replacements[(ord(inp[0].upper())-64):]
            if len(inp)==2 and inp.isalpha(): 
                replacements = replacements[:(ord(inp[0].upper())-65)]+inp[1].upper()+replacements[(ord(inp[0].upper())-64):]
        duration = time.time()-begin
        if display(ct,replacements)==quote:
            print("Congrats! You have completed the cipher in "+str(round(duration,3))+" seconds!\n")
            if hints:
                print("You used "+str(hints)+" hints.\n")
    if mode in ["quit", "q"]:
        exit()

def main():
    print(chr(27)+"[2J")
    print("Monoalphabetic Substitution Cipher Generator")
    modeList = ["list", "l", "help", "h", "aristocrat", "aristo", "a", "patristocrat", "patristo", "pat", "p", "quit", "q"]
    quotes = open("quotes.txt", "r")
    l = []
    for i in range(40569):
        l.append(quotes.readline().strip())
    while 1:
        mode = input("What would you like to do? For a list of commands, type 'list'. ").strip().lower()
        while mode not in modeList:
            mode = input("Sorry, I didn't understand that. What would you like to do? For a list of commands, type 'list'. ").strip().lower()
        chooseMode(mode,l)
            
if __name__ == "__main__":
    main()