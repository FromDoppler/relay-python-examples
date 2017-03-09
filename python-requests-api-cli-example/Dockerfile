FROM python:2.7.12

# Replace with your values
ENV DOPPLERRELAY_ACCOUNT_ID 12345 
ENV DOPPLERRELAY_ACCOUNT_NAME my-account-name
ENV DOPPLERRELAY_APIKEY my_api_key

# Copy current code
WORKDIR /usr/src/python-requests-api-cli-example
COPY . .

# Install dependencies
RUN pip install requests

# Example script
CMD [ "python", "./python-requests-api-cli-example.py" ]
