# from aws_cdk import (
#     # Duration,
#     Stack,
#     # aws_sqs as sqs,
# )
# from constructs import Construct

# class HelloCdkStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)

#         # The code that defines your stack goes here

#         # example resource
#         # queue = sqs.Queue(
#         #     self, "HelloCdkQueue",
#         #     visibility_timeout=Duration.seconds(300),
#         # )


import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
            
class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)