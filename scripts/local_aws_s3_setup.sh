#!/bin/sh

aws s3 mb s3://help-me-sam --endpoint-url=http://localstack:4566
aws s3api put-bucket-notification-configuration \
    --bucket help-me-sam \
    --notification-configuration ../localstack/notification.json \
    --endpoint-url=http://localstack:4566

aws lambda create-function \
    --function-name ThumbnailGenerator \
    --code ImageUri=thumbnailgenerator:latest \
    --package-type Image \
    --timeout 600 \
    --memory-size 1024
