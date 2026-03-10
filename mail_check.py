import imaplib
import email
from email.header import decode_header

def fetch_emails():
  
    IMAP_SERVER = "imap.gmail.com"
    EMAIL_ADDRESS = " "
    APP_PASSWORD = " " # mail hesabından alınan 16 haneli şifre (App Password)

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ADDRESS, APP_PASSWORD)
        mail.select("inbox")
        
        status, messages = mail.search(None, "ALL")
        mail_ids = messages[0].split()
        last_5_ids = mail_ids[-5:]

        print(f"\n--- Son 5 E-posta ({EMAIL_ADDRESS}) ---\n")
        for m_id in reversed(last_5_ids):
            res, msg_data = mail.fetch(m_id, "(RFC822)")
            for response in msg_data:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    sender = msg.get("From")
                    print(f"KİMDEN: {sender}\nKONU: {subject}\n" + "-"*30)
        mail.logout()
    except Exception as e:
        print(f"HATA OLUŞTU: {e}")

if __name__ == "__main__":
    fetch_emails()
