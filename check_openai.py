import httpx



def check_openai():
    client = httpx.Client()
    response = client.post('http://0.0.0.0:8000/api/complaints/', json={
        'text': 'You are from technical developer!!!'
    }, timeout=None)

    print(response.status_code)
    print(response.text)


check_openai()