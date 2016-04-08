import string


def loadWords2():
    try:
        inFile = open(PATH_TO_FILE, 'r', 0)
    except IOError as e:
        print "The  wordlist doesn't exist;"
        return ['apple','orange','pear','lime','lemon']
    line = inFile.readline()
    wordlist = string.split(line,',')
    print " ", len(wordlist), 'words loaded'
    return wordlist

PATH_TO_FILE = 'words2.txt'
loadWords2()

PATH_TO_FILE = 'doesntExist.txt'
loadWords2()