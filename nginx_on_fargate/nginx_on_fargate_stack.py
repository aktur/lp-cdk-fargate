from aws_cdk import Stack, Tags
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns
from constructs import Construct


class NginxOnFargateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc: ec2.Vpc = ec2.Vpc(self, "VpcForFargate")
        cluster: ecs.Cluster = ecs.Cluster(self, "EcsCluster", vpc=vpc)

        fargate_service: ecs_patterns.ApplicationLoadBalancedFargateService = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "FargateService",
            cluster=cluster,
            cpu= 256,
            memory_limit_mib=512,
            task_image_options={
                'image': ecs.ContainerImage.from_registry("nginx")
            },
            desired_count=1,
        )

        Tags.of(scope).add("AppName", "NginxFargatePoc")
        Tags.of(scope).add("Stage", "Dev")
        
