import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_HOST = "smtp-relay.brevo.com"
SMTP_PORT = 587
SMTP_USER = os.getenv("EMAIL_USER")
SMTP_PASS = os.getenv("EMAIL_PASS")
EMAIL_FROM = os.getenv("EMAIL_FROM")


async def send_email(to_email: str, subject: str, html: str):
    msg = MIMEMultipart("alternative")

    msg["Subject"] = subject
    msg["From"] = f"Coursify <{EMAIL_FROM}>"
    msg["To"] = to_email

    msg.attach(MIMEText(html, "html"))

    await aiosmtplib.send(
        msg,
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SMTP_USER,
        password=SMTP_PASS,
        start_tls=True,
    )


async def send_verification_code(to_email: str, code: str):
    html = f"""
        <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
            <h2 style="color: #20AFAB;">Email Verification</h2>
            <p>Your verification code is:</p>
            <h1 style="letter-spacing: 8px; color: #4da3f5;">{code}</h1>
            <p>This code expires in <strong>10 minutes</strong>.</p>
        </div>
    """

    await send_email(
        to_email,
        "Your Coursify Verification Code",
        html
    )


async def send_reset_code(to_email: str, code: str):
    html = f"""
        <div style="font-family: sans-serif; max-width: 480px; margin: auto;">
            <h2 style="color: #20AFAB;">Password Reset</h2>
            <p>You requested to reset your Coursify password. Your reset code is:</p>
            <h1 style="letter-spacing: 8px; color: #f5a623;">{code}</h1>
            <p>This code expires in <strong>10 minutes</strong>.</p>
            <p style="color: #999; font-size: 12px;">
                If you didn't request this, you can safely ignore this email.
            </p>
        </div>
    """

    await send_email(
        to_email,
        "Your Coursify Password Reset Code",
        html
    )