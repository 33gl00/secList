#########################
# PASSWD LIST GENERATOR #
#########################

import argparse
import os

parser = argparse.ArgumentParser(description="Generate seclist for brute force tool")
parser.add_argument("-k", "--keyword", type=str, required=True, help="Keyword for init passwordlist")
parser.add_argument("-e", "--exhaustive", action="store_true", help="Exhaustive variation")
parser.add_argument("-d", "--date", type=int, default="1985", help="Minimum date used for range")
parser.add_argument("-o", "--outputFile", type=str, default="passwdList.txt", help="Output file's path")

args = parser.parse_args()
keyword = args.keyword
minimumDate = args.date
exhaustive = args.exhaustive
outputFile = args.outputFile

def keywordFormatted(passwd):
    wordlist = []
    wordlist.append(passwd)
    wordlist.append(passwd.lower())
    wordlist.append(passwd.upper())
    wordlist.append(passwd.capitalize())
    wordlist.append(passwd[:-1] + passwd[-1].upper())
    return wordlist

def keySalted(passwd):
    wordList = []
    charSet = ["-", "+", "*", "@", "!", "#", "?", "$"]
    secondarySet = [ "'", "_", "%", "<", ">", '"', " "]

    if exhaustive :
        charSet = charSet + secondarySet

    for char in charSet:
        wordList.append(passwd + char)
        wordList.append(char + passwd)

    return wordList

def generateDates(starteDate, exhaustive):
    exhaustiveList = []
    dateList = []

    for year in range(starteDate, 2025):
        dateList.append(str(year))
    for month in range(1, 13):
        for day in range(1, 32):
            dateList.append(f"{day:02d}{month:02d}")
            for year in range(starteDate, 2025):
                exhaustiveList.append(f"{month:02d}{year}")
            for year in range(starteDate, 2025):
                exhaustiveList.append(f"{day:02d}{month:02d}{year % 100:02d}")

    if exhaustive :
        return dateList + exhaustiveList
    else :
        return dateList

def sav(outputFile, keyz, exhaustive):
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS et Linux
        os.system("clear")

    with open(outputFile, 'w') as file: 
        for key in keyz :
            file.write(key + '\n')

def mix(dateList, keyList, more) :
    passwdList = []
    result = []

    for word in keyList :
        for date in dateList :
            passwdList.append(keySalted(word + date))
            if more :
                passwdList.append(keySalted(date + word))

    for keyz in passwdList :
        for key in keyz:
            result.append(key)

    # Element distinc , clone deleted
    return set(result)

#################################################
print("In Progress...")
dateList = generateDates(minimumDate, exhaustive)
keyList = keywordFormatted(keyword)
keyz = mix(dateList, keyList, exhaustive)

sav(outputFile, keyz, exhaustive)

print(f"Password list saved in : {outputFile}")
print(f"{len(keyz)} generated")
print(f"{len(set(keyz))} generated")
exit()
######################################## eegloo