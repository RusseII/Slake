#!/usr/bin/env python3
import os

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from slake.slake_stack import SlakeStack

env_USA = core.Environment(account="576758376358", region="us-west-2")

app = core.App()
SlakeStack(app, "slake", env=env_USA)

app.synth()

