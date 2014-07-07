"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from soycorn.model import meta
import logging
import re
import sets
from docutils.core import publish_parts

from pylons import url
from soycorn.lib.helpers import link_to
from soycorn.model import meta

log = logging.getLogger(__name__)

# disable docutils security hazards:
# http://docutils.sourceforge.net/docs/howto/security.html
SAFE_DOCUTILS = dict(file_insertion_enabled=False, raw_enabled=False)
wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)", re.UNICODE)


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine

news_table = sa.Table('news', meta.metadata,
                sa.Column('title', sa.types.Unicode(40), primary_key=True),
                sa.Column('content', sa.types.Unicode(), default=''))

class News(object):

    def __init__(self, title, content=None):
        self.title = title
        self.content = content
    
    def get_content(self):
        """Convert reStructuredText content to HTML for display, and
        create links for WikiWords
        """
        content = publish_parts(self.content, writer_name='html',
                                settings_overrides=SAFE_DOCUTILS)['html_body']
        return content


    def __unicode__(self):
        return self.title

    __str__ = __unicode__

orm.mapper(News, news_table)
