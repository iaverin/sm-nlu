FROM python:3.9-slim-buster
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
# RUN pip install psycopg2-binary
RUN pip install waitress
COPY . /app
ARG ENVFILE
# RUN mv $ENVFILE config.py
EXPOSE 5005
CMD ["waitress-serve", "--port", "5005", "--call", "nluserver:create_app"]