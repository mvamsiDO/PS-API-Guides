import requests
import json
import os

api_key = os.environ.get('GRADIENT_API_KEY')
project_id = os.environ.get('GRADIENT_PROJECT_ID')

hf_token = os.environ.get('HF_READ_TOKEN')

url = "https://api.paperspace.com/v1/deployments"

def create_update_deployment(project_id, spec_obj, api_key, deployment_id=None):
    payload = json.dumps({
      "deploymentId": deployment_id,
      "projectId": project_id,
      "config": spec_obj
    })
    headers = {
      'Content-Type': 'application/json',
    }
    headers['Authorization'] = "Bearer " + api_key
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

# spec_obj = json.load(open('configs/mistral_vllm_config.json'))
# spec_obj["env"][0]["value"] = hf_token
# print(spec_obj)
# result = create_update_deployment(project_id, spec_obj, api_key)
# print(result) # {"deploymentId":"8b02d762-0aa1-41e3-8b63-717477cf090d"} 

def get_run_status(deployment_id, api_key):
    n_url = url + "/" + deployment_id + "/runs"
    headers = {
      'Content-Type': 'application/json',
    }
    headers['Authorization'] = "Bearer " + api_key

    response = requests.request("GET", n_url, headers=headers)
    json_response = json.loads(response.text)
    # print(json_response)
    print(response.status_code)
    if response.status_code != 200:
        print("Error: ", response.text)
        return "Error"
    if not json_response:
        print("Empty response!")
        return "No Runs Found"
    else:
        status = json_response[0]['instances'][0]['state']
        return status

# result = get_run_status("8b02d762-0aa1-41e3-8b63-717477cf090d", api_key)
# print("Status: ", result)  # Status:  healthy / pending / error / No Runs Found 


def get_endpoint_url(deployment_id, api_key):
    n_url = url + "/" + deployment_id
    headers = {
      'Content-Type': 'application/json',
    }
    headers['Authorization'] = "Bearer " + api_key
    response = requests.request("GET", n_url, headers=headers)
    json_response = json.loads(response.text)
    # print(json_response)
    print(response.status_code)
    if response.status_code != 200:
        print("Error: ", response.text)
        return "Error"
    if not json_response:
        print("Empty response!")
        return "No Runs Found"
    else:
        endpoint_url = json_response['endpoint']
        return endpoint_url

# result = get_endpoint_url("8b02d762-0aa1-41e3-8b63-717477cf090d", api_key)
# print("Result: ", result)  # Endpoint URL


def disable_deployment(project_id, spec_obj, deployment_id, api_key):
    spec_obj["enabled"] = False
    print("spec_obj after disable:", spec_obj)
    payload = json.dumps({
      "deploymentId": deployment_id,
      "projectId": project_id,
      "config": spec_obj
    })
    headers = {
      'Content-Type': 'application/json',
    }
    headers['Authorization'] = "Bearer " + api_key
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

spec_obj = json.load(open('configs/mistral_vllm_config.json'))
spec_obj["env"][0]["value"] = hf_token
print(spec_obj)
deployment_id = "8b02d762-0aa1-41e3-8b63-717477cf090d"
result = disable_deployment(project_id, spec_obj, deployment_id, api_key)
print(result)  
