# Programatically Start and Stop Paperspace Resources using the API

- Repo with Python scripts showing the usage of the new [Paperspace API](https://docs.digitalocean.com/reference/paperspace/pspace/api-reference/)
- Main use case is to start and stop Paperspace resources like Gradient Deployments and Core machines using the API.
- For both the cases we use an A5000 GPU, with Mistral-7B vLLM docker image that exposes an API endpoint to run inference on a model.

## Introduction
1. `gradient_api_example` 
    - Python script and supporting files showing how to use the Paperspace API for Gradient Deployments 
    - To create a new Deployment
    - To Fetch the status of a Deployment
    - To Disable a Deployment

2. `core_api_example` 
    - Python Notebook and supporting files showing how to use the Paperspace API for Core machines
    - To start and Stop a Core machine
    - To get the status of a Core machine
    - To Create and attach a Startup Script to a Core machine

3. `VLLM-MistralTest.postman_collection.json`
    - Postman collection to test the API endpoints for the Mistral-7B vLLM docker image
    - Make sure to change the `URL` in the postman collection to the `IP address` of the Core machine OR the `endpoint url` of the Gradient Deployment
