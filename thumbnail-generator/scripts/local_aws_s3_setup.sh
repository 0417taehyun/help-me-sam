#!/bin/sh

aws s3 mb s3://example-bucket --endpoint-url=http://localstack:4566
aws s3 cp /data/test.mp4 s3://example-bucket/test.mp4 --endpoint-url=http://localstack:4566
