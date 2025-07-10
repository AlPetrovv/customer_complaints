from logging import Logger

from aiohttp import ClientSession
from sqlalchemy.ext.asyncio import AsyncSession

from complaints import crud, schemas
from config import settings
from core.enums import CategoryType
from core import exceptions


logger = Logger(__name__)
SENTIMENT_URL = settings.integration.sentiment_api_url
SENTIMENT_API_KEY = settings.integration.sentiment_api_key


error_status_code_map = {
    400: exceptions.BadRequest,
    401: exceptions.Unauthorized,
    404: exceptions.NotFound,
    429: exceptions.TooManyRequests,
    500: exceptions.InternalServerError
}

async def get_sentiment(text: str) -> str|None:
    try:
        data= text.encode("utf-8")
        headers = {"apikey": SENTIMENT_API_KEY}
        async with ClientSession() as session:
            async with session.post(SENTIMENT_URL, data=data, headers=headers) as response:
                status = response.status
                if status == 200:
                    res_data: dict = await response.json()
                    return res_data['sentiment']
                if status not in error_status_code_map:
                    raise exceptions.BaseHttpException
                raise error_status_code_map[status]()
    except exceptions.BaseHttpException as exc:
        ...
        # logger.error(f"""Error in get_sentiment: {exc.status_code} - {exc.message}""")
    except Exception as exc:
        ...
        # logger.error(f"Error in get_sentiment: {exc}")
    return None


async def get_category(complaint_id: int, text: str, session: AsyncSession) -> None:
    prompt = ('You are a helpful assistant. '
              'Your response should be a single word category(payment, technical or other) for the following text')

    response = settings.integration.openai_client.chat.completions.create(
            model=settings.integration.openai_model,
            messages=[
      {'role': 'system', 'content': prompt},
      {'role': 'user', 'content': text},
    ]
        )
    category = response.choices[0].message.content
    if category not in list(map(str, CategoryType)):
        logger.error(f'{response}')
        print(category)
        print(response.choices[0].message)
        # logger.error(f"Invalid category: {category}")
        category = CategoryType.other
    category = CategoryType(category)
    complaint_in = schemas.ComplaintUpdatePartial(id=complaint_id, category=category)
    await crud.update_partial_complaint(session, complaint_in)
