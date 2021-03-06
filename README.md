MTG Montage
===========

MTG Montage is a small program that will take a list of Magic: The Gathering
cards (in standard format), finds images stored locally that match each card
name, resamples them, and places them on a 3x3 grid in a pdf file. This pdf
can be printed and the cards will be the same size as a real magic card.

Disclaimer: This software is to be used for personal proxies only. If you
enjoy playing the game, buy the cards.

Installation
------------

  - For OSX and Linux users, run `sudo pip install mtg-montage` or download the script `bin/mtg-montage` and put it on your system

Screenshots
-----------

![card list](https://raw.githubusercontent.com/maxmackie/mtg-montage/gh-pages/img/text.png)

![output pdf](https://raw.githubusercontent.com/maxmackie/mtg-montage/gh-pages/img/cards.png)

Dependencies
------------

  - `imagemagick` and `montage`: [Installation Instructions](http://www.imagemagick.org/script/binary-releases.php)
  - High Quality MTG Card Scans: [CCGH Releases](http://www.slightlymagic.net/forum/viewforum.php?f=15&sid=d0990f90b80adda9df59504a87d1f88f)

Examples
--------

`mtg-montage` is very straightforward to use. At the very minimum, it requires
three pieces of information: the directory where your images are stored, the file
that contains the list of cards you want to proxy, and the name of the pdf output
file and where it should be stored.

You can get more information on all the supported flags by looking at the `--help`
text. Below are some common usage examples.

1. Standard usage
```
mtg-montage --directory ~/mtg-images/ --input ~/cubelist.txt --output ~/cubelist.pdf
```
2. Save the card choices you make
```
mtg-montage --directory ~/mtg-images/ --input ~/cubelist.txt --output ~/cubelist.pdf --savefile ~/choices.txt
```
3. Load a past set of choices to regenerate the pdf
```
mtg-montage --directory ~/mtg-images/ --input ~/cubelist.txt --output ~/cubelist.pdf --choices ~/choices.txt
```
4. Run a test, don't actually make the pdf. This is useful if you want to see which cards the program can't find
```
mtg-montage --directory ~/mtg-images/ --input ~/cubelist.txt --output ~/cubelist.pdf --test
```
