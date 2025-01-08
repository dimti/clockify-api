from typing_extensions import Literal
from clockify.model.base_model import BaseModel

class CostRate_HourlyRate(BaseModel):
    amount: int
    currency: Literal['USD']