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