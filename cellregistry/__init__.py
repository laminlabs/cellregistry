"""A registry for single cells [`source <https://github.com/laminlabs/cellregistry/blob/main/cellregistry/models.py>`__].

Install and mount `cellregistry` in a new instance:

>>> pip install cellregistry
>>> lamin init --storage ./test-cellregistry --schema bionty,cellregistry

Import the package:

>> import cellregistry as creg

The `Cell` registry:

.. autosummary::
   :toctree: .

    Cell
"""

__version__ = "0.1.0"  # denote a pre-release for 0.1.0 with 0.1rc1

from lamindb_setup import _check_instance_setup


def __getattr__(name):
    if name != "models":
        _check_instance_setup(from_module="cellregistry")
    return globals()[name]


if _check_instance_setup():
    import lamindb

    del __getattr__  # delete so that imports work out
    from .models import Cell
