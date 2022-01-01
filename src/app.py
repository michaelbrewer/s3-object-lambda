import boto3
from urllib.request import urlopen

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging.correlation_paths import S3_OBJECT_LAMBDA
from aws_lambda_powertools.utilities.data_classes import event_source
from aws_lambda_powertools.utilities.data_classes.s3_object_event import (
    S3ObjectLambdaEvent,
)

logger = Logger()
tracer = Tracer()
session = boto3.Session()
s3 = session.client("s3")


@logger.inject_lambda_context(correlation_id_path=S3_OBJECT_LAMBDA)
@event_source(data_class=S3ObjectLambdaEvent)
def lambda_handler(event, context):

    # Get object from S3
    original_object = urlopen(event.input_s3_url).read()

    # Make changes to the object about to be returned
    transformed_object = original_object.upper()

    # Write object back to S3 Object Lambda
    s3.write_get_object_response(
        Body=transformed_object,
        RequestRoute=event.request_route,
        RequestToken=event.request_token,
    )

    return {"status_code": 200}
