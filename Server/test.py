import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="AKIAZ4AWCEGPHBGH3PNK",
    aws_secret_access_key="NCmPMk3Gasj3IdF+bPfsRW71aHxF82Jq002wIEO/",
    region_name="ap-southeast-2"
)

# Send your sms message.
client.publish(
    PhoneNumber="+918551053280",
    Message="Hello World!"
)
