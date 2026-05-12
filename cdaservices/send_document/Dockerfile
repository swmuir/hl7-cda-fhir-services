FROM python:3.10-slim
RUN pip install --no-cache-dir requests
WORKDIR /app
COPY send_document.py .
CMD ["python", "send_document.py"]
