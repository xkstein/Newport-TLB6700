#!/usr/bin/env python
##############################################################################
#
# (c) 2026 no one.
# All rights reserved.
#
# File coded by: Jamie, Claude AI.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/xkstein/newport-tlb6700/graphs/contributors  # noqa: E501
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Definition of __version__."""

#  We do not use the other three variables, but can be added back if needed.
#  __all__ = ["__date__", "__git_commit__", "__timestamp__", "__version__"]

# obtain version information
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("newport_tlb6700")
except PackageNotFoundError:
    __version__ = "unknown"
