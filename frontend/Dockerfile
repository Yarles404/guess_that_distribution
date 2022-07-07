FROM python:3.10.5-slim

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
