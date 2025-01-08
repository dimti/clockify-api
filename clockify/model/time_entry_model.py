from datetime import datetime
from typing import Any, List, Optional
from pydantic import Field

from clockify.model.base_model import BaseModel
from clockify.model.user_model import User
from clockify.model.tag_model import Tag
from clockify.model.task_model import Task
from clockify.model.project_model import Project


class TimeInterval(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None


class HourlyRate(BaseModel):
    amount: Optional[float] = None
    currency: Optional[str] = None


class TimeEntry(BaseModel):
    id_: Optional[str] = Field(default=None, alias='id')
    description: str
    tags: Optional[List[Tag]] = None
    tag_ids: Optional[List[str]] = Field(default=None, alias='tagIds')
    user: Optional[User] = None
    user_id: Optional[str] = Field(default=None, alias='userId')
    billable: Optional[bool] = None
    task: Optional[Task] = None
    task_id: Optional[str] = Field(default=None, alias='taskId')
    project: Optional[Project] = None
    project_id: Optional[str] = Field(default=None, alias='projectId')
    time_interval: Optional[TimeInterval] = Field(default=None, alias='timeInterval')
    workspace_id: Optional[str] = Field(default=None, alias='workspaceId')
    hourly_rate: Optional[HourlyRate] = Field(default=None, alias='hourlyRate')
    custom_field_values: List[Any] = Field(default=None, alias='customFieldValues')
    is_locked: Optional[bool] = Field(default=None, alias='isLocked')


class TimeEntryGetParams(BaseModel):
    description: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    project: Optional[str] = None
    task: Optional[str] = None
    tags: Optional[List[str]] = None
    project_required: Optional[bool] = None
    task_required: Optional[bool] = None
    hydrated: Optional[bool] = None
    in_progress: Optional[bool] = None
    page: Optional[int] = 1
    page_size: Optional[int] = 50


class CreateTimeEntryDTO(BaseModel):
    start: datetime
    end: datetime
    billable: bool = True
    description: str
    project_id: Optional[str] = Field(default=None, alias='projectId')
    task_id: Optional[str] = Field(default=None, alias='taskId')
    tag_ids: Optional[List[str]] = Field(default=None, alias='tagIds')
