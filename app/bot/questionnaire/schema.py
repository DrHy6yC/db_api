from datetime import datetime


from pydantic import BaseModel, ConfigDict


class SQuestionnaireAdd(BaseModel):
    questionnaire_name: str
    questionnaire_description: str


class SQuestionnaire(SQuestionnaireAdd):
    id: int
    create_time: datetime
    model_config = ConfigDict(from_attributes=True)


class SQuestionnaireID(BaseModel):
    ok: bool = True
    questionnaire_id: int
