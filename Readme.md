# Notifications API

## Overview

This API allows you to send notifications via email using SMTP. Below are the instructions and examples on how to interact with the API using curl.

## Endpoints

### Send Email

- **URL:** `/send/email`
- **Method:** POST
- **Description:** Sends an email notification.

#### Request Body

```json
{
  "to": "recipient@example.com",
  "subject": "Your Subject",
  "body": "Email body content"
}
```

#### Example using aiohttp to interact with API

```python
import aiohttp
import asyncio

async def send_email():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/send/email', json={
            'to': 'recipient@example.com',
            'subject': 'Your Subject',
            'body': 'Email body content'
        }) as response:
            print(await response.text())

asyncio.run(send_email())
```

#### Example curl

```bash
curl -X POST \
  http://localhost:8080/send/email \
  -H 'Content-Type: application/json' \
  -d '{
    "to": "recipient@example.com",
    "subject": "Your Subject",
    "body": "Email body content"
  }'
```

## Healthcheck Endpoint

- **URL:** `/healthcheck`
- **Method:** GET
- **Description:** This endpoint is used to verify that the service is running and healthy. It returns a simple status message indicating the health of the service.

#### Example curl healthcheck

```bash
curl -X GET http://localhost:8080/healthcheck
```

## Error Handling

- The API returns a 400 status code if there is an error sending the email.

## Configuration

- SMTP settings can be configured in the `core/config.py` file.
- To start the API in docker, run `docker build .` and `docker run -p 8080:8080 <image_id>`
