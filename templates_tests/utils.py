"""Utilities."""

import pathlib
import pkg_resources

import jinja2
import ansible.plugins.filter.core
import yaml


def relative_to_path(base_path, relative_path):
    """Resolve path relative to base path."""
    if not base_path.is_dir():
        base_path = base_path.parent
    return base_path.joinpath(relative_path).resolve()


def render_role_template(role_path, template_filename, variables_path=None):
    """Render file from Ansible role template."""
    variables = {}
    default_variables_path = pathlib.Path(role_path, "defaults", "main.yml")
    if default_variables_path.exists():
        variables.update(
            yaml_parse(data=default_variables_path.read_text()),
        )
    if variables_path is not None:
        variables.update(
            yaml_parse(data=variables_path.read_text()),
        )
    env = _make_template_env(
        search_path=pathlib.Path(role_path, "templates"),
    )
    template = env.get_template(name=template_filename)
    return template.render(**variables)


def _make_template_env(search_path):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            searchpath=str(search_path),
        ),
        keep_trailing_newline=True,
        lstrip_blocks=True,
        trim_blocks=True,
    )
    env.filters.update(ansible.plugins.filter.core.FilterModule().filters())
    return env


def resource_abs_path(resource_path, package=None):
    """Get resource absolute path."""
    return _ResourcePathContextManager(resource_path, package)


def resource_bytes(resource_path, package=None):
    """Get raw content of resource."""
    if package is None:
        package = __name__
    return pkg_resources.resource_string(
        package_or_requirement=package,
        resource_name=str(pathlib.Path("data", resource_path))
    )


def resource_str(resource_path, package=None):
    """Get content of UTF-8 encoded resource."""
    return resource_bytes(resource_path, package).decode()


def resource_yaml(resource_path, package=None):
    """Get content of YAML formatted resource."""
    return yaml_parse(data=resource_str(resource_path, package))


def yaml_parse(data):
    """Parse YAML data."""
    return yaml.load(
        stream=data,
        Loader=yaml.Loader
    )


class _ResourcePathContextManager:

    def __init__(self, resource_path, package=None):
        if package is None:
            package = __name__
        self._package = package
        self._resource_path = resource_path

    def __enter__(self):
        return pathlib.Path(
            pkg_resources.resource_filename(
                package_or_requirement=self._package,
                resource_name=str(pathlib.Path("data", self._resource_path)),
            ),
        )

    def __exit__(self, exc_type, exc_value, traceback):
        pkg_resources.cleanup_resources()
