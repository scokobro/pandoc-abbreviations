# pandoc-abbreviations
Python filter for [pandoc](http://pandoc.org/index.html), replaces user-defined abbreviations with their expansions.

# This project's aim
This project was created to provide a simple alternative to the kind of user-definable macros available in LaTeX, for instance...

```TeX
\newcommand{\hb}{hanbaiten}
\newcommand{\osh}{oshigami}
```

which , when the source document is processed, replace the typed abbreviations (i.e. `\hb` above) with the word in the final curly brackets, the expansion.

This is useful to me, as I am sure it is to many writers, as a way of ensuring consistency across uses of a single term or phrase. For instance, I write about the mass media in Japan, so I mention the titles of newspapers quite a lot; some journals want the Japanese term for newspaper transliterated 'shimbun' and some want 'shinbun'. I eventually realised, after initially going down the obvious 'search-replace' route, that it would just be easier to be able to replace every occurrence with an abbreviation (the macros mentioned above when I was writing in LaTeX) the expansion of which could be adjusted ad hoc. And this is my attempt to replicate that convenience when writing in pandoc markdown.

# Installation
'Installing' seems like rather a grand word for this: Copy the `abbrevs.py` file into your home directory's `.pandoc/filters/` directory.

This filter relies on the functionality of the [pandocfilters](https://github.com/jgm/pandocfilters) project so please make sure it's installed.

Bingo. Read on...

# Defining abbreviations
Abbreviations and their expansions have to be defined before you can use them, they can be stored in two different places;

1. In a 'database' file, or,
2. in the source document YAML metadata.

It doesn't really matter which but you should know that abbreviations defined in metadata will take priority over those defined in the database file.

## The 'dbase' file

Create a file called 'dbase' and place it in your home directory's `.pandoc` directory, along with all that other good stuff.<sup id="a1">[1](#f1)</sup>

Abbreviations can be added to this file, this make them available for use in all source documents. They are defined as `key=value` pairs, one per line; they have to look like this:

```
ltd=limited
sb=shimbun
ir=International Relations
j=日本
```

Keys (the bit on the left of the '=') have to be alphabetic. As you can see, expansions (the stuff to the right of the '=') can contain multiple words (unfortunately not paragraphs though) and the double-byte characters used in CJK languages.

## Definitions in metadata
If you want to define local abbreviations in your source document then you can add some `key: value` entries to the metadata at the start if your file. For instance;

```yaml
---
author: Peter McPython
title: Pythoning and Pythoneers
+di: discombobulatory
+afaik: as far as I know
---
```

As you can see, in the metadata definitions, abbreviations keys need to start with a '+'. The character after the '+' *must* be alphabetic. Be aware that these will override the definitions in the 'dbase' file.

# Using abbreviations in source document
When you're happy with your abbreviation/expansion definitions, you can then begin to use them in your writing. To use an abbrev.(I'm abbreviating as it's getting tedious) just include the `key` preceded by one '+' sign. So, assuming we are using the definitions created above we would write this:

```markdown
## Studying +ir

The study of *+ir* has been proved to be **+di** and, +afaik, is unlikely to lead to nirvana.
```

and, when the document is processed, end up with:

>## Studying international relations
>
>The study of *international relations* has been proved to be **discombobulatory** and, as far as I know, is unlikely to lead to nirvana.

Notice that you can use the usual markdown headers and text formatting techniques around abbreviations. Punctuation is also preserved properly.

And that's it really.

# Problems and limitations
Tests have been whatever the opposite of 'thorough' is. As far as I can see it doesn't wreck any of the standard pandoc markdown functionality. I'd be interested to hear from anyone who has problems or doesn't get the results they are expecting.

It'd be nice to be able to use this to insert boilerplate text snippets, but in order to do that we would need to deal with paragraphs. I'm certain this is fairly straightforward but I'm sick of dealing with json for the time being... maybe next year:wink:

----

<b id="f1">1</b> Footnote content here.
If you would prefer to put your 'dbase' file somewhere else you can put the path to your file into the line that read `#dbasePath = 'a/path/of/your/choice'# user selected path` (make sure you uncomment it!) And indeed you can call the file whatever you want. [↩](#a1)
