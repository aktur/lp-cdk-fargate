from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2  # ec2 module has been import
from constructs import Construct


class NginxOnFargateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc(self, "VpcForFargate")
        
