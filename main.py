"""
This script allows you to test the sentiment analysis API with your own data. 
It takes in a movie review and returns the predicted sentiment (positive or negative).
"""
import requests

def main():
    
    review = input("Enter your movie review: ")

    url = "https://7iuspchcp9.execute-api.us-east-1.amazonaws.com/stage_1/dev"

    payload = f"\"{review}\""
    headers = {
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text) #Uncomment if you want to see numerical value of prediction. 1 is positive, 0 is negative. 

    if "1" in response.text:
        print("Sentiment prediction: positive")
    else:
        print("Sentiment prediction: negative")
    
    return response.text

if __name__ == "__main__":
    main()