FROM python:3.9-alpine

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev
RUN apk add postgresql zlib jpeg

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install Pillow==8.4.0
RUN pip install --no-cache-dir -r requirements.txt


# copy project
COPY . .

