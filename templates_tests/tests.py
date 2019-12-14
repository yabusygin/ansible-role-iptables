"""/etc/iptables/rules.* templates tests."""

import unittest
import pathlib

from .utils import (
    relative_to_path,
    render_role_template,
    resource_abs_path,
    resource_str,
)


_ROLE_PATH = relative_to_path(
    base_path=pathlib.Path(__file__),
    relative_path=pathlib.Path(".."),
)
_TEMPLATE_FILENAME = "rules.v4.j2"


class AcceptAllRules(unittest.TestCase):
    """Test rules accepting all packets."""

    def test(self):
        """Run test."""
        expect = resource_str(
            resource_path=pathlib.Path("accept-all", "rules.v4"),
            package=__name__,
        )
        context_manager = resource_abs_path(
            resource_path=pathlib.Path("accept-all", "vars.yml"),
            package=__name__,
        )
        with context_manager as variables_path:
            actual = render_role_template(
                role_path=_ROLE_PATH,
                template_filename=_TEMPLATE_FILENAME,
                variables_path=variables_path,
            )
        self.assertEqual(expect, actual)


class CustomizedDefaultPolicies(unittest.TestCase):
    """Test customized default policies."""

    def test(self):
        """Run test."""
        expect = resource_str(
            resource_path=pathlib.Path("custom-policy", "rules.v4"),
            package=__name__,
        )
        context_manager = resource_abs_path(
            resource_path=pathlib.Path("custom-policy", "vars.yml"),
            package=__name__,
        )
        with context_manager as variables_path:
            actual = render_role_template(
                role_path=_ROLE_PATH,
                template_filename=_TEMPLATE_FILENAME,
                variables_path=variables_path,
            )
        self.assertEqual(expect, actual)
