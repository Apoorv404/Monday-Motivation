# Monday-Motivation

A Python application that automatically sends you a random motivational quote every Monday morning to help start your week with inspiration.

## Description

This project uses Python to:
- Check if it's Monday
- Select a random quote from a curated collection of motivational quotes
- Send the quote via email using SMTP (Gmail)

## Features

- Automated email delivery every Monday
- Collection of inspiring quotes from various thought leaders and philosophers
- Secure email sending using Gmail's SMTP server
- Easy to customize with your own quotes

## Requirements

- Python 3.x
- Gmail account (for sending emails)
- Required Python modules:
  - smtplib (built-in)
  - datetime (built-in)
  - random (built-in)

## Setup

1. Clone this repository
2. Open `main.py` and configure the following variables:
   - `my_email`: Your Gmail address
   - `password`: Your Gmail app password
   - `recipient_email`: Email address to receive the quotes

Note: For security, you'll need to use an App Password if you have 2-factor authentication enabled on your Gmail account.

## Usage

Run the script manually:
```bash
python main.py
```

For automatic execution, set up the script to run every day using your system's task scheduler. The script will only send emails on Mondays.

## File Structure

- `main.py` - Main script that handles email sending
- `quotes.txt` - Collection of motivational quotes
