## Customer complaints

The project accepts complaints from the user via API and analyzes them


Functionality:
1. Analyzes the sentiment of a user's message([Sentiment Analysis by APILayer](https://apilayer.com/marketplace/sentiment-analysis-api))
2. Analyzes the message category using [OpenAI API](https://platform.openai.com/docs/guides/completion/overview)

Use the `INSTALL.md` to get started.

### Built With


![FastAPI](https://img.shields.io/badge/fastapi-%23000000.svg?style=for-the-badge&logo=fastapi&logoColor=white) 
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-%231485B4.svg?style=for-the-badge&logo=SQLAlchemy&logoColor=white]) 
![Alembic](https://img.shields.io/badge/Alembic-%231485B4.svg?style=for-the-badge&logo=alembic&logoColor=white]) 
![Pydantic](https://img.shields.io/badge/pydantic-%231485B4.svg?style=for-the-badge&logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/docker-compose-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%230db7ed.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Postman Collections

##  post /api/complaints/
![workspace 1](./postman_collections/img.png)

##  get /api/complaints/
![workspace 1](./postman_collections/img_1.png)

##  path /api/complaints/
![workspace 1](./postman_collections/img_2.png)

##  [ApiLayer](https://api.apilayer.com/sentiment/analysis)
# post 
![workspace 1](./postman_collections/img_3.png)
# headers 
![workspace 1](./postman_collections/img_4.png)