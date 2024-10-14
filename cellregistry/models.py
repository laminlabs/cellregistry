from __future__ import annotations

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
)


class Cell(Record, CanValidate, TracksRun, TracksUpdates):
    """References.

    Example:
        >>> cell = Cell(
        ...     name="A paper title",
        ... ).save()
    """

    class Meta(Record.Meta, TracksRun.Meta, TracksUpdates.Meta):
        abstract = False

    id: int = models.BigAutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid: str = models.CharField(unique=True, max_length=12, default=ids.base62_12)
    """Universal id, valid across DB instances."""
    name: str = models.CharField(max_length=255, default=None, db_index=True)
    """A name for the cell."""
    artifacts: Artifact = models.ManyToManyField(
        Artifact, through="ArtifactReference", related_name="references"
    )
    """Artifacts labeled with this reference."""


class ArtifactCell(Record, LinkORM, TracksRun):
    id: int = models.BigAutoField(primary_key=True)
    artifact: Artifact = models.ForeignKey(Artifact, CASCADE, related_name="links_cell")
    cell: Cell = models.ForeignKey(Cell, CASCADE, related_name="links_artifact")
