"""
Definition of the :class:`UnlimitedText` model.
"""
from django.db import models
from django_dicom.models.values.data_element_value import DataElementValue


class UnlimitedText(DataElementValue):
    """
    A :class:`~django.db.models.Model` representing a single *Unknown* data
    element value.
    """

    value = models.TextField(blank=True, null=True)
    """
    Overrides
    :attr:`~django_dicom.models.values.data_element_value.DataElementValue.value`
    to assign a :class:`~django.db.models.TextField`.
    """

    raw = models.TextField(blank=True, null=True)
    """
    Overrides
    :attr:`~django_dicom.models.values.data_element_value.DataElementValue.raw`
    to assign a :class:`~django.db.models.TextField`.
    """
