import boto3
import csv

# AWS Clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# SNS Topic ARN
TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):

    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        print(f"File Uploaded: {key}")

        response = s3.get_object(
            Bucket=bucket,
            Key=key
        )

        content = response['Body'].read().decode('utf-8')

        rows = list(csv.DictReader(content.splitlines()))

        print(f"Total Rows: {len(rows)}")

        for row in rows:
            print(row)

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="CSV File Uploaded",
            Message=f"""
A new CSV file has been uploaded.

Bucket: {bucket}
File: {key}
Total Records: {len(rows)}

CSV processing completed successfully.
"""
        )

        return {
            "statusCode": 200,
            "body": "CSV Processed Successfully"
        }

    except Exception as e:
        print(f"Error: {str(e)}")

        return {
            "statusCode": 500,
            "body": str(e)
        }
