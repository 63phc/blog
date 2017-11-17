#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pavel burns'
SITENAME = 'pavel burns'
SITESUBTITLE = 'tech blog'
SITEURL = ''

PATH = 'content'
# STATIC_PATHS = ['blog', 'downloads']
# ARTICLE_PATHS = ['blog']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Europe/Moscow'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/63phc'),
          ('github', 'https://github.com/63phc'),
          ('facebook', 'https://facebook.com/63phc'),
          ('envelope', 'mailto:pavel.burns@gmail.com'))

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# THEME ATTILA CONF
COLOR_SCHEME_CSS = 'monokai.css'

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

AUTHORS_BIO = {
  "pavel burns": {
    "name": "Pavel Burns",
    "cover": "https://github.com/63phc/blog/blob/gh-pages/assets/img/ava.jpg",
    "image": "https://github.com/63phc/blog/blob/gh-pages/assets/img/ava.jpg",
    "website": "http://blog.pavelburns.ru",
    "location": "Russian",
    "bio": "Пишу код во всех точках мира, работаю на фрилансе в команде NoNameDreamTeam"
  }
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Comments
DISQUS_SITENAME = "63phc"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-12"

# END THEME ATTILA CONF

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# NEW SETTINGS http://docs.getpelican.com/en/3.6.3/settings.html

# Status: published -> default draft | The default metadata you want to use for all articles and pages.
# DEFAULT_METADATA = {
#     'status': 'draft',
# }

# If you manage multiple languages, you can set the date formatting here.
# See the “Date format and locale” section below for details.
# DATE_FORMATS = {}

# USE_FOLDER_AS_CATEGORY = True
# DEFAULT_CATEGORY = 'misc'

# DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True

# Where to output the generated files.
# OUTPUT_PATH = 'output/'

# http://docs.getpelican.com/en/3.6.3/plugins.html#plugins
# PLUGINS = []
# PLUGIN_PATHS = []

# http://docs.getpelican.com/en/3.6.3/settings.html#template-pages
# TEMPLATE_PAGES = None

# STATIC_PATHS = ['images']

# DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

# Setting to None will cause the summary to be a copy of the original content.
# SUMMARY_MAX_LENGTH = 50

# If disabled, content with dates in the future will get a default status of draft.
# WITH_FUTURE_DATES = True

# If True, saves content in caches. See Reading only modified content for details about caching.
# CACHE_CONTENT = False
# CACHE_PATH = 'cache'

# The URL to refer to an article.
# ARTICLE_URL = '{slug}.html'
# The place where we will save an article.
# ARTICLE_SAVE_AS = '{slug}.html'
# The URL to refer to an article which doesn’t use the default language.
# ARTICLE_LANG_URL = '{slug}-{lang}.html'
# The place where we will save an article which doesn’t use the default language.
# ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
# The URL to refer to an article draft.
# DRAFT_URL = 'drafts/{slug}.html'
# The place where we will save an article draft.
# DRAFT_SAVE_AS = 'drafts/{slug}.html'
# The URL to refer to an article draft which doesn’t use the default language.
# DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
# The place where we will save an article draft which doesn’t use the default language.
# DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
# The URL we will use to link to a page.
# PAGE_URL = 'pages/{slug}.html'
# The location we will save the page.
# This value has to be the same as PAGE_URL or you need to use a rewrite in your server config.
# PAGE_SAVE_AS = 'pages/{slug}.html'
# The URL we will use to link to a page which doesn’t use the default language.
# PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
# The location we will save the page which doesn’t use the default language.
# PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
# CATEGORY_URL = 'category/{slug}.html'	The URL to use for a category.
# CATEGORY_SAVE_AS = 'category/{slug}.html'	The location to save a category.
# TAG_URL = 'tag/{slug}.html'	The URL to use for a tag.
# TAG_SAVE_AS = 'tag/{slug}.html'	The location to save the tag page.
# AUTHOR_URL = 'author/{slug}.html'	The URL to use for an author.
# AUTHOR_SAVE_AS = 'author/{slug}.html'	The location to save an author.
# YEAR_ARCHIVE_SAVE_AS = ''	The location to save per-year archives of your posts.
# MONTH_ARCHIVE_SAVE_AS = ''	The location to save per-month archives of your posts.
# DAY_ARCHIVE_SAVE_AS = ''	The location to save per-day archives of your posts.
# SLUG_SUBSTITUTIONS = ()	Substitutions to make prior to stripping out non-alphanumerics when generating slugs.
# Specified as a list of 2-tuples of (from, to) which are applied in order.


THEME = 'themes/attila'


















