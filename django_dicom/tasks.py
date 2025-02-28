import math
from typing import Iterable, Union
from datetime import datetime

from celery import group, shared_task

from django_dicom.models.image import Image


@shared_task(name="django_dicom.import-data")
def import_data(path: Union[str, Iterable[str]], max_parallel: int = 5, today_only: bool = False):
    """
    Imports new data (unfamiliar subdirectories) from the provided path.

    Parameters
    ----------
    data_directory : Union[int, str, Path]
        Directory path or DataDirectory instance ID
    today_only : bool
        Whether to look for a '<year>/<month>/<day>' subdirectory to import,
        default is False

    Returns
    -------
    list
        The names of the subdirectories within the DataDirectory that were
        imported
    """
    if isinstance(path, (str, Path)):
        if today_only:
            today = datetime.today()
            path = (
                Path(path)
                / str(today.year)
                / str(today.month)
                / str(today.day)
            )
        try:
            return Image.objects.import_path(path, pattern="*")
        except Exception:
            pass
    else:
        try:
            # Calculate the number of chunks according to the analysis
            # version's *max_parallel* attribute.
            n_chunks = math.ceil(len(path) / max_parallel)
        except ZeroDivisionError:
            # If `max_parallel` is set to 0, run all in parallel.
            return group(import_data.s(p) for p in path)()
        else:
            return import_data.chunks(((p,) for p in path), n_chunks)()
