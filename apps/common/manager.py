from django.db.models import QuerySet
from django.core.exceptions import (
    ObjectDoesNotExist,
    ValidationError,
    MultipleObjectsReturned,
)






class BaseObjectManagerQuerySet(QuerySet):
    """
       The main/base manager for the apps models. This is used for including common
        model filters and methods. This is used just to make things DRY.

        This can be used in both ways:
            1. Model.app_objects.custom_method()
            2. Model.app_objects.filter().custom_method()
    """
    def get_or_none(self, *args, **kwargs):

        """
            Get the object based on the given **kwargs. If not present returns None.
            Note: Expects a single instance.
        """

        try:
            return self.get(*args, **kwargs)

        except (
                ObjectDoesNotExist,
                AttributeError,
                ValueError,
                MultipleObjectsReturned,
                ValidationError,
        ):
            return None


