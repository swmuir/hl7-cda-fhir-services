FROM python:3.10-slim
RUN pip install --no-cache-dir requests
WORKDIR /app
COPY cda2fhir.py .
CMD ["python", "cda2fhir.py"]
