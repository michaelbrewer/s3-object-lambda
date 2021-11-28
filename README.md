## S3 Object Lambda example

Update examples:

```script
aws s3 cp './examples/' s3://{S3BucketName} --recursive
```

Download via access point:

```script
aws s3api get-object --bucket '{S3ObjectLambdaAccessPoint}' --key lower.txt './upper.txt'
```
