# EmailNotifier

This is a simple email notifier made for monitoring Gmail emails from a desired account and the send a sms to a phone number which is configured with the people at Twilo.

## Setting up

### Docker (recommended)

```bash
$ docker build . -t email_notifier
# Docker will do it's building here
$ docker run email_notifier
# Running the project! 
```

### Python environment

```bash
$ python -m pip install -r requirements.txt
...
$ python -c "import nltk; nltk.download('punkt')"
# Installs the Punkt Sentence Tokenizer for NLTK
```

## Running

```bash
$ python main.py
```

It's as simple as this!

### Purpose for making this

I have an online business and I don't check emails as regular as I do with SMS messages. I thought, "Why not get notified on my phone when I get an email?". And so I have made this program. 

Made by [Taran Nagra](https://github.com/tarannagra)!
