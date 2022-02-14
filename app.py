#!/usr/bin/env python3
import os

from aws_cdk import App

from nginx_on_fargate.nginx_on_fargate_stack import NginxOnFargateStack

app = App()
NginxOnFargateStack(app, "NginxOnFargateStack")

app.synth()
