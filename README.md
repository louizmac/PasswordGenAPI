<div align="center">

# PasswordGenAPI

<p>
  A lightweight, open-source REST API for secure password generation.
  <br>
  Generate strong, customizable passwords using Python and FastAPI.
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-REST_API-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Version-1.0.0-black?style=flat-square" alt="Version">
</p>

</div>

---

## Overview

PasswordGenAPI is a simple, lightweight REST API that generates cryptographically secure passwords.

It allows developers to generate customizable passwords for websites, mobile applications, and other projects without relying on external password generation services.

Passwords are generated using Python's built-in `secrets` module.

No database or external API is required.

## Features

- Cryptographically secure password generation
- Customizable password length (8–128 characters)
- Optional uppercase letters
- Optional lowercase letters
- Optional numbers
- Optional special characters
- Guaranteed inclusion of each enabled character type
- JSON responses
- Input validation
- Interactive API documentation
- No external API dependencies
- Lightweight and self-hosted

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/louizmac/PasswordGenAPI.git
cd PasswordGenAPI
```

**2. Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Start the server**

```bash
python3 -m uvicorn main:app --host 127.0.0.1 --port 8000
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive documentation:

`http://127.0.0.1:8000/docs`

## API Reference

### Generate Password

`GET /api/v1/password/generate`

Generate a cryptographically secure password with customizable settings.

**Parameters**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| length | Integer | 20 | Password length (8–128) |
| uppercase | Boolean | true | Include uppercase letters |
| lowercase | Boolean | true | Include lowercase letters |
| numbers | Boolean | true | Include numbers |
| symbols | Boolean | true | Include special characters |

At least one character type must be enabled.

### Example Request

```bash
curl -G "http://127.0.0.1:8000/api/v1/password/generate" \
  --data-urlencode "length=24" \
  --data-urlencode "uppercase=true" \
  --data-urlencode "lowercase=true" \
  --data-urlencode "numbers=true" \
  --data-urlencode "symbols=true"
```

### Example Response

```json
{
  "password": "K7#mP9!vR2@xL5$qT8zN4&kB",
  "length": 24,
  "options": {
    "uppercase": true,
    "lowercase": true,
    "numbers": true,
    "symbols": true
  }
}
```

The password is randomly generated for every request.

## Python Example

Install the requests library:

```bash
pip install requests
```

```python
import requests

url = "http://127.0.0.1:8000/api/v1/password/generate"

response = requests.get(
    url,
    params={
        "length": 24,
        "uppercase": True,
        "lowercase": True,
        "numbers": True,
        "symbols": True
    }
)

response.raise_for_status()

password = response.json()["password"]

print(password)
```

## JavaScript Example

```javascript
async function generatePassword() {
    const response = await fetch(
        "http://127.0.0.1:8000/api/v1/password/generate?length=20"
    );

    if (!response.ok) {
        throw new Error("Password generation failed");
    }

    const data = await response.json();

    return data.password;
}

generatePassword().then(console.log);
```

## Password Options

| Option | Characters |
|--------|------------|
| Uppercase | A–Z |
| Lowercase | a–z |
| Numbers | 0–9 |
| Symbols | ! @ # $ % ^ & * ( ) - _ = + |

Every enabled character category is guaranteed to appear at least once in the generated password.

## Error Handling

PasswordGenAPI validates incoming requests and returns appropriate HTTP errors.

| Status Code | Description |
|-------------|-------------|
| 200 | Password generated successfully |
| 400 | Invalid password configuration |
| 422 | Invalid request parameters |

Example error response:

```json
{
  "detail": "At least one character type must be enabled"
}
```

## Project Structure

```text
PasswordGenAPI/
├── main.py
├── core/
│   ├── __init__.py
│   └── generator.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Security

PasswordGenAPI uses Python's `secrets` module for cryptographically secure random password generation.

- Passwords are generated using a cryptographically secure random source.
- No database is required.
- Passwords are not intentionally stored by the application.
- No external password generation service is used.
- HTTPS is recommended for public deployments.
- Password responses should use `Cache-Control: no-store`.
- Request and response logging should avoid sensitive password data.

For sensitive applications, generating passwords locally is preferable to transmitting them through a third-party server.

## TryMyAPIs

PasswordGenAPI is designed for integration with **TryMyAPIs**, a platform for discovering, testing, and learning how to use REST APIs.

TryMyAPIs provides an interactive interface for exploring APIs directly in your browser.

**Website:** [trymyapis.rf.gd](https://trymyapis.rf.gd)

## License

See the `LICENSE` file for licensing information.

---

<div align="center">

  <sub>Built with Python and FastAPI.</sub>
  <br>
  <sub>Created by <a href="https://github.com/louizmac">louizmac</a></sub>

</div>
