
import ckan.plugins as p
import datetime as datetime
from logging import getLogger
from ckanext.dga_stats.views import get_blueprints

log = getLogger(__name__)


def date_range():
    return list(reversed(list(range(2013, datetime.datetime.now().year + 1))))


class StatsPlugin(p.SingletonPlugin):
    """Stats plugin."""

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)
    p.implements(p.IBlueprint)

    # ITemplateHelpers

    def get_helpers(self):
        """Register the most_popular_groups() function above as a template
        helper function.

        """
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {"date_range": date_range}

    # IConfigurer

    def update_config(self, config):
        p.toolkit.add_template_directory(config, "../templates")
        p.toolkit.add_public_directory(config, "../public")
        p.toolkit.add_resource("../public/ckanext/stats", "ckanext_dga_stats")

    # IBlueprint

    def get_blueprint(self):
        return get_blueprints()
