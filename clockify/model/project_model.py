from typing import Optional, List
from typing_extensions import Literal

from clockify.model.base_model import BaseModel
from clockify.model._rates import CostRate_HourlyRate
from pydantic import Field

class MemberShip(BaseModel):
    user_Id: Optional[str] = Field(default=None, alias='userId')
    hourly_rate: Optional[CostRate_HourlyRate] = Field(default=None, alias='hourlyRate')
    cost_rate: Optional[CostRate_HourlyRate] = Field(default=None, alias='costRate')
    target_Id: Optional[str] = Field(default=None, alias='targetId')
    membership_Type: Optional[str] = Field(default=None, alias='membershipType')
    membership_Status: Optional[str] = Field(default=None, alias='membershipStatus')


class Estimate(BaseModel):
    estimate: Optional[str] = None
    type: Optional[str] = None


class TimeEstimate(BaseModel):
    estimate: Optional[str] = None
    type: Optional[str] = None
    reset_option: Optional[str] = Field(default=None, alias='resetOption')
    active: Optional[bool] = None
    include_non_billable: Optional[bool] = Field(default=None, alias='includeNonBillable')


class Project(BaseModel):
    name: str
    workspace_id: str = Field(alias='workspaceId')
    id_: Optional[str] = Field(default=None, alias='id')
    hourly_rate: Optional[CostRate_HourlyRate] = Field(default=None, alias='hourlyRate')
    client_id: Optional[str] = Field(default=None, alias='clientId')
    billable: Optional[bool] = None
    memberships: Optional[List[MemberShip]] = None
    color: Optional[str] = None
    estimate: Optional[Estimate] = None
    archived: Optional[bool] = None
    duration: Optional[str] = None
    client_name: Optional[str] = Field(default=None, alias='clientName')
    note: Optional[str] = None
    cost_rate: Optional[CostRate_HourlyRate] = Field(default=None, alias='costRate')
    time_estimate: Optional[TimeEstimate] = Field(default=None, alias='timeEstimate')
    budget_estimate: Optional[str] = Field(default=None, alias='budgetEstimate')
    template: Optional[bool] = None
    public_: Optional[bool] = Field(default=None, alias='public')


class ProjectGetParams(BaseModel):
    hydrated: Optional[bool] = None
    archived: Optional[bool] = None
    name: Optional[str] = None
    page: int = 1
    page_size: int = Field(default=50, alias='page-size')
    billable: Optional[bool] = None
    clients: Optional[List[str]] = None
    contains_client: Optional[bool] = Field(default=None, alias='contains-client')
    client_status: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(default=None, alias='client-status')
    users: Optional[List[str]] = None
    contains_users: Optional[bool] = Field(default=None, alias='contains-users')
    user_status: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(default=None, alias='user-status')
    is_template: Optional[bool] = Field(default=None, alias='is-template')
    sort_column: Optional[Literal["NAME", "CLIENT_NAME", "DURATION"]] = Field(default=None, alias='sort-column')
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(default=None, alias='sort-order')
