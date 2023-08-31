from datetime import date


AUTHOR = "Ivan Kojic"
SITENAME = "SoftyTech"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ["blog"]
ARTICLE_SAVE_AS = "{date:%Y}/{slug}.html"
ARTICLE_URL = "{date:%Y}/{slug}.html"
PAGE_PATHS = ["pages"]

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "English"

THEME = "softyTechTheme"

DISQUS_SITENAME = "softytech"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = (("Home", "/"),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
