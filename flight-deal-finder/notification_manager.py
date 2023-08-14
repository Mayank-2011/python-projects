import smtplib


class NotificationManager:

    def send_emails(self, emails, message):
        my_email = "your email"
        password = "your email application password"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}".encode("utf-8")
                )
