# WhatsApp Automation with Selenium

A beginner Python project that uses Selenium to send a message through
WhatsApp Web.

## What It Does

1. Opens WhatsApp Web in Chrome.
2. Reuses a saved Chrome profile to stay logged in.
3. Searches for a contact.
4. Opens the matching chat.
5. Types and sends a message.
6. Waits for WhatsApp's sent checkmark before closing Chrome.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Enter the exact WhatsApp contact name and message when prompted. On the first
run, scan the WhatsApp Web QR code. Later runs reuse the private
`.chrome-profile` folder.

## Privacy

The `.venv`, `.chrome-profile`, `.env`, and Python cache files are excluded
from Git. Never commit WhatsApp session data, phone numbers, or private
messages.

Use this project only for your own account and consensual messaging. Avoid
bulk or unsolicited messages.
