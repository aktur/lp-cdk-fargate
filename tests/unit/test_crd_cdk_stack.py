import aws_cdk as core
import aws_cdk.assertions as assertions

from crd_cdk.crd_cdk_stack import CrdCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in crd_cdk/crd_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CrdCdkStack(app, "crd-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
