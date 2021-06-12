from aws_cdk import core as cdk
import os

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
import aws_cdk.aws_appsync as appsync
import aws_cdk.aws_dynamodb as db
from aws_cdk.aws_lambda_python import PythonFunction
from aws_cdk.aws_dynamodb import Table, Attribute, AttributeType


class SlakeStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        db = Table(self, 'events', partition_key=Attribute(name='id', type=AttributeType.STRING))

        event_collector = PythonFunction(self, 'event_collector', entry=os.path.join(
            os.getcwd(), 'slake/lambdas/event_collector'), environment={'TABLE_NAME': db.table_name})

        db.grant_write_data(event_collector)

        

        # api = appsync.GraphqlApi(self, "Api",
        #     name="demo",
        #     schema=appsync.Schema.from_asset(os.path.join(
        #                                  os.getcwd(), 'slake','schema.graphql')),
        #     authorization_config=appsync.AuthorizationConfig(
        #         default_authorization=appsync.AuthorizationMode(
        #             authorization_type=appsync.AuthorizationType.IAM
        #         )
        #     ),
        #     xray_enabled=True
        # )

        # demo_table = db.Table(self, "DemoTable",
        #     partition_key=db.Attribute(
        #         name="id",
        #         type=db.AttributeType.STRING
        #     )
        # )

        # demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)

        # # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # demo_dS.create_resolver(
        #     type_name="Query",
        #     field_name="getDemos",
        #     request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
        #     response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        # )

        # # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        # demo_dS.create_resolver(
        #     type_name="Mutation",
        #     field_name="addDemo",
        #     request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
        #         appsync.PrimaryKey.partition("id").auto(),
        #         appsync.Values.projecting("input")),
        #     response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        # )
