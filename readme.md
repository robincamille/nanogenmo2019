This project was created for NaNoGenMo (National Novel Generation Month) 2019. Using a list of existing fortunes from other sources, a list of interjections, and a Markov generator, it creates a year of daily horoscopes for each Zodiac sign. 

General format, inspired by Cosmopolitan magazine's horoscopes: date, sign, exclamation ("Yikes, Leo!"), then a mangled horoscope. 

## To use 

```
python3 horoscoperator.py
```

It outputs output.md, a Markdown-formatted file.


## Sources

The Markov generator I'm using...
- adapts [http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/](this script from agiliq.com)
- adapts the [MarkovGen library](https://github.com/mattspitz/markovge)

The interjections came from [https://github.com/dariusk/corpora/blob/master/data/words/interjections.json](Darius Kazemi's corpora repository).

The all-fortunes.txt text came from...
- [https://github.com/dariusk/corpora/blob/master/data/divination/tarot_interpretations.json](Tarot interpretations from Darius Kazemi's Corpora repo)
- [https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/](Josh Madison's fortune cookie fortunes)
- [https://github.com/vromero/fortune-cookies/blob/master/fortunes](@vromero's fortune cookie fortunes)
- [https://github.com/reggi/fortune-cookie/blob/master/fortune-cookies.txt](@reggi's fortune cookie fortunes)
- [https://github.com/ianli/fortune-cookies-galore/blob/master/fortunes.txt](@ianli's fortune cookie fortunes)

### Similar project
- [https://play.google.com/store/apps/details?id=com.volchok.minutehoroscope&hl=en_US](Horoscope a Minute) Android app that generates a horoscope every minute