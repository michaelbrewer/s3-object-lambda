# S3 Object Lambda example

## Deployment

Build:

```script
sam build
```

Guided deployment

```script
sam deploy --guided
```

Update examples:

```script
aws s3 cp './examples/' s3://{S3BucketName} --recursive
```

Download via access point:

```script
aws s3api get-object --bucket '{S3ObjectLambdaAccessPoint}' --key lower.txt './upper.txt'
```

## Development

Install dev dependencies

```script
make dev
```

After initial deployment, run in watch mode

```script
make watch
```

Clean up local environment

```script
make clean
```
