## About 

This project was created for [NaNoGenMo 2019](https://github.com/nanogenmo/2019) (National Novel Generation Month). Using a list of existing horoscopes and fortunes from other sources, a list of interjections, and a Markov generator, it creates a year of daily horoscopes for each Zodiac sign. 

General format, inspired by Cosmopolitan magazine's horoscopes: date, sign, exclamation ("Yikes, Leo!"), then a mangled horoscope. 

Absolutely zero astrological knowledge went into the creation of this script. It's meant to be whimsical but not mean-spirited.

## To use 

On the command line (Terminal on a Mac), type: 

```
python3 horoscoperator.py
```

It will ask you to type which sign you want output for (e.g., "Leo") or "All."

The script outputs output.md, a Markdown-formatted file. If you chose one sign, the file is about 16,000 words long. If you chose all signs, it will be about 200,000 words long.

## Sample output  

### Monday, November 30, 2020

#### Aries

Curses, Aries! For problems at the end of the people is the breakfast of champions. The early bird gets the work, but the daylight sick. When one burns one's bridges, what a very nice fire it makes. Big book, big bore. Alimony and bribes will engage a large share of your loved ones will be advanced socially, without any special effort your.

#### Taurus

Right, Taurus! Today. Pick battles big enough to make me ambitious. A true friend is a true sense of humor is not being emotional, but being able to decide. Wherever you go, whenever you can, and pride is taking less than your dreams. Bloom where you go. I learn by going where i have counted 136 different kinds of composition decompositions.

#### Gemini

Gee whiz, Gemini! A month of opportunities, you.

[See more of the sample text for all signs](https://github.com/robincamille/nanogenmo2019/blob/master/sample-output_all.md)

[See sample text for one sign](https://github.com/robincamille/nanogenmo2019/blob/master/sample-output_leo.md)


## Sources

The Markov generator I'm using...
- adapts [this script from agiliq.com](http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/)
- adapts the [MarkovGen library](https://github.com/mattspitz/markovge)

The interjections came from [Darius Kazemi's corpora repository](https://github.com/dariusk/corpora/blob/master/data/words/interjections.json).

A huge thank you to the sources for all-fortunes.txt...
- [Tarot interpretations from Darius Kazemi's Corpora repo](https://github.com/dariusk/corpora/blob/master/data/divination/tarot_interpretations.json)
- [Josh Madison's fortune cookie fortunes](https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/)
- [@vromero's fortune cookie fortunes](https://github.com/vromero/fortune-cookies/blob/master/fortunes)
- [@reggi's fortune cookie fortunes](https://github.com/reggi/fortune-cookie/blob/master/fortune-cookies.txt)
- [@ianli's fortune cookie fortunes](https://github.com/ianli/fortune-cookies-galore/blob/master/fortunes.txt)

### Similar project
- [Horoscope a Minute](https://play.google.com/store/apps/details?id=com.volchok.minutehoroscope&hl=en_US) Android app that generates a horoscope every minute

---

## To do
- Fiddle with capitalization / punctuation 
- Is there a better way to use Markov chains to structure a sentence? 
- Should the signs be ordered somehow? Current sign first? 
- Consider adding to the structure: moon/planet movements, final piece of advice
