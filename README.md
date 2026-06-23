# AWS S3 → Lambda → SNS CSV Processing Project

## Project Overview

This project demonstrates a serverless event-driven architecture on AWS.

Whenever a CSV file is uploaded to an Amazon S3 bucket:

1. Amazon S3 triggers an AWS Lambda function.
2. Lambda reads the uploaded CSV file.
3. Lambda parses the CSV data using Python.
4. Parsed records are logged to CloudWatch.
5. Lambda sends an email notification using Amazon SNS.

---

# Architecture

```text
CSV Upload
     │
     ▼
Amazon S3 Bucket
     │
     ▼
AWS Lambda
     │
 ┌───┴────┐
 ▼        ▼
CloudWatch SNS
 Logs      │
           ▼
      Email Alert
```

---

# AWS Services Used

| Service    | Purpose                    |
| ---------- | -------------------------- |
| Amazon S3  | Store uploaded CSV files   |
| AWS Lambda | Process uploaded CSV files |
| Amazon SNS | Send email notifications   |
| IAM        | Manage permissions         |
| CloudWatch | Store Lambda logs          |

---

# Project Workflow

Step 1:

User uploads a CSV file to S3.

Example:

```text
employees.csv
```

Step 2:

S3 Event Notification triggers Lambda.

Step 3:

Lambda retrieves file using:

```python
s3.get_object()
```

Step 4:

Lambda parses CSV using:

```python
csv.DictReader()
```

Step 5:

Records are printed to CloudWatch Logs.

Example:

```python
{
'name': 'John Doe',
'email': 'john.doe@example.com',
'department': 'Engineering',
'salary': '95000'
}
```

Step 6:

Lambda publishes a message to SNS.

Step 7:

SNS sends an email notification to subscribed users.

---

# Prerequisites

AWS Account

Basic knowledge of:

* S3
* Lambda
* IAM
* SNS
* Python

---

# Step 1: Create S3 Bucket

Navigate to:

```text
AWS Console
→ S3
→ Create Bucket
```

Bucket Name:

```text
test-csv-rik
```

Keep default settings.

---

# Step 2: Create SNS Topic

Navigate to:

```text
AWS Console
→ SNS
→ Topics
→ Create Topic
```

Type:

```text
Standard
```

Name:

```text
csv-upload-alert
```

Copy Topic ARN.

Example:

```text
arn:aws:sns:ap-south-1:123456789012:csv-upload-alert
```

---

# Step 3: Create Email Subscription

Inside SNS Topic:

```text
Create Subscription
```

Protocol:

```text
Email
```

Endpoint:

```text
your-email@example.com
```

Confirm the subscription through the email received from AWS.

---

# Step 4: Create Lambda Function

Navigate to:

```text
AWS Console
→ Lambda
→ Create Function
```

Configuration:

```text
Function Name:
csv-file-processor

Runtime:
Python 3.13

Handler:
lambda_function.lambda_handler
```

Upload:

```text
lambda_function.py
```

---

# Step 5: Configure IAM Permissions

Attach permissions to Lambda execution role.

Required permissions:

## S3

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject"
  ],
  "Resource": "*"
}
```

## SNS

```json
{
  "Effect": "Allow",
  "Action": [
    "sns:Publish"
  ],
  "Resource": "*"
}
```

For learning purposes you may attach:

```text
AmazonS3ReadOnlyAccess
AmazonSNSFullAccess
```

---

# Step 6: Configure S3 Trigger

Open Lambda.

Select:

```text
Add Trigger
```

Choose:

```text
S3
```

Configuration:

```text
Bucket:
test-csv-rik

Event Type:
PUT

Prefix:
(optional)

Suffix:
.csv
```

Save.

---

# Step 7: Deploy Lambda Code

Update:

```python
TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"
```

Deploy Lambda.

---

# Testing

Upload:

```text
employees.csv
```

to:

```text
test-csv-rik
```

Expected Results:

## CloudWatch Logs

```text
File Uploaded: employees.csv
Total Rows: 4
```

## SNS Email

Subject:

```text
CSV File Uploaded
```

Message:

```text
A new CSV file has been uploaded.

Bucket: test-csv-rik
File: employees.csv
Total Records: 4

CSV processing completed successfully.
```

---

# Common Issues and Fixes

## AccessDenied on GetObject

Cause:

Missing S3 permissions.

Fix:

```text
s3:GetObject
```

permission must be attached.

---

## Unable to Import Module

Cause:

Wrong file name or handler.

Correct:

```text
lambda_function.py
```

Handler:

```text
lambda_function.lambda_handler
```

---

## No Email Received

Verify:

1. SNS subscription is confirmed.
2. Correct Topic ARN is configured.
3. Lambda has sns:Publish permission.

---

# Future Enhancements

This project can be extended with:

* MySQL Database Integration
* Amazon RDS
* Duplicate Record Detection
* CSV Validation
* Error Notification Emails
* Dead Letter Queue (DLQ)
* EventBridge Integration
* CloudWatch Dashboard
* Data Analytics Pipeline

---

# Author

Gairik Baidya

MCA | AWS Cloud & Full Stack Developer

GitHub Portfolio Project

```
```
