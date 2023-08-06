from dataclasses import dataclass


@dataclass
class AWSS3ObjectModel:
    bucket_name: str
    object_key: str
