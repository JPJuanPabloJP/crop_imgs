import time
import json
import boto3


def lambda_handler(event, context):

    # client
    ec2 = boto3.client("ec2")
    ssm = boto3.client("ssm")
    # region
    region = 'us-east-1'

    # getting instance information
    describeInstance = ec2.describe_instances()

    InstanceId = []
    # fetchin instance id of the running instances
    for i in describeInstance["Reservations"]:
        for instance in i["Instances"]:
            if instance["State"]["Name"] == "running":
                InstanceId.append(instance["InstanceId"])

    # looping through instance ids
    for instanceid in InstanceId:
        # command to be executed on instance
        response = ssm.send_command(
            InstanceIds=[instanceid],
            DocumentName="AWS-RunShellScript",
            Parameters={"commands": ["sudo systemctl start grafana-server","sudo service influxdb start"]})

        # fetching command id for the output
        command_id = response["Command"]["CommandId"]

        time.sleep(3)

        # fetching command output
        output = ssm.get_command_invocation(CommandId=command_id, InstanceId=instanceid)
        print(output)

    return {"statusCode": 200, "body": json.dumps("commands executed successfully")}
