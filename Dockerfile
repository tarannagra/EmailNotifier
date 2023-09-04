
# syntax=docker/dockerfile:experimental

# Docker is cool

# Changing the base image to python:3.9 to make sure the right version of Python and pip are installed.
FROM python:3.9

# Copying the entire current directory to the /app/ directory in the Docker image.
COPY . /app/

# Setting /app/ as the working directory.
WORKDIR /app/

# Installing the requirements from the requirements.txt file using pip.
# Commenting out the old line and adding a new line with the correct pip command.
RUN pip install -r requirements.txt

# Installing the nltk package and downloading the 'punkt' dataset.
# Commenting out the old line and adding a new line with the correct Python command.
RUN python -c "import nltk; nltk.download('punkt')"

# Adding a comment explaining what this command does.
# Running the main.py script when the Docker container starts.
CMD python ./main.py
