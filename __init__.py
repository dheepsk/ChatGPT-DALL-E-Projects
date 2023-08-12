import logging
import openai
import azure.functions as func


# sample request
# {"prompt": "pikachu running", "n": 1, "size": "1024x1024"}
secret_key = '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'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI secret_key to authenticate
    openai.api_key = secret_key

    # get variables from the HTTP request body
    req_body = req.get_json()

    # call OpenAI API
    output = openai.Image.create(
        prompt=req_body['prompt'],
        n=req_body['n'],
        size=req_body['size']
    )

    # provide the response
    output_text = output['data'][0]['url'] # go to openai documentation to know what names to put

    return func.HttpResponse(output_text,status_code=200)