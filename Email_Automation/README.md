# Email Automation Bot

A simple command-line Python project that sends emails using SMTP. The program collects recipients, a subject, and a message body, then asks for confirmation before sending.

## Features

- Send an email using Gmail SMTP
- Send the same email to multiple recipients
- Ask for recipient emails from the terminal
- Ask for the subject and message body
- Confirm before sending emails
- Store email login information outside of `main.py`

## How To Run

From the `Email_Automation` folder, activate the virtual environment:

```bash
source .venv/bin/activate
```

Then run:

```bash
python main.py
```

## Email Setup

This project uses a `config.py` file for private login information.

Create a file named `config.py`:

```python
email_address = "your_email@gmail.com"
email_password = "your_gmail_app_password"
```

For Gmail, use an App Password instead of your normal Gmail password. Your Google account usually needs 2-Step Verification enabled before you can create an App Password.

## Safety Notes

- Do not upload `config.py` to GitHub.
- Do not use this project for spam.
- Test with your own email address before sending to anyone else.
- Keep recipient lists small while learning.

## What I Learned

This project helped me practice:

- Python functions
- Lists and loops
- User input
- SMTP
- `EmailMessage`
- App passwords
- Keeping secrets out of code
- Confirmation prompts before automated actions
