from typing_extensions import Literal

from clockify.model.base_model import BaseModel
from pydantic import Field


class Client(BaseModel):
    id_: str = Field(default=None, alias='id')
    name: str
    workspace_id: str = Field(alias='workspaceId')
    archived: bool = False


class ClientGetParams(BaseModel):
    archived: bool = None
    name: str = None
    page: int = 1
    page_size: int = Field(default=50, alias='page-size')
    sort_column: Literal["NAME"] = Field(default=None, alias='sort-column')
    sort_order: Literal["ASCENDING", "DESCENDING"] = Field(default=None, alias='sort-order')


class ClientUpdateParams(BaseModel):
    archive_projects: bool = Field(default=None, alias='archive-projects')
