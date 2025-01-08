from typing import Optional
from pydantic import Field

from clockify.model.base_model import BaseModel


class Tag(BaseModel):
    id_: str = Field(default=None, alias='id')
    name: str
    workspace_id: str = Field(alias='workspaceId')
    archived: bool = False


class TagGetParams(BaseModel):
    name: Optional[str] = None
    archived: Optional[bool] = None
    page: int = 1
    page_size: int = Field(default=50, alias='page-size')
