FROM python:3.10-slim

RUN pip install clickhouse-driver

COPY app.py /app/app.py

CMD ["python", "/app/app.py"]
