"""/etc/iptables/rules.* templates tests."""

import unittest
import pathlib
import importlib.resources as resources

from ..utils import (
    relative_to_path,
    render_role_template,
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
        actual = render_role_template(
            role_path=_ROLE_PATH,
            template_filename=_TEMPLATE_FILENAME,
        )
        self.assertEqual(expect, actual)
