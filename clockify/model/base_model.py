from datetime import datetime
from pydantic import ConfigDict, BaseModel


class BaseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    def json_dict(self, **kwargs):
        """
        Parse dict so that it can be json serialized by Python's json module
        """
        d = super().model_dump(exclude_unset=True, by_alias=True, **kwargs)
        for k, v in d.items():
            if isinstance(v, datetime):
                d[k] = v.isoformat()[:19] + "Z"
        return d
