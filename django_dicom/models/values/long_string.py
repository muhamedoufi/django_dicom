from django.db import models
from django_dicom.models.values.data_element_value import DataElementValue


class LongString(DataElementValue):
    value = models.CharField(max_length=64, blank=True, null=True)
    raw = models.CharField(max_length=64, blank=True, null=True)
