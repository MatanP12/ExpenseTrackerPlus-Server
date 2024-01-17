FROM python:3.11-alpine3.15

ENV POETRY_VERSION=1.4.2

WORKDIR /app

COPY /pyproject.toml .
RUN pip install poetry==${POETRY_VERSION}
RUN poetry config virtualenvs.create false

RUN poetry install --without dev --no-root
COPY ./src .

EXPOSE 8000

CMD [ "poetry","run", "uvicorn","expense_tracker_plus.main:app"]