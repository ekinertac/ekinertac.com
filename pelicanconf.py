#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Ekin Ertaç'
SITENAME = u'/bin/blog/ekinertac'
SITEURL = 'http://ekinertac.com'
TIMEZONE = 'Europe/Istanbul'
THEME = "pelican-octopress-theme"
DEFAULT_LANG = u'tr'

STATIC_PATHS = ['images', ]

MD_EXTENSIONS = [
    # 'toc',
    'codehilite',
    'attr_list',
    'headerid',
    'nl2br',
    'def_list',
    'fenced_code',
    'footnotes',
]

DISQUS_SITENAME = "ekinertac-pelican"
GOOGLE_ANALYTICS = "UA-9694343-1"

# Blogroll
LINKS =  (
#    (u'Fatih Erikli', 'http://fatiherikli.com'),
#    (u'Olgay Sezgin', 'http://olgaysezgin.com'),
#    (u'Yaşar İçli', 'http://yasaricli.com'),
#    (u'Erdem Özkol', 'http://erdemozkol.com'),
)

# Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/ekinertac'),
    ('github', 'http://github.com/ekinertac'),
    ('linkedin', 'http://tr.linkedin.com/in/ekinertac'),
)

DEFAULT_PAGINATION = 10
TWITTER_USERNAME = 'ekinertac'
