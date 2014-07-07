"""Setup the SoyCorn application"""
import logging

import pylons.test

from soycorn import model
from soycorn.config.environment import load_environment
from soycorn.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Used to setup soycorn"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    log.info("Creating tables...")
    meta.metadata.create_all(bind=meta.engine)
    log.info("Successfully set up.")

    log.info("Adding front page data...")
    news = model.News(title=u'FrontPage',
                      content=u'We haz soycorn!')
    meta.Session.add(news)
    meta.Session.commit()
    log.info("Successfully set up.")
