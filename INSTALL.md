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
4. Install poetry(if you use docker image, skip step 4,5,6,7,8)
   * You can install poetry from [here](https://python-poetry.org/)
   * Or use `pip install poetry` if you have venv environment
   * Or use `curl -sSL https://install.python-poetry.org | python3 -`, you need curl installed
5. Create virtual environment
   ```sh
   poetry env use 3.10
   ```
6. Use virtual environment
   ```sh
   source "$(poetry env info -p)"/bin/activate
   ```
7. Install dependencies
   ```sh
   poetry install
   ```
8. Run alembic migrations
   ```sh
   python3 alembic upgrade head
   ```
9. Add env variables to files 
   ```sh
   cp envs/app.env.template envs/app.env
   cp envs/db.env.template envs/db.env
   ```
   and replace `xxx` with your data
10. Run server
    ```sh
    cd src && python3 main.py
    ```
    if you use docker
    ```sh
    docker compose up --build -d
    ```
11. Open Postman or your favorite client to [docs](http://localhost:8000/docs/)
