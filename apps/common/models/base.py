import uuid
from django.db import models

COMMON_CHAR_FEILD_MAX_LENGTH = 512
COMMON_NULLABLE_FEILD_CONFIG = {
    'default':None,
    'null':True
}
COMMON_BLANK_AND_NULLABLE_FEILD_CONFIG = {
    'blank':True,
    **COMMON_NULLABLE_FEILD_CONFIG
}

class BaseModel(models.Model):

    # uuid for unique id field
    uuid = models.UUIDField(default=uuid.uuid4(),editable=False)

    # for time tracking
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

