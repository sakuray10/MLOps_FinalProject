![image] 
(https://github.com/sakuray10/MLOps_FinalProject/assets/87715968/aa5593da-6858-484c-8ff1-37b90351fcc4)
# Sentiment Analysis with AWS SageMaker, Lambda, and API Gateway

MLOps Final Project - Amani, Diarra, Sakura
### This project aims to perform sentiment analysis on movie reviews using a weighted ensemble model deployed on AWS SageMaker, Lambda, and API Gateway. The dataset used for training and testing is the IMDB Movie Ratings Sentiment Analysis dataset available on Kaggle.

## Key Components:
1. Dataset: The IMDB Movie Ratings Sentiment Analysis dataset contains labeled movie reviews, making it suitable for training a sentiment analysis model.

2. AWS SageMaker: SageMaker is utilized for model training and deployment. Multiple machine learning algorithms are employed to create diverse models, which are combined using a weighted ensemble approach for improved performance.

3. Weighted Ensemble Model: The ensemble model combines the predictions of individual models using weights assigned based on their performance on validation data.

4. Lambda: AWS Lambda is used to create a serverless function that executes the ensemble model for sentiment analysis.

5. API Gateway: API Gateway is employed to create a RESTful API that allows users to make HTTP requests to invoke the Lambda function for sentiment analysis.

## Deployment Steps:
1. Data Preprocessing: The IMDb dataset is preprocessed to prepare it for model training.

2. Model Training: Multiple machine learning algorithms are used to train individual models on the preprocessed data.

3. Ensemble Model Creation: The ensemble model is constructed by combining the predictions of individual models with assigned weights.

4. Model Deployment: The ensemble model is deployed on SageMaker for real-time inference.

5. Lambda Function Creation: An AWS Lambda function is created to execute the ensemble model for sentiment analysis.

6. API Gateway Configuration: API Gateway is configured to create a REST API endpoint that triggers the Lambda function.

## Usage:
Users can access the sentiment analysis functionality by making HTTP requests to the API Gateway endpoint with their movie reviews as input. The API will return the sentiment analysis results as a response.

## Benefits:
- Accurate Sentiment Analysis: The weighted ensemble model provides improved sentiment analysis accuracy by leveraging the strengths of individual models.

- Scalability: The serverless architecture using Lambda and API Gateway allows for easy scalability and cost-effectiveness.

- Real-time Inference: The deployed model supports real-time inference, making it suitable for interactive applications.

## This project demonstrates how to implement a sentiment analysis solution using a weighted ensemble model on AWS SageMaker, Lambda, and API Gateway, providing a practical and efficient approach for analyzing movie reviews.







### IMDB Movie Ratings Sentiment Analysis
### Kaggle Data Set: https://www.kaggle.com/datasets/yasserh/imdb-movie-ratings-sentiment-analysis




