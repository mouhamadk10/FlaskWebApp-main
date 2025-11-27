FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV SERVER_PORT=8000
ENV SERVER_HOST=0.0.0.0

EXPOSE 8000

CMD ["python", "runserver.py"]
