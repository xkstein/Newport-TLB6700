|Icon| |title|_
===============

.. |title| replace:: newport-tlb6700
.. _title: https://xkstein.github.io/newport-tlb6700

.. |Icon| image:: https://avatars.githubusercontent.com/xkstein
        :target: https://xkstein.github.io/newport-tlb6700
        :height: 100px

|PyPI| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/xkstein/newport-tlb6700/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/xkstein/newport-tlb6700/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/xkstein/newport-tlb6700/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/xkstein/newport-tlb6700

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/newport-tlb6700
        :target: https://anaconda.org/conda-forge/newport-tlb6700

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff
        :target: https://github.com/xkstein/newport-tlb6700/pulls

.. |PyPI| image:: https://img.shields.io/pypi/v/newport-tlb6700
        :target: https://pypi.org/project/newport-tlb6700/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/newport-tlb6700
        :target: https://pypi.org/project/newport-tlb6700/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/xkstein/newport-tlb6700/issues

Unofficial Newport Velocity TLB6700 tunable laser python driver

For more information about the newport-tlb6700 library, please consult our `online documentation <https://xkstein.github.io/newport-tlb6700>`_.

Installation
------------

To install using ``pip`` into your ``newport-tlb6700_env`` environment, type ::

        pip install newport-tlb6700

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/xkstein/newport-tlb6700/>`_. Once installed, ``cd`` into your ``newport-tlb6700`` directory
and run the following ::

        pip install .

This package also provides command-line utilities. To check the software has been installed correctly, type ::

        newport-tlb6700 --version

You can also type the following command to verify the installation. ::

        python -c "import newport_tlb6700; print(newport_tlb6700.__version__)"


To view the basic usage and available commands, type ::

        newport-tlb6700 -h

TO DO
---------------

* Read until (allows for smaller chunks and faster queries)
* Get on pypi
* Add example scripts

Acknowledgements
----------------

``newport-tlb6700`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.
