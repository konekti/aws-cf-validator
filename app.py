import boto3
from botocore.exceptions import ClientError, ParamValidationError
from chalice import Chalice
from chalice import BadRequestError

app = Chalice(app_name='aws-cf-validator')

def is_valid(document):
    client = boto3.client('cloudformation')
    print("document: {}".format(document))

    try:
        client.validate_template(TemplateBody=document)
    except ClientError as e:
        return { "validity": "false", "message": "ClientError " + str(e) }
    except ParamValidationError as e:
        return { "validity": "false", "message": "ParamValidationError " + str(e) }
    except Exception as e:
        return { "validity": "false", "message": "Unexpected Exception " + str(e) }

    return { "validity": "true", "message": "valid" }


@app.route('/validate', methods=['POST'], cors=True, content_types=['text/plain'])
def index():
    return is_valid(app.current_request.raw_body.decode('utf-8'))
