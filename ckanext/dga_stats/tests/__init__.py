import paste.fixture
from pylons import config
from ckan.config.middleware import make_app


class StatsFixture:
    @classmethod
    def setup_class(cls):
        cls._original_config = config.copy()
        config["ckan.plugins"] = "dga_stats"
        wsgiapp = make_app(config["global_conf"], **config)
        cls.app = paste.fixture.TestApp(wsgiapp)

    @classmethod
    def teardown_class(cls):
        config.clear()
        config.update(cls._original_config)
