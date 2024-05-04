FROM python:3.12.3
# Выбор папки, в которой будет вестись работа
WORKDIR /code
# Установка зависимостей проекта
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# Перенос проекта в образ
COPY . /code/

COPY ./migration /code/migration 
COPY ./alembic.ini /code/alembic.ini
COPY ./entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/code/entrypoint.sh"]