"""
Definition of the :class:`CodeString` model.
"""
from django.db import models
from django_dicom.models.values.data_element_value import DataElementValue


class CodeString(DataElementValue):
    """
    A :class:`~django.db.models.Model` representing a single *CodeString* data
    element value.
    """

    value = models.CharField(max_length=16, blank=True, null=True)
    """
    Overrides
    :attr:`~django_dicom.models.values.data_element_value.DataElementValue.value`
    to assign a :class:`~django.db.models.CharField`.
    """

    raw = models.CharField(max_length=16, blank=True, null=True)
    """
    Overrides
    :attr:`~django_dicom.models.values.data_element_value.DataElementValue.raw`
    to assign a :class:`~django.db.models.CharField`.
    """
