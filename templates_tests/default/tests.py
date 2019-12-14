"""/etc/iptables/rules.* templates tests."""

import unittest
import pathlib
try:
    import importlib.resources as resources
except ImportError:
    import importlib_resources as resources

from ..utils import (
    relative_to_path,
    render_role_template,
    yaml_parse,
)


_ROLE_PATH = relative_to_path(
    base_path=pathlib.Path(__file__),
    relative_path=pathlib.Path("..", ".."),
)
_TEMPLATE_FILENAME = "rules.v4.j2"


class DefaultRules(unittest.TestCase):
    """Test default rules."""

    def test(self):
        """Run test."""
        expect = resources.read_text(
            package=__package__,
            resource="rules.v4",
        )
        variables = None
        if resources.is_resource(package=__package__, name="vars.yml"):
            variables = yaml_parse(
                data=resources.read_text(
                    package=__package__,
                    resource="vars.yml",
                ),
            )
        actual = render_role_template(
            role_path=_ROLE_PATH,
            template_filename=_TEMPLATE_FILENAME,
            variables=variables,
        )
        self.assertEqual(expect, actual)
