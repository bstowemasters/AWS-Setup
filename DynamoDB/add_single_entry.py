import boto3
import json
from botocore.exceptions import ClientError
import os

# Define your AWS credentials
# We're reading these values from our OS's environment variables, this is so we can securely store the code online (etc GitHub) without anyone seeing our credentials!
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")

# Define the region of your table & the table name
REGION = "eu-west-1"
TABLE_NAME = "Users"

# Initialize session
session = boto3.session.Session(
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name=REGION,
)

# Create DynamoDB client
dynamodb = session.client('dynamodb')

# Define the items we want to store
item = {
    "ID": {"S": "001"}, # What happens if we run this twice?
                        # How could you randomise this each time (UUIDs)? 
    "Username": {"S": "BenSM"},
    "Password": {"S": "BensBadPassword"}
    # What could we do to hide the password from being seen by anybody?
}

# Write the data to the DynamoDB Table
def write_to_dynamodb():
    response = dynamodb.put_item(TableName=TABLE_NAME, Item=item)
    print("Successfully added table entry")

    # Print the response from the API
    print(f"\nResponse:\n{json.dumps(response, indent=4)}")
    # Have you used 'f' strings in python?

# This is fine for the example but for best practice we should use if __name__ == "__main__": runOurFunc()
write_to_dynamodb()
