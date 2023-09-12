#!/bin/bash

# Set your Google Cloud Project ID and App name
PROJECT_ID="YOUR_PROJECT_ID"
APP_NAME="YOUR_APP_NAME"

# Authenticate and configure the project
gcloud auth login
gcloud config set project $PROJECT_ID

# Build the Docker image and push it to Google Cloud Registry
docker build -t gcr.io/$PROJECT_ID/$APP_NAME .
gcloud auth configure-docker
docker push gcr.io/$PROJECT_ID/$APP_NAME

# Deploy to Google Cloud Run
gcloud run deploy --image gcr.io/$PROJECT_ID/$APP_NAME --platform managed
