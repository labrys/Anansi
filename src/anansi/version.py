"""Module to construct version."""

import logging
import os

import setuptools_scm
from pkg_resources import (
    get_distribution,
    DistributionNotFound,
    RequirementParseError,
)

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def get_version():
    """Get the installed version or the scm version if running from source."""
    version = None
    try:
        version = get_distribution(__name__).version
    except (DistributionNotFound, RequirementParseError):
        log.warning('Could not get version from installation.')
        relative_root = '../..'
        here = os.path.dirname(__file__)
        root = os.path.join(here, relative_root)
        absolute_root = os.path.abspath(root)
        return setuptools_scm.get_version(absolute_root)
