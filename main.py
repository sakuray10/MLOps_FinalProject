"""
This CLI tool allows you to test the sentiment analysis API with your own data. 
It takes in a movie review and returns the predicted sentiment (positive or negative).
"""
import click
import requests

@click.command()
@click.option('--text', help='text to be classified')

def predict(text): # pylint: disable=no-value-for-parameter
    url = "https://7iuspchcp9.execute-api.us-east-1.amazonaws.com/stage_1/dev" # AWS endpoint
    payload = f"\"{text}\""
    headers = {
    'Content-Type': 'text/plain'
    }
    response = requests.request("POST", url, headers=headers, data=payload, timeout=10)
    click.echo(response.text)  
    if "1" in response.text:
        click.echo("Sentiment prediction: positive")
    else:
        click.echo("Sentiment prediction: negative") 
    return response.text # returns numerical value of prediction. 0 is negative, 1 is positive.

if __name__ == '__main__':
    predict() # pylint: disable=no-value-for-parameter