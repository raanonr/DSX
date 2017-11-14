#https://console.bluemix.net/docs/services/cloud-object-storage/libraries/python.html#python
# Prerequisite ::::::::
# pip install ibm-cos-sdk

import boto3
import json
import requests
import random
from botocore.client import Config
from pprint import pprint

#credentials = json.loads('{"apikey": "2SozF9MkHGQULJZHZTiZOnidaLSc3zIqr3SkDUC0YD0t", "endpoints": "https://cos-service.bluemix.net/endpoints", "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/db0d062d2b4c0836e18618a5222d8068:22e3b946-6154-4032-8e8f-7cfb0b429602::"}')

def get_cos( api_key, service_instance_id, cos_service_url="cos-service.bluemix.net"):

    # Request detailed enpoint list
    endpoints_url="https://" + cos_service_url + "/endpoints"
    endpoints = requests.get(endpoints_url).json()
    #print(json.dumps(endpoints, indent=2))
    #import pdb; pdb.set_trace()

    # Obtain iam and cos host from the the detailed endpoints
    iam_host = (endpoints['identity-endpoints']['iam-token'])
    cos_host = (endpoints['service-endpoints']['cross-region']['us']['public']['us-geo'])

    # Constrict auth and cos endpoint
    auth_endpoint = "https://" + iam_host + "/oidc/token"
    service_endpoint = "https://" + cos_host

    # Create client
    cos = boto3.client('s3',
                    ibm_api_key_id=api_key,
                    ibm_service_instance_id=service_instance_id,
                    ibm_auth_endpoint=auth_endpoint,
                    config=Config(signature_version='oauth'),
                    endpoint_url=service_endpoint)
    return cos

# Call S3 to list current buckets
def get_buckets( cos):

    response = cos.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    return buckets

def list_buckets( cos):

    buckets = get_buckets(cos)

    # Print out the bucket list
    print("Current Bucket List:")
    print(json.dumps(buckets, indent=2))

# Call S3 to list current objects
def get_objects( cos, bucket_name):

    response = cos.list_objects(Bucket=bucket_name)

    # Get a list of all object names from the response
    objects = [object['Key'] for object in response['Contents']]

    return objects

def list_objects( cos, bucket_name):

    objects = get_objects(cos, bucket_name)

    # Print out the object list
    print("Objects in bucket: %s:" % bucket_name)
    print(json.dumps(objects, indent=2))

def list_all_bucket_objects( cos):

    buckets = get_buckets(cos)
    for bucket_name in buckets:
        list_objects( cos, bucket_name)

