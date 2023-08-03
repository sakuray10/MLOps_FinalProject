"""
This CLI tool allows you to test the sentiment analysis API with your own data. 
It takes in a movie review and returns the predicted sentiment (positive or negative).
"""
import requests
import click

@click.command()
@click.option('--text', help='text to be classified')

def predict(text): # pylint: disable=no-value-for-parameter
    url = "https://7iuspchcp9.execute-api.us-east-1.amazonaws.com/stage_1/dev" # AWS endpoint
    payload = f"\"{text}\""
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("POST", url, headers=headers, data=payload, timeout=10)  
    return response.text # returns numerical value of prediction. 0 is negative, 1 is positive.

def main(text):
    response = predict(text)
    if "1" in response:
        click.echo("Sentiment prediction: positive")
    else:
        click.echo("Sentiment prediction: negative") 

if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter