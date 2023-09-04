# syntax=docker/dockerfile:experimental

# Docker is cool

FROM python
COPY . /app/
WORKDIR /app/
RUN python -m pip install -r requirements.txt
RUN python -c "import nltk; nltk.download('punkt')"
CMD python ./main.py