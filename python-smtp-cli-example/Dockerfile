FROM python:2.7.12

# Replace with your values
ENV DOPPLERRELAY_USERNAME myusername@mydomain.com
ENV DOPPLERRELAY_PASSWORD my_api_key

# Copy current code
WORKDIR /usr/src/python-smtp-cli-example
COPY . .

# Example script
CMD [ "python", "./python-smtp-cli-example.py" ]
