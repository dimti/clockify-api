from typing import List, Literal, Optional
from pydantic import Field

from clockify.model.base_model import BaseModel

class AmountByCurrency(BaseModel):
    currency: Literal['USD'] = Field(default=None, alias='currency')
    amount: float = Field(default=None, alias='amount')

class Amounts(BaseModel):
    type: Literal['EARNED', 'COST', 'PROFIT', 'HIDE_AMOUNT', 'EXPORT'] = Field(default=None, alias='type')
    value: float = Field(default=None, alias='value')
    amount_by_currency: List[AmountByCurrency] = Field(default=None, alias='amountByCurrency')

class TotalAmountByCurrency(BaseModel):
    currency: Literal['USD'] = Field(default=None, alias='currency')
    amount: float = Field(default=None, alias='amount')

class SummaryReportTotals(BaseModel):
    total_time: int = Field(default=None, alias='totalTime')
    total_billable_time: int = Field(default=None, alias='totalBillableTime')
    entries_count: int = Field(default=None, alias='entriesCount')
    amounts: List[Amounts] = Field(default=None, alias='amounts')
    num_of_currencies: int = Field(default=None, alias='numOfCurrencies')
    id: str = Field(default=None, alias='_id')
    total_amount: float = Field(default=None, alias='totalAmount')
    total_amount_by_currency: List[TotalAmountByCurrency] = Field(default=None, alias='totalAmountByCurrency')

class TimeEntryId(BaseModel):
    project: Optional[str] = Field(default=None, alias='PROJECT')
    user: Optional[str] = Field(default=None, alias='USER')
    month: Optional[str] = Field(default=None, alias='MONTH')
    time_entry: str = Field(default=None, alias='TIMEENTRY')

class SummaryReportGroupChildren(BaseModel):
    duration: int = Field(default=None, alias='duration')
    amounts: List[Amounts] = Field(default=None, alias='amounts')
    amount: float = Field(default=None, alias='amount')
    id: TimeEntryId | str = Field(default=None, alias='_id')
    name: str = Field(default=None, alias='name')
    children: Optional[List['SummaryReportGroupChildren']] = Field(default=None, alias='children')

class SummaryReportGroupOne(BaseModel):
    # Catched an PROJECT group
    currency: Optional[Literal['USD']] = Field(default=None, alias='currency')
    duration: int = Field(default=None, alias='duration')
    amounts: List[Amounts] = Field(default=None, alias='amounts')
    amount: float = Field(default=None, alias='amount')
    # Only for USER group
    has_membership: Optional[bool] = Field(default=None, alias='hasMembership')
    id: str = Field(default=None, alias='_id')
    # Presented if current GROUP Essence is exists (example grouping by project, but entries does not have a project)
    name: Optional[str] = Field(default=None, alias='name')
    name_lower_case: str = Field(default=None, alias='nameLowerCase')
    # Only for a PROJECT group
    color: Optional[str] = None
    # Also
    client_name: Optional[str] = Field(default=None, alias='clientName')
    sorting_field: str = Field(default=None, alias='sortingField')
    children: List[SummaryReportGroupChildren] = Field(default=None, alias='children')
    # For a MONTH group mode
    month_short_value: Optional[str] = Field(default=None, alias='monthShortValue')
    # TODO: That field monthShortValue presented not only for groupOne object, and may be exists in children - need correct typing
    # TODO: Conditional typing depended with a group mode

class SummaryReport(BaseModel):
    totals: List[SummaryReportTotals] = []
    group_one: List[SummaryReportGroupOne] = Field(default=[], alias='groupOne')

class ClientsGetParam(BaseModel):
    ids: List[str]

class SummaryFilter(BaseModel):
    groups: List[Literal['USER', 'TIMEENTRY']] = Field(default=None, alias='groups')
    sort_column: Literal['GROUP'] = Field(default=None, alias='sortColumn')
    summary_chart_type: Literal['PROJECT'] = Field(default=None, alias='summaryChartType')

class SummaryReportGetParams(BaseModel):
    clients: Optional[ClientsGetParam] = None
    summary_filter: SummaryFilter = Field(default=None, alias='summaryFilter')
    export_type: Optional[Literal['JSON', 'CSV', 'XLSX', 'PDF']] = Field(default='JSON', alias='exportType')
    date_range_type: Optional[Literal['ABSOLUTE', 'TODAY', 'YESTERDAY', 'THIS_WEEK', 'LAST_WEEK', 'PAST_TWO_WEEKS', 
                                    'THIS_MONTH', 'LAST_MONTH', 'THIS_YEAR', 'LAST_YEAR']] = Field(default=None, alias='dateRangeType')
    date_range_start: str = Field(default=None, alias='dateRangeStart') # Example: '2024-12-01T00:00:00Z'
    date_range_end: str = Field(default=None, alias='dateRangeEnd') # Example: '2024-12-27T23:59:59Z'



