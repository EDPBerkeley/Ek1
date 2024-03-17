import base64
from mongoengine import *
from bson.objectid import ObjectId

from models.one_image import OneImage


class CustomSerializer:
    @staticmethod
    def to_json(data, resolve_images=False):

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
            elif isinstance(obj, OneImage):
                return CustomSerializer.resolve_image(obj, resolve_image=resolve_images)
            elif isinstance(obj, Document) or isinstance(obj, EmbeddedDocument):
                return resolve_object_ids(dict(obj._data))
            else:
                return obj

        return resolve_object_ids(data)

    @staticmethod
    def resolve_image(obj: OneImage, resolve_image=False):
        if resolve_image is True:
            obj["element"].seek(0)
            return {
                "url": obj["url"],
                "element": base64.b64encode(obj["element"].read()).decode('utf-8')
            }
        else:
            return {"id": str(obj["id"])}
