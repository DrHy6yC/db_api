from sqlalchemy import select

from db.engine import async_session_sql_connect
from bot.questionnaire.schema import SQuestionnaireAdd, SQuestionnaire
from bot.questionnaire.ORM import QuestionnaireOrm


class QuestionnaireRepository:
    @classmethod
    async def add_one(cls, data: SQuestionnaireAdd) -> int:
        async with async_session_sql_connect() as session:
            questionnaire_dict = data.model_dump()
            questionnaire = QuestionnaireOrm(**questionnaire_dict)
            session.add(questionnaire)
            await session.flush()
            await session.commit()
            return questionnaire.id

    @classmethod
    async def find_all(cls) -> list[SQuestionnaire]:
        async with async_session_sql_connect() as session:
            query = select(QuestionnaireOrm)
            result = await session.execute(query)
            questionnaire_models = result.scalars().all()
            questionnaire_schemas = [SQuestionnaire.model_validate(questionnaire_model) for questionnaire_model in questionnaire_models]
            return questionnaire_schemas
