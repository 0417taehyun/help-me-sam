#!/bin/sh

aws s3 mb s3://help-me-sam --endpoint-url=http://localstack:4566
aws s3 cp /data/test.mp4 s3://help-me-sam/test.mp4 --endpoint-url=http://localstack:4566
