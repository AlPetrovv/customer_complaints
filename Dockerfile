FROM python:3.10.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN useradd -m app

RUN apt upgrade -y && apt update -y &&  \
    apt install -y python3-dev

WORKDIR home/app

ADD pyproject.toml .

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

RUN chown -R app:app /home/app/

USER app



