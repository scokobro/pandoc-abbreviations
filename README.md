# pandoc-abbreviations
Pandoc filter in python to replace listed abbreviations with their expansions.

# Why?
This project was created to provide a simple alternative to the kind of user-definable macros available in LaTeX, for instance...

```TeX
\newcommand{\hb}{hanbaiten}
\newcommand{\og}{oshigami}
```

which replace the two letter abbreviation with the word in the final curly brackets.

This is useful to me, as I am sure it is to many academics, as a way of ensuring consistency across uses of a single term or phrase. For instance, I write about the mass media in Japan, so I mention the titles of newspapers quite a lot; some journals want the Japanese term for newspaper transliterated 'shimbun' and some want 'shinbun'. I eventually realised, after initially going down the obvious 'search-replace' route, that it would just be easier to be able to replace every occurrence with an abbreviation that could be adjusted ad hoc. And thsi is my attempt to bring tat convenience to writing in pandoc markdown.

# Defining abbreviations
Abbreviations and their expansiosn have to be defined before you can use them, they can be stored in two different places;

1. In a 'database' file,or,
2. in the source document YAML metadata.

It doesn't really matter which but you should know that abbreviations defined in metadata will take priority over those defined in the database file.

## The 'dbase' file

Create a file called 'dbase' and place it in your `.pandoc` directory along with all that other good stuff.

Abbreviations should be defined one per line and have to look like this:

```
ltd=limited
sb=shimbun
ir=International Relations
j=日本
```

## Definitions in metadata
If you want to define local abbreviations in your source document then you can add some entries to the metadata at the start if your file. For instance;

```yaml
---
author: Peter McPython
title: Pythoning and Pythoneers
date: 20 Nov 2015
+di: discombobulatory
+afaik: as far as I know
---
```

As you can see, in the metadata definitions, abbreviations keys need to start with a '+'. The character after the '+' *must* be alphabetic.

# Using abbreviations in source document
When you're happy with your abbreviation/expansion definitions, you can then begin to start using them in your writing. To use an abbrev.(I'm abbreviating as it's getting tedious) just include the key preceded by one '+' sign. So, assuming we are using the definitions created above we would write this:

```md
Are you studying +ir?

The study of *+ir* has been proved to be **+di** and, +afaik, is unlikely to lead to nirvana.
```

and, when the document is processed, end up with:


>Are you studying international relations?
>
>The study of *international relations* has been proved to be **discombobulatory** and, as far as I know, is unlikely to lead to nirvana.

Notice that you can use the usual markdown text formatting techniques around abbreviations.

# Problems?
