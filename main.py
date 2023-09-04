"""
# Email Notifier by Taran :)

This is a simple email notifier made for monitoring Gmail emails from a desired account
    and the send a sms to a phone number which is configured with the people at Twilo.

Please refer to the README.md for help on how to set up the environment and usage!
"""



import time
import tomllib
from typing import Union, NoReturn

from simplegmail import Gmail
from twilio.rest import Client
from nltk.tokenize import word_tokenize
from colorama import Fore, init; init(autoreset=True)

class ENotify(object):
    def __init__(self) -> None:
        self.data = tomllib.load(open('conf.toml', 'rb'))
        
        # Twilo
        self.client = Client(
            self.data["twilio"]["account_sid"],
            self.data["twilio"]["auth_token"]
        )
        self.from_number = self.data["twilio"]["from_number"]
        self.to_number = self.data["twilio"]["to_number"]
        self.message_to_send = self.data["twilio"]["message_body"]

        # Gmail
        self.gmail = Gmail()
        self.sender = self.data["gmail"]["sender"]
        self.to_watch = self.data["gmail"]["to_watch"]
        self.keywords = self.data["gmail"]['keywords']

    def read_inbox(self) -> NoReturn:
        # Retrieve unread emails
        print(f"{Fore.YELLOW}Checking inbox belonging to {self.sender}")
        while True:
            print(f"{Fore.YELLOW}Awaiting emails...")
            unread_emails = self.gmail.get_unread_inbox()
            for email in unread_emails:
                if self.to_watch in email.sender: # returns: Name <email@domain.com> which is annoying
                    print(f"{Fore.GREEN}Found email from {self.to_watch}!")
                    tokenised_content = word_tokenize(email.plain.lower())
                    for word in tokenised_content:
                        if word in self.keywords:
                            print(f"{Fore.GREEN}Found a good email!")
                            email.mark_as_important()
                            email.star()
                            email.mark_as_read()
                            print(f"{Fore.YELLOW}Sending SMS to {self.to_number}...")
                            self.send_sms()
            time.sleep(10)
    
    def send_sms(self) -> bool:
        message = self.client.messages.create(
            body=self.message_to_send,
            from_=self.from_number,
            to=self.to_number
        )
        if (message.status.lower() == "queued"):
            print("Sent SMS successfully!")
            return True
        return False


    def send_email(self) -> bool:
        # Fall back method if SMS failed... it shouldn't but best to have a precaution than not
        ...

    def get_properties(self) -> NoReturn:
        unread = self.gmail.get_unread_inbox()
        for x in unread:
            print(x.sender)
            print(x.plain.lower()) 
        words = word_tokenize(x.plain.lower())
        keywords = self.data["gmail"]['keywords']
        for word in words:
            if word in keywords:
                print(word)


if __name__ == '__main__':
    en = ENotify()
    en.read_inbox()
    # en.get_properties()