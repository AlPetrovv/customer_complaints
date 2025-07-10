## Getting Started

### Prerequisites

Before getting started, you will need to have Python 3.10 for running local server or docker.

### Installation

1. Get  OpenAI API Key at [OpenAI](https://platform.openai.com/docs/guides/completion/overview)
2. Get APILayer API Key for Sentiment Analysis at [APILayer](https://apilayer.com/marketplace/sentiment-analysis-api)
3. Clone the repo
   ```sh
   git clone https://github.com/AlPetrovv/customer_complaints.git
   ```
4. Install poetry(if you use docker image, skip step 4,5,6)
   * You can install poetry from [here](https://python-poetry.org/)
   * Or use `pip install poetry` if you have venv environment
   * Or use `curl -sSL https://install.python-poetry.org | python3 -`, you need curl installed
5. Install dependencies
   ```sh
   poetry install
   ```
6. Run alembic migrations
   ```sh
   poetry run alembic upgrade head
   ```
7. Add env variables to files 
   ```sh
   cp envs/app.env.template envs/app.env
   cp envs/db.env.template envs/db.env
   ```
   and replace `xxx` with your data
8. Run server
   ```sh
   poetry run uvicorn src.main:app --reload
   ```
   if you use docker
   ```sh
   docker run customer_complaints
   ```
