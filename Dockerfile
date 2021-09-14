FROM python:alpine
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


RUN pip install pipenv
RUN apk update && apk add gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


ENV PATH="/.venv/bin:$PATH"
WORKDIR /app

COPY . /app/
EXPOSE 5000

CMD ["python" , "app.py"]