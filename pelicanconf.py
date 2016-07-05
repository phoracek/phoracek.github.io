# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = u'Petr Horáček &middot; blog'
SITEURL = '/'
AUTHOR = u'Petr Horáček'
AUTHOR_DESCRIPTION = (
    u'<p><b>Petr Horáček</b> is a guy from Czech Republic, studying at '
    '<a href="http://fi.muni.cz/">FI MUNI</a>, working in '
    '<a href="http://redhat.com">Red Hat</a> on networking part of '
    '<a href="http://www.ovirt.org/">oVirt</a>.<br>He likes programming, '
    'Linux, travelling, livecoding, music, multimedia.</p>')
AUTHOR_DESCRIPTION_PLAIN = (
    u'Petr Horáček is a guy from Czech Republic, studying at FI MUNI, working '
    'in Red Hat on networking part of oVirt. He likes programming, Linux, '
    'travelling, livecoding, music, multimedia.')
AUTHOR_CONTACT = (u'<p>p.horacek94 at gmail dot com<br>'
                  'phoracek at irc.oftc.net #ovirt<br>'
                  '<a href="http://www.github.com/phoracek">'
                  'www.github.com/phoracek</a></p>')


TIMEZONE = 'Europe/Prague'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%d. %m. %Y'

PLUGIN_PATH = 'plugins'
PLUGINS = ['lightbox']

PATH = 'content'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = ('index', 'tag', 'category', 'period_archives')
PAGINATED_DIRECT_TEMPLATES = ('index', 'tag', 'category', 'period_archives')

DEFAULT_CATEGORY = 'Misc'

FILENAME_METADATA = '(?P<date>\d{4}\d{2}\d{2})_(?P<slug>[^_]*)'

ARTICLE_SAVE_AS = 'articles/{category}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{category}/{slug}-{lang}.html'
ARTICLE_URL = 'articles/{category}/{slug}-{lang}.html'
ARTICLE_LANG_URL = 'articles/{category}/{slug}-{lang}.html'

YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}.html'
ARCHIVES_YEARS = [2015]

AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
