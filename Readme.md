# Notifications API

## Overview

This API allows you to send notifications via email using SMTP. Below are the instructions and examples on how to interact with the API using curl.

## Endpoints

### Send Email

- **URL:** `/send-email`
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

#### Example curl

```bash
curl -X POST \
  http://localhost:8080/send-email \
  -H 'Content-Type: application/json' \
  -d '{
    "to": "recipient@example.com",
    "subject": "Your Subject",
    "body": "Email body content"
  }'
```

## Error Handling

- The API returns a 400 status code if there is an error sending the email.

## Configuration

- SMTP settings can be configured in the `core/config.py` file.
- To start the API in docker, run `docker build .` and `docker run -p 8080:8080 <image_id>`
