from src.custom import AWSS3, AWSLambdaEvent, AWSS3ObjectModel


class AWSEventParser:
    @staticmethod
    def create_aws_s3_object_model(event: AWSLambdaEvent) -> AWSS3ObjectModel:
        aws_s3_record: AWSS3 = event.get("Records").pop().get("s3")
        return AWSS3ObjectModel(
            bucket_name=aws_s3_record.get("bucket").get("name"),
            object_key=aws_s3_record.get("object").get("key"),
        )
