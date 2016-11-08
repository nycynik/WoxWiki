# WoxWiki

A note taking personal wiki solution to capture my life.

After getting fedup from a myriad of tools which didn't satisfy
my thirst to *effectively*, *correctly*, and *seemlessly*
capture my thoughts onto the digital media, I finally decided
to write my own solution. This is how **WoxWiki** was born.

But since I'll be using this for life, it's important that my
data is stored in something portable. Flat-files although being
portable, are largely a pain because they don't have a
structured format (and XML sucks). So, all data is stored as
*markdown* inside a sqlite file (which will allow for easy
exporting).

Everything resides as a page. There are no namespaces or portals
like other traditional wikis (mediawiki), because organising
content is hard. It's pure cognitive load which we shouldn't
have to think about. Multiple categories, and multiple tags will
solve this organizing issue for us.

## Features

* [X] Easy to use
* [X] Multiple tags
* [ ] Multiple categories
    - Heirarchial category structure
* [ ] Page Linking
* [ ] Content searching
* [ ] Journaling/Diary/Blogging
* [ ] Export markdown files
* [ ] Import markdown files 

## Philosophy

- Keep it simple, silly, stupid
- Avoid feature creep
- Avoid cognitive load
- Minimal design overhead
