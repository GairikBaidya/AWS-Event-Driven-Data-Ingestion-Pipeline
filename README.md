# 🚀 AWS Serverless CSV Processing Pipeline

> An end-to-end event-driven data ingestion pipeline built using AWS services that securely uploads CSV files from a web application, processes data automatically, stores records in MySQL, and sends real-time email notifications.

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow)
![S3](https://img.shields.io/badge/Amazon-S3-blue)
![SNS](https://img.shields.io/badge/Amazon-SNS-green)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue)
![Python](https://img.shields.io/badge/Python-3.13-yellow)

---

# 📌 Project Overview

This project demonstrates a complete cloud-native, event-driven architecture using AWS services.

When a user uploads a CSV file through the web application:

✅ File is securely uploaded to Amazon S3 using a Pre-Signed URL

✅ Amazon S3 triggers an AWS Lambda function

✅ Lambda reads and parses the CSV file

✅ Records are inserted into a MySQL database hosted on AWS EC2

✅ Amazon SNS sends an email notification

✅ Logs are stored in Amazon CloudWatch

---

# 🏗️ Architecture

```text
┌─────────────────┐
│   Frontend UI   │
│ HTML/CSS/JS     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ API Gateway     │
└────────┬────────┘
         │
         ▼
┌────────────────────────┐
│ Lambda                 │
│ Generate Pre-Signed URL│
└────────┬───────────────┘
         │
         ▼
┌─────────────────┐
│ Amazon S3       │
│ CSV Storage     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Lambda CSV Processor    │
│ Parse CSV & Insert Data │
└───────┬─────────┬───────┘
        │         │
        ▼         ▼
 ┌───────────┐ ┌──────────┐
 │ MySQL EC2 │ │ SNS Email│
 └───────────┘ └──────────┘
```

---

# ✨ Features

### 🌐 Frontend

* Modern CSV Upload Interface
* Drag & Drop Support
* CSV Preview
* Upload Progress Tracking
* Success Receipt Generation

### ☁️ AWS Services

* Amazon S3
* AWS Lambda
* API Gateway
* Amazon SNS
* CloudWatch Logs
* IAM Roles & Policies
* Lambda Layers

### 🗄️ Database

* MySQL on Amazon EC2
* Automatic Record Insertion
* Structured Employee Data Storage

### 🔒 Security

* Pre-Signed URLs
* IAM Role-Based Access
* Secure Browser Uploads
* No AWS Credentials Exposed

---

# 🛠️ Tech Stack

| Category     | Technology            |
| ------------ | --------------------- |
| Frontend     | HTML, CSS, JavaScript |
| Backend      | Python                |
| Cloud        | AWS                   |
| Storage      | Amazon S3             |
| Compute      | AWS Lambda            |
| API          | API Gateway           |
| Notification | Amazon SNS            |
| Database     | MySQL                 |
| Monitoring   | CloudWatch            |

---

# 📂 Project Structure

```text
aws-serverless-csv-processing-pipeline/
│
├── frontend/
│   └── index.html
│
├── lambda/
│   ├── generate-upload-url/
│   │   └── lambda_function.py
│   │
│   └── csv-processor/
│       └── lambda_function.py
│
├── screenshots/
│   ├── frontend.png
│   ├── upload-success.png
│   ├── s3-upload.png
│   ├── mysql-data.png
│   └── sns-email.png
│
├── architecture.png
│
└── README.md
```

---

# ⚙️ Workflow

## Step 1

User uploads:

```text
employees.csv
```

from the web application.

---

## Step 2

Frontend requests a secure upload URL from:

```text
API Gateway
```

---

## Step 3

Lambda generates a temporary:

```text
Pre-Signed URL
```

---

## Step 4

Browser uploads CSV directly to:

```text
Amazon S3
```

---

## Step 5

S3 triggers:

```text
CSV Processing Lambda
```

---

## Step 6

Lambda:

* Reads CSV
* Parses records
* Inserts rows into MySQL

---

## Step 7

Amazon SNS sends:

```text
CSV Imported Successfully
```

email notification.

---

# 📧 Sample Notification

```text
Subject:
CSV Imported Successfully

File: employees.csv

Rows Inserted: 5

Database: csvdb
Table: employees
```

---

# 🗃️ Sample CSV

```csv
name,email,department,salary
John Doe,john.doe@example.com,Engineering,95000
Jane Smith,jane.smith@example.com,Marketing,78000
Michael Chang,m.chang@example.com,Sales,82000
```

---

# 📸 Screenshots

## Frontend Upload Portal

Add screenshot here:

```text
screenshots/frontend.png
```

## Successful Upload

Add screenshot here:

```text
screenshots/upload-success.png
```

## Data Stored in MySQL

Add screenshot here:

```text
screenshots/mysql-data.png
```

## SNS Email Notification

Add screenshot here:

```text
screenshots/sns-email.png
```

---

# 🎯 Learning Outcomes

Through this project I learned:

* Event-Driven Architecture
* AWS Lambda
* Amazon S3
* API Gateway
* Lambda Layers
* IAM Permissions
* SNS Notifications
* MySQL Integration
* CloudWatch Monitoring
* CORS Configuration
* Secure File Uploads using Pre-Signed URLs

---

# 🚧 Future Improvements

* Dynamic File Naming
* Duplicate Record Handling
* RDS MySQL Migration
* Dashboard & Analytics
* Authentication with Cognito
* CSV Validation
* Multi-User Support
* Data Visualization

---

# 👨‍💻 Author

### Gairik Baidya

MCA Student | Full Stack Developer | AWS Cloud Enthusiast

📌 Passionate about Cloud Computing, Web Development, and AI

---

⭐ If you found this project useful, don't forget to star the repository.
