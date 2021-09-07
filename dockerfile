FROM python:3.9-alpine
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN apk update && apk add gcc python3-dev musl-dev
RUN apk add g++
RUN pip install -r requirements.txt
# RUN pip install psycopg2-binary
RUN pip install waitress
RUN python -m spacy download ru_core_news_sm
COPY . /app
ARG ENVFILE
# RUN mv $ENVFILE config.py
EXPOSE 5005
CMD ["waitress-serve", "--port", "5005", "--call", "nluserver:create_app"]