"""A registry for single cells [`source <https://github.com/laminlabs/cellregistry/blob/main/cellregistry/models.py>`__].

This schema module provides a single registry `Reference` to store references to studies, reports, papers, blog posts, preprints.

Install the package::

   pip install cellregistry

Import the package::

   import cellregistry as creg

The `Reference` registry:

.. autosummary::
   :toctree: .

    Reference
"""

__version__ = "0.1.0"  # denote a pre-release for 0.1.0 with 0.1rc1

from lamindb_setup import _check_instance_setup


def __getattr__(name):
    if name != "models":
        _check_instance_setup(from_module="cellregistry")
    return globals()[name]


if _check_instance_setup():
    del __getattr__  # delete so that imports work out
