#2020 horoscopes book for NaNoGenMo

import datetime, json, random, markovgen, re, string

#set up date paramaters 
start = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d") #change to 2021-01-01
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

#set up signs
signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

#set up horoscope text
interjectionfile = open('interjections.json','r')
interjections = interjectionfile.read()
interjectionfile.close()
interjectionlist = json.loads(interjections)["interjections"]

markovorig = open("all-fortunes.txt")

#set up output file
outfile = open("output.md","w")

outfile.write("# 2020 Horoscopes\n\n")

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
        outfile.write("### " + sign + "\n\n")
        interjection = interjectionlist[random.randint(0,(len(interjectionlist)-1))].capitalize()
        #fortune = tarot[random.randint(0,(len(tarot)-1))].lower().capitalize()

        # Repeatable Markov'd text generator
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

        #print(interjection + ", " + sign + "! " + fortune[:-1] + " " + mfortune)

        #print(interjection + ", " + sign + "! " + mfortune)
   
        outfile.write(interjection + ", " + sign + "! " + mfortune + "\n\n")
    outfile.write("---\n")


print("Done")
outfile.close
markovorig.close()

# Script modified from http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
# Original MarkovGen library from https://github.com/mattspitz/markovgen - modified by RobinCamille to spit out smaller chunks
