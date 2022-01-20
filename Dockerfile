FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app/backend
COPY requirements.txt /app/backend
RUN pip install -r requirements.txt
EXPOSE 9020
