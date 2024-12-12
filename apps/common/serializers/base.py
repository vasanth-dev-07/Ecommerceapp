from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from apps.common.config import CUSTOM_ERRORS_MESSAGES


class CustomMessageMixin:

    def get_display(self,field_name):
        return field_name.replace('_', " ")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field_name, field in getattr(self,"fields",{}).items:
            if field.__class__.__name__ == 'ManyRelatedField':
                field.error_messages.update(
                    CUSTOM_ERRORS_MESSAGES["ManyRelatedField"])
                field.child_relation.error_message.update(
                    CUSTOM_ERRORS_MESSAGES["PrimaryKeyRelatedField"])
            elif field.__class__.__name__ == 'PrimaryRelatedField':
                field.error_messages.update(
                    CUSTOM_ERRORS_MESSAGES["PrimaryKeyRelatedField"])
            else:
                field.error_messages.update({
                    "blank":f'please enter {self.get_display(field_name)}',
                    "null":f'please enter{self.get_display(field_name)}'
                }
            )