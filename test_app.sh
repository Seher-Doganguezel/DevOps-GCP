#!/bin/bash

# Set the URL of your application on Google Cloud Run
APP_URL="YOUR_APP_URL"

# GET Tests
echo "GET Tests:"
curl $APP_URL/ENDPOINT

# POST Tests
echo -e "\nPOST Tests:"
curl -X POST -d "data=value" $APP_URL/ENDPOINT

# Error 404 Test
echo -e "\n404 Test:"
curl $APP_URL/nonexistent_endpoint
