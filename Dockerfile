FROM python:3.12

WORKDIR /service

RUN pip install  --upgrade pip && pip install aiosmtplib pydantic[email] fastapi uvicorn

COPY . .

EXPOSE 8080

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]