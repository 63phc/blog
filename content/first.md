title: Лети как ветер булзай
date: 2018-02-07 21:10
author: pavel burns
tags: ass, publishing
slug: fly_as_air_bulzai
keywords: coding
category: Yeah
headline: или почему я выбрал Pelican
og_image: https://habrastorage.org/webt/26/iw/te/26iwte8ajw3kxx9cqfoyeugdo1g.jpeg

#Лети как ветер булзай
---
Стандартная фраза с которой я начинаю уже свой третий блог,
это тестовая статья и в ней я просто расскажу, как дожил до тогого, что у меняю уже третий блог,
что с ними стало и как работает

Первый мой блог был на платформе аналог ЖЖ и блогспот, найти его заного я так и не сумел.
сьехал я с него по причине не возможности редактировать шаблон блога. (За денежку конечно можно было вставлять кастомный шаблон)

Второй блог, я как настоящий программист решил написать сам. Взял в руки бутсрап, тогда только вышедшая вторая версия, и начал писать его на пхп с мускулом
Где то год он провисел в сети, вскоре закончился хостинг с доменом и все статью канули в пропасть 
После это дело я быстро забросил, как и в последующим сам пхп

И вот сегодня третья реанкорнация этого блога.
На этот раз всё по фуншую. Мои любимый питон, хостится все на GitHub Pages, генератор статики Pelican

Просто покажу фаил requirements.txt 

``` 
asn1crypto==0.23.0
bcrypt==3.1.4
blinker==1.4
cffi==1.11.2
cryptography==2.1.3
docutils==0.14
Fabric3==1.13.1.post1
feedgenerator==1.9
idna==2.6
Jinja2==2.10
Markdown==2.6.9
MarkupSafe==1.0
paramiko==2.4.0
pelican==3.7.1
pyasn1==0.3.7
pycparser==2.18
Pygments==2.2.0
PyNaCl==1.2.0
python-dateutil==2.6.1
pytz==2017.3
six==1.11.0
Unidecode==0.4.21
```
 
---
###Почему Pelican?
Потому, что Питон) на этом всё


---
####Пометка для себя  по Markdown

---

# h1 Heading 8-)
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


## Horizontal Rules

***

## Typographic replacements

Enable typographer option to see result.

(c) (C) (r) (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,,  -- ---

"Smartypants, double quotes" and 'single quotes'


## Emphasis

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~


## Blockquotes


> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.


## Lists

Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar


## Code

Inline `code`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


Block code "fences"

```
Sample text here...
```

Syntax highlighting

``` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

## Tables

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Right aligned columns

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


## Links

[link text](http://dev.nodeca.com)

[link with title](http://nodeca.github.io/pica/demo/ "title text!")

Autoconverted link https://github.com/nodeca/pica (enable linkify to see)


## Images

![Minion](https://octodex.github.com/images/minion.png)
![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

![Alt text][id]

With a reference later in the document defining the URL location:

[id]: https://octodex.github.com/images/dojocat.jpg  "The Dojocat"


## Plugins

The killer feature of `markdown-it` is very effective support of
[syntax plugins](https://www.npmjs.org/browse/keyword/markdown-it-plugin).


### [Emojies](https://github.com/markdown-it/markdown-it-emoji)

> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:
>
> Shortcuts (emoticons): :-) :-( 8-) ;)

see [how to change output](https://github.com/markdown-it/markdown-it-emoji#change-output) with twemoji.


### [Subscript](https://github.com/markdown-it/markdown-it-sub) / [Superscript](https://github.com/markdown-it/markdown-it-sup)

- 19^th^
- H~2~O


### [\<ins>](https://github.com/markdown-it/markdown-it-ins)

++Inserted text++


### [\<mark>](https://github.com/markdown-it/markdown-it-mark)

==Marked text==


### [Footnotes](https://github.com/markdown-it/markdown-it-footnote)

Footnote 1 link[^first].

Footnote 2 link[^second].

Inline footnote^[Text of inline footnote] definition.

Duplicated footnote reference[^second].

[^first]: Footnote **can have markup**

    and multiple paragraphs.

[^second]: Footnote text.


### [Definition lists](https://github.com/markdown-it/markdown-it-deflist)

Term 1

:   Definition 1
with lazy continuation.

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

_Compact style:_

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b


### [Abbreviations](https://github.com/markdown-it/markdown-it-abbr)

This is HTML abbreviation example.

It converts "HTML", but keep intact partial entries like "xxxHTMLyyy" and so on.

*[HTML]: Hyper Text Markup Language

### [Custom containers](https://github.com/markdown-it/markdown-it-container)

::: warning
*here be dragons*
:::