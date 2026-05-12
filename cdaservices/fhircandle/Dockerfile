FROM python:3.10-slim
RUN pip install --no-cache-dir requests
WORKDIR /app
COPY post_fhir.py .
CMD ["python", "post_fhir.py"]
