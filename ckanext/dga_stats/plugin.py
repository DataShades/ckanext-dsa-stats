from __future__ import annotations

import ckan.plugins as p
import ckan.plugins.toolkit as tk
import datetime as datetime
import logging

log = logging.getLogger(__name__)


def date_range():
    return list(reversed(list(range(2013, datetime.datetime.now().year + 1))))


@tk.blanket.blueprints
class StatsPlugin(p.SingletonPlugin):
    """Stats plugin."""

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)

    # ITemplateHelpers
    def get_helpers(self):
        return {"date_range": date_range}

    # IConfigurer

    def update_config(self, config):
        p.toolkit.add_template_directory(config, "templates")
        p.toolkit.add_public_directory(config, "public")
        p.toolkit.add_resource("public/ckanext/stats", "ckanext_dga_stats")
