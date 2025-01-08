from typing import List, Optional
from typing_extensions import Literal
from pydantic import Field

from clockify.model.base_model import BaseModel
from clockify.model._rates import CostRate_HourlyRate


class Task(BaseModel):
    id_: str = Field(default=None, alias='id')
    name: str
    project_id: str = Field(alias='projectId')
    assignee_ids: List[str] = Field(default=[], alias='assigneIds')
    estimate: str = None
    billable: bool = None
    hourly_rate: Optional[CostRate_HourlyRate] = Field(default=None, alias='hourlyRate')
    cost_rate: Optional[CostRate_HourlyRate] = Field(default=None, alias='costRate')
    status: Literal["ACTIVE", "DONE"] = None


class TaskGetParams(BaseModel):
    is_active: Optional[bool] = Field(default=None, alias='is-active')
    name: Optional[str] = None
    page: int = 1
    page_size: int = Field(default=50, alias='page-size')
    strict_name_search: Optional[bool] = Field(default=None, alias='strict-name-search')
    sort_column: Optional[Literal["ID", "NAME"]] = Field(default=None, alias='sort-column')
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(default=None, alias='sort-order')