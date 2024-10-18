from __future__ import annotations

from bionty.models import CellType
from django.db import models
from django.db.models import CASCADE, PROTECT
from lnschema_core import ids
from lnschema_core.models import (
    Artifact,
    CanValidate,
    Feature,
    LinkORM,
    Record,
    TracksRun,
    TracksUpdates,
    ULabel,
)


class Cell(Record, CanValidate, TracksRun, TracksUpdates):
    """Single cells.

    Example:
        >>> cell = Cell(
        ...     name="A paper title",
        ... ).save()
    """

    class Meta(Record.Meta, TracksRun.Meta, TracksUpdates.Meta):
        abstract = False

    id: int = models.BigAutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid: str = models.CharField(unique=True, max_length=20, default=ids.base62_20)
    """Universal id, valid across DB instances."""
    name: str = models.CharField(
        max_length=255, default=None, unique=True, db_index=True
    )
    """A unique name for the cell.

    It's typically the barcode combined with an identifier for the dataset that
    first measured the cell.

    For example::

        xJkeL0OxEFIpvGWKdpne_AGTGTTGTCCGAGCTG
        CZINY-0109_CTGGTCTAGTCTGTAC
        Pan_T7935494_ATCATGGTCTACCTGC

    """
    description: str = models.CharField(
        max_length=255, db_index=True, null=True, default=None
    )
    """A description."""
    # ulabels: ULabel = models.ManyToManyField(
    #     ULabel, through="CellULabel", related_name="cells"
    # )
    # """Cell type labels for this cell."""
    # cell_types: CellType = models.ManyToManyField(
    #     CellType, through="CellCellType", related_name="cells"
    # )
    # """Cell type labels for this cell."""
    # artifacts: Artifact = models.ManyToManyField(
    #     Artifact, through="ArtifactCell", related_name="cells"
    # )
    # """Artifacts that measured this cell."""


class ArtifactCell(Record, LinkORM, TracksRun):
    id: int = models.BigAutoField(primary_key=True)
    artifact: Artifact = models.ForeignKey(Artifact, CASCADE, related_name="links_cell")
    cell: Cell = models.ForeignKey(Cell, CASCADE, related_name="links_artifact")


class CellCellType:
    id: int = models.BigAutoField(primary_key=True)
    cell: Cell = models.ForeignKey(Cell, CASCADE, related_name="links_cell_type")
    # follow the .lower() convention in link models
    celltype: CellType = models.ForeignKey(CellType, PROTECT, related_name="links_cell")
    feature: Feature = models.ForeignKey(
        Feature, PROTECT, null=True, default=None, related_name="links_cellcelltype"
    )


class CellULabel:
    id: int = models.BigAutoField(primary_key=True)
    cell: Cell = models.ForeignKey(Cell, CASCADE, related_name="links_ulabel")
    ulabel: ULabel = models.ForeignKey(ULabel, PROTECT, related_name="links_cell")
    feature: Feature = models.ForeignKey(
        Feature, PROTECT, null=True, default=None, related_name="links_cellulabel"
    )
