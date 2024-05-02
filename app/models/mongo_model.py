import bson.objectid
from pydantic import BaseModel, ValidationInfo

import datetime
from bson.objectid import ObjectId


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, validation_info: ValidationInfo):
        try:
            return ObjectId(str(v))
        except:
            raise ValueError("Not a valid ObjectId")


def convert(oid):
    return str(oid)


class MongoModel(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime.datetime: lambda dt: dt.isoformat(),
            bson.objectid.ObjectId: convert,
        }

    @classmethod
    def from_mongo(cls, data: dict):
        """We must convert _id into "id". """
        if not data:
            return data
        id = data.pop('_id', None)
        k = dict(data, id=str(id))
        return k

    def to_mongo(self, **kwargs):
        exclude_unset = kwargs.pop('exclude_unset', True)
        by_alias = kwargs.pop('by_alias', True)

        parsed = self.dict(
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

        # Mongo uses `_id` as default key. We should stick to that as well.
        if '_id' not in parsed and 'id' in parsed:
            parsed['_id'] = parsed.pop('id')

        return parsed
