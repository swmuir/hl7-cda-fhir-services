FROM python:3.10-slim
RUN pip install --no-cache-dir requests
WORKDIR /app
COPY get_codes.py .
CMD ["python", "get_codes.py"]
