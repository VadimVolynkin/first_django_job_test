FROM python:3.9.16-buster

# linux libs and create the app user
RUN apt update && apt install -y --no-install-recommends htop nano \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install poetry

# copy and install dependencies
WORKDIR /app/backend

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root
# copy all app files
ADD ./backend .

EXPOSE 8020

CMD ["poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8020" ]