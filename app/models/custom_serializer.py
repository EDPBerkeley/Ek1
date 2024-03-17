import base64
from mongoengine import *
from bson.objectid import ObjectId


class CustomSerializer:
    @staticmethod
    def to_json(data):

        # Custom logic to recursively resolve ObjectId fields
        def resolve_object_ids(obj):

            if isinstance(obj, dict):
                d = {}
                for k, v in obj.items():
                    d[k] = resolve_object_ids(v)
                return d
            elif isinstance(obj, list):
                return [resolve_object_ids(item) for item in obj]
            elif isinstance(obj, ObjectId):
                return str(obj)
            elif isinstance(obj, ImageGridFsProxy):
                obj.seek(0)
                binary_data = obj.read()
                if (base64.b64encode(binary_data).decode('utf-8') == ""):
                    print("hit")
                return base64.b64encode(binary_data).decode('utf-8')
            elif isinstance(obj, Document) or isinstance(obj, EmbeddedDocument):
                return resolve_object_ids(dict(obj._data))
            else:
                return obj

        return resolve_object_ids(data)
