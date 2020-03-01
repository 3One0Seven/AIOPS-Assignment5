import json
from pre_processing.pre_processing import PreProcessor
import boto3
import datetime
import time

my_pre_precessor = PreProcessor(padding_size=40, max_dictionary_size=5000)
sage_maker_client = boto3.client("runtime.sagemaker")
def lambda_handler(event, context):
    
    tweet = event["tweet"]
    
    pre_start_time = time.time()
    features = my_pre_precessor.pre_process_text(tweet)
    pre_process_time = time.time() - pre_start_time
    
    # TODO implement
    model_playload = {
        'features_input': features
    }

    model_start_time = time.time()
    model_response = sage_maker_client.invoke_endpoint(
    	EndpointName = 'preprocess',
    	ContentType = 'application/json',
    	Body = json.dumps(model_playload))
    model_inference_time = time.time() - model_start_time

    result = json.loads(model_response["Body"].read().decode())

    response = {}

    if result["predictions"][0][0] >= 0.5:
    	response["sentiment"] = "positive"
    else:
    	response["sentiment"] = "negative"
    payload = {
    	"Date and time of request" : datetime.datetime.now(),
    	"Tweet" : tweet,
    	"Sentiment" : response["sentiment"],
    	"Probability from the model" : result["predictions"][0][0],
    	"Preprocessing Time" : str(pre_process_time),
    	"Model Inference Time" : str(model_inference_time)
    }

    def default(o):
    	if isinstance(o, (datetime.date,datetime.datetime)):
    		return o.isoformat()
    print('Result: ' + json.dumps(response, default = default, indent = 2))

    s3 = boto3.resource('s3')
    s3_result = s3.Object('group12twitterbucket', 'lmbda/payload.json')

    s3object.put(
        Body=(bytes(json.dumps(payload, default=default).encode('UTF-8')))
    )

    return response