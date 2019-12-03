#2020 horoscopes book for NaNoGenMo by @robincamille
#Outputs a long .md file of daily horoscopes for each date in 2020

import datetime, json, random, markovgen, re, string

#set up signs
signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", \
         "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

#get user input: one sign, or all signs?
mysign = input("Which sign would you like to get a book of horoscopes for?\n \
Choose: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, \
Sagittarius, Capricorn, Aquarius, Pisces, or All\n")
mysign = mysign.capitalize()
while mysign not in signs:
    if mysign == "All":
        break #list signs remains same, contains all 12 Zodiac signs
    else: #not All or any sign
        mysign = input("****************************************\n \
Try again, and pick from this list:\n \
Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, \
Sagittarius, Capricorn, Aquarius, Pisces, or All\n")
else:
    signs = [mysign] #user has chosen one sign

print("Generating book of horoscopes...")

#set up date paramaters 
start = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d") #change to 2021-01-01
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]


#set up interjections for "Yikes, Gemini!" style opener
interjectionfile = open('interjections.json','r')
interjections = interjectionfile.read()
interjectionfile.close()
interjectionlist = json.loads(interjections)["interjections"]


#set up output file
outfile = open("output.md","w")
outfile.write("# Daily Horoscopes for 2020\n")
if len(signs) == 1:
    outfile.write("## For " + signs[0] + "\n\n")

# function: Markov chain text generator
markovorig = open("source-text.txt")
def makeFortune():
    mk = markovgen.Markov(markovorig)
    line = mk.generate_markov_text()

    #remove punctuation
    exclude = ['"','(',')',';'] 
    line = ''.join(ch for ch in line if ch not in exclude)

    #make line lowercase, add period at end
    line = line.lower()
    line = line.split(". ")
    mfortune = []
    for l in line:
        l += "."
        mfortune.append(l.capitalize())
    mfortune = ' '.join(mfortune)
    return(mfortune)

for date in date_generated:
    if date.strftime("%d")[0] == "0":
        day = date.strftime("%d")[1]
    else:
        day = date.strftime("%d")
    #print("\n\n" + date.strftime("%A, %B") + " " + day + date.strftime(", %Y"))
    outfile.write("\n\n## " + date.strftime("%A, %B") \
                  + " " + day + date.strftime(", %Y") + "\n\n")

    for sign in signs:
        #print("\n" + sign)
        interjection = interjectionlist[random.randint(0,(len(interjectionlist)-1))].capitalize()
        if len(signs) > 1:
            outfile.write("### " + sign + "\n\n")
            interjection = interjection + ", " + sign + "! "
        else:
            interjection = interjection + "! "
        #fortune = tarot[random.randint(0,(len(tarot)-1))].lower().capitalize()

        outfile.write(interjection + makeFortune() + "\n\n")
        outfile.write("---\n")


print("Done: see output.md")
outfile.close
markovorig.close()

# Script modified from http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
# Original MarkovGen library from https://github.com/mattspitz/markovgen - modified by RobinCamille to spit out smaller chunks
