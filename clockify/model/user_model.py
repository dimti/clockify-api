from typing import List, Optional
from typing_extensions import Literal
from pydantic import Field

from clockify.model.base_model import BaseModel
from clockify.model._week import weekDays


class Membership(BaseModel):
    user_id: Optional[str] = Field(default=None, alias='userId')
    hourly_rate: Optional[float] = Field(default=None, alias='hourlyRate')
    cost_rate: Optional[float] = Field(default=None, alias='costRate')
    target_id: Optional[str] = Field(default=None, alias='targetId')
    membership_type: Optional[str] = Field(default=None, alias='membershipType')
    membership_status: Optional[str] = Field(default=None, alias='membershipStatus')


class SummaryReportSettings(BaseModel):
    group: Optional[str] = None
    subgroup: Optional[str] = None


class Settings(BaseModel):
    week_start: Optional[str] = Field(default=None, alias='weekStart')
    time_zone: Optional[str] = Field(default=None, alias='timeZone')
    time_format: Optional[str] = Field(default=None, alias='timeFormat')
    date_format: Optional[str] = Field(default=None, alias='dateFormat')
    send_newsletter: Optional[bool] = Field(default=None, alias='sendNewsletter')
    weekly_updates: Optional[bool] = Field(default=None, alias='weeklyUpdates')
    long_running: Optional[bool] = Field(default=None, alias='longRunning')
    scheduled_reports: Optional[bool] = Field(default=None, alias='scheduledReports')
    approval: Optional[bool] = Field(default=None, alias='approval')
    pto: Optional[bool] = None
    alerts: Optional[bool] = Field(default=None, alias='alerts')
    reminders: Optional[bool] = Field(default=None, alias='reminders')
    time_tracking_manual: Optional[bool] = Field(default=None, alias='timeTrackingManual')
    summary_report_settings: Optional[SummaryReportSettings] = Field(default=None, alias='summaryReportSettings')
    is_compact_view_on: Optional[bool] = Field(default=None, alias='isCompactViewOn')
    dashboard_selection: Optional[str] = Field(default=None, alias='dashboardSelection')
    dashboard_view_type: Optional[str] = Field(default=None, alias='dashboardViewType')
    dashboard_pin_to_top: Optional[bool] = Field(default=None, alias='dashboardPinToTop')
    project_list_collapse: Optional[int] = Field(default=None, alias='projectListCollapse')
    collapse_all_project_lists: Optional[bool] = Field(default=None, alias='collapseAllProjectLists')
    group_similar_entries_disabled: Optional[bool] = Field(default=None, alias='groupSimilarEntriesDisabled')
    my_start_of_day: Optional[str] = Field(default=None, alias='myStartOfDay')
    project_picker_task_filter: Optional[bool] = Field(default=None, alias='projectPickerTaskFilter')
    lang: Optional[str] = Field(default=None, alias='lang')
    multi_factor_enabled: Optional[bool] = Field(default=None, alias='multiFactorEnabled')
    theme: Optional[str] = Field(default=None, alias='theme')
    scheduling: Optional[bool] = None

class CustomField(BaseModel):
    custom_field_id: str = Field(default=None, alias='customFieldId')
    value: str

class MemberProfile(BaseModel):
    name: str
    email: str
    week_start: weekDays = Field(default='MONDAY', alias='weekStart')
    work_capacity: str = Field(default='PT7H', alias='workCapacity')
    working_days:List[weekDays] = Field(default=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY'], alias='workingDays')
    workspace_number: int = Field(default=3, alias='workspaceNumber')
    image_url: str = Field(default=None, alias='imageUrl')
    remove_profile_image: Optional[bool] = Field(default=False, alias='removeProfileImage')
    has_password: bool = Field(default=True, alias='hasPassword')
    has_pending_approval_request: bool = Field(default=False, alias='hasPendingApprovalRequest')
    user_custom_field_values: List[CustomField] = Field(default=None, alias='userCustomFieldValues')

class MemberProfileGetParams(BaseModel):
    image_url: Optional[str] = Field(default=None, alias='imageUrl')
    name: Optional[str] = None
    remove_profile_image: Optional[bool] = Field(default=False, alias='removeProfileImage')
    user_custom_fields: Optional[List[CustomField]] = Field(default=None, alias='userCustomFields')
    week_start: Optional[weekDays] = Field(default='MONDAY', alias='weekStart')
    work_capacity: Optional[int] = Field(default=25200, alias='workCapacity')
    working_days: Optional[List[weekDays]] = Field(default='MONDAY', alias='workingDays')

class User(BaseModel):
    id_: Optional[str] = Field(default=None, alias='id')
    email: Optional[str] = None
    name: str
    memberships: Optional[List[Membership]] = Field(default=None, alias='memberships')
    profile_picture: Optional[str] = Field(default=None, alias='profilePicture')
    active_workspace: Optional[str] = Field(default=None, alias='activeWorkspace')
    default_workspace: Optional[str] = Field(default=None, alias='defaultWorkspace')
    settings: Optional[Settings] = Field(default=None, alias='settings')
    status: Optional[str] = None

class UserGetParams(BaseModel):
    email: Optional[str] = None
    include_roles: Optional[bool] = Field(default=None, alias='include-roles')
    sort_column: Optional[Literal["ID", "EMAIL", "NAME", "NAME_LOWERCASE", "ACCESS", "HOURLYRATE", "COSTRATE"]] = Field(default=None, alias='sort-column')
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(default=None, alias='sort-order')
    