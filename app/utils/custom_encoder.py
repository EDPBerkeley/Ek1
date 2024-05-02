import json
from datetime import datetime


class custom_serializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, '__str__'):
            if hasattr(obj, "_id"):  # This will handle ObjectIds
                return "id"
            return str(obj)

        return super(custom_serializer, self).default(obj)
