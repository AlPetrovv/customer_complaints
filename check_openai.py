import aiohttp

async def check_openai():
    async with aiohttp.ClientSession() as session:
        data = {
            'text': 'You are from technical developer!!!'
        }
        async with session.post('http://0.0.0.0:8000/api/complaints/', data=data) as response:
            return response