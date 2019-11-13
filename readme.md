This project was created for NaNoGenMo (National Novel Generation Month) 2019. Using a list of existing fortunes from other sources, a list of interjections, and a Markov generator, it creates a year of daily horoscopes for each Zodiac sign. 

General format, inspired by Cosmopolitan magazine's horoscopes: date, sign, exclamation ("Yikes, Leo!"), then a mangled horoscope. 

## To use 

```
python3 horoscoperator.py
```

It outputs output.md, a Markdown-formatted file.

## Sample output  

### Monday, November 30, 2020

#### Aries

Curses, Aries! For problems at the end of the people is the breakfast of champions. The early bird gets the work, but the daylight sick. When one burns one's bridges, what a very nice fire it makes. Big book, big bore. Alimony and bribes will engage a large share of your loved ones will be advanced socially, without any special effort your.

#### Taurus

Right, Taurus! Today. Pick battles big enough to make me ambitious. A true friend is a true sense of humor is not being emotional, but being able to decide. Wherever you go, whenever you can, and pride is taking less than your dreams. Bloom where you go. I learn by going where i have counted 136 different kinds of composition decompositions.

#### Gemini

Gee whiz, Gemini! A month of opportunities, you.

#### Cancer

Just wondering, Cancer! You always know when to will.

#### Leo

Tsk-tsk, Leo! Rather not do. Education is the mastery of every virtue at the moment of awkwardness. Stop procrastinating - starting tomorrow. Enthusiastic leadership gets you a huge in.

#### Virgo

Well, well, Virgo! By hate. Hate is never profound except when he was too small and walked on his toes to make it's.

#### Libra

Oh-oh, Libra! Talents and abilities. You are rendering a final decision. You are embracing the aid of the people who never try. The person who can be enjoyed today. A family reunion in the future. To understand is hard. Take care and understanding, your life together. You are honoring the spirit, not just the letter, of mess..

#### Scorpio

Meh, Scorpio! You are getting your heart's desire. You are preserving purity. You are refusing to settle for a long journey over water. Actions have unexpected consequences, so be prepared. You are on the soil of many cannot. You will be run by.

#### Sagittarius

Well done, Sagittarius! Are 75. If all the options you have. You are seeking guidance from a higher power. You are constantly changing your mind. You are only young once, but your parents moved away, and you will run with success. We all have extraordinary coded within us, waiting to be caught in a eucalyptus tree tonight. You will make for.

#### Capricorn

Word, Capricorn! The possible repercussions of your life so far. You will be blessed with longevity. You will soon be yours. Functioning superbly will come true. You are believing good things happen to be turned on its way. Be direct, usually one can accomplish more that way. Use your eloquence where it will do well when you think you can be anywhere. Your reasoning is excellent your aim like.

#### Aquarius

Dear me, Aquarius! Have good luck and overcome many hardships. A good beginning is half the task. Sometimes traveling to new situations. You are aligning yourself with negative or unhealthy extent. A lover is getting restless. Find out what he has, but also makes you feel good. Merging. You are tearing something or someone apart. You are never silly depend on them to guide you. You will find an.

#### Pisces

Tut, Pisces! Always know when to be equal with men lacks ambition. Ouch!!! the greatest power is in your friends. Rest has a peaceful effect on your in.


## Sources

The Markov generator I'm using...
- adapts [this script from agiliq.com](http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/)
- adapts the [MarkovGen library](https://github.com/mattspitz/markovge)

The interjections came from [Darius Kazemi's corpora repository](https://github.com/dariusk/corpora/blob/master/data/words/interjections.json).

The all-fortunes.txt text came from...
- [Tarot interpretations from Darius Kazemi's Corpora repo](https://github.com/dariusk/corpora/blob/master/data/divination/tarot_interpretations.json)
- [Josh Madison's fortune cookie fortunes](https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/)
- [@vromero's fortune cookie fortunes](https://github.com/vromero/fortune-cookies/blob/master/fortunes)
- [@reggi's fortune cookie fortunes](https://github.com/reggi/fortune-cookie/blob/master/fortune-cookies.txt)
- [@ianli's fortune cookie fortunes](https://github.com/ianli/fortune-cookies-galore/blob/master/fortunes.txt)

### Similar project
- [Horoscope a Minute](https://play.google.com/store/apps/details?id=com.volchok.minutehoroscope&hl=en_US) Android app that generates a horoscope every minute