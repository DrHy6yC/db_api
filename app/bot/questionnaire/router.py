from typing import Annotated

from fastapi import APIRouter, Depends

from bot.questionnaire.repository import QuestionnaireRepository
from bot.questionnaire.schema import SQuestionnaireID, SQuestionnaireAdd, SQuestionnaire

router = APIRouter(
    prefix="/questionnaire",
    tags=["Вопросник"],
)


@router.post("")
async def add_questionnaire(
        questionnaire: Annotated[SQuestionnaireAdd, Depends()],
) -> SQuestionnaireID:
    questionnaire_id = await QuestionnaireRepository.add_one(questionnaire)
    questionnaire_response = SQuestionnaireID(
        id=True,
        questionnaire_id=questionnaire_id
    )
    return questionnaire_response


@router.get("")
async def get_questionnaires() -> list[SQuestionnaire]:
    questionnaires = await QuestionnaireRepository.find_all()
    return questionnaires
