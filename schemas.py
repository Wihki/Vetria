from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ContractResponse(BaseModel):
    contract_id: int
    user_id: int
    contract_details: str

class ClauseResponse(BaseModel):
    clause_id: int
    contract_id: int
    description: str

class AlertResponse(BaseModel):
    alert_id: int
    message: str
    is_active: bool

class AnalysisResponse(BaseModel):
    analysis_id: int
    result: str
    timestamp: str
