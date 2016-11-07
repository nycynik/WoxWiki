# WoxWiki

A note taking personal wiki solution to capture my life.

After getting fedup from a myriad of tools which didn't satisfy
my thirst to *effectively*, *correctly*, and *seemlessly*
capture my thoughts onto the digital media, I finally decided
to write my own solution. This is how **WoxWiki** was born.

Humans live for a long time. I reckon, I still have some time
left, and I want a place where I can dump everything *easily*.

It should allow categorizing, organising, searching, pretty much
everything a brain dump should do.

But since I'll be using this for life, it's important that my
data is stored in something portable. Flat-files although being
portable, are largely a pain because they don't have a
structured format (and XML sucks). So, all data is stored as
*markdown* inside a sqlite file.

## Features

* [X] Easy to use
* [X] Multiple tags
* [ ] Multiple categories
* [ ] Page Linking
* [ ] Content searching
* [ ] Namespaces
* [ ] Journaling/Diary/Blogging
* [ ] Export markdown files
* [ ] Import markdown files 

---

## Philosophy

- Keep it simple, silly, stupid
- Avoid feature creep
- Avoid cognitive load
- Minimal design overhead
- Minimal use of colors
- Everything inside a database, flat files are a useless
  abstraction.

## Goals

Importance scale: 0, 1, 2, .. inf .. 

`0` being the most important feature.

* Pages
    - Add
    - Move
    - Edit
    - Remove
* Categories
    - Multiple categories
    - category page
    - list of categories
    - nested categories
* Tags
    - mutiple tags
    - tag page
    - list of tags
* Something like a namespace
    - Any page can *only* belong to one namespace
    - used for highest level classification
* File upload as a direct child (subpage)
    - for easy linking in markdown
* Improve UI

