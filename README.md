## 📘 `README.md`

```markdown
# 🧠 AWS AI Demo Project — Image Label Detection & Sentiment Analysis

This project demonstrates how to use **Amazon Rekognition** and **Amazon Comprehend** to perform intelligent analysis on both images and text using Python and AWS SDK (`boto3`).

## 🚀 Features

- 🔍 **Image Label Detection** using Amazon Rekognition
- 💬 **Sentiment Analysis** on text using Amazon Comprehend
- 🗂️ Image fetched directly from **Amazon S3**
- ✅ Python CLI app
- 🖼️ (Optional) Streamlit web interface

---

## 🧰 Tech Stack

- AWS Rekognition
- AWS Comprehend
- Amazon S3
- Python 3.x
- `boto3`
- (Optional) Streamlit for a web UI

---

## 🔧 Setup Instructions

### 1. Upload an Image to S3
- Create a bucket in AWS S3
- Upload an image (`.jpg`, `.png`) — e.g., `sample.jpg`

### 2. Configure AWS Credentials
```bash
aws configure
````

Provide your Access Key, Secret Key, Region, and `json` output format.

### 3. Install Dependencies

```bash
pip install boto3
# Optional (for web version):
pip install streamlit
```

### 4. Run the Script

```bash
python aws_ai_app.py
```

### 5. Optional: Launch the Web Interface

```bash
streamlit run app.py
```

---

## 🧠 Sample Output

```bash
Detected Labels:
- Person (99.23%)
- Helmet (98.45%)
- Safety (95.13%)

Sentiment Analysis:
- Sentiment: POSITIVE
- Confidence Scores: {'Positive': 0.987, 'Negative': 0.005, 'Neutral': 0.007, 'Mixed': 0.001}
```

---

## 📌 Notes

* Make sure the IAM user has the following policies:

  * `AmazonS3ReadOnlyAccess`
  * `AmazonRekognitionFullAccess`
  * `ComprehendFullAccess`
* Text for sentiment analysis must be in **English**.

---

## 🌟 Future Improvements

* Add object localization (bounding boxes)
* Use AWS Translate for multilingual input
* Store analysis results in DynamoDB
* Add authentication to the UI


---

## 📝 GitHub Project Description

> 🧠 A beginner-friendly project that uses **Amazon Rekognition** to detect image labels and **Amazon Comprehend** to perform sentiment analysis — all powered by Python and AWS SDK. Built as part of my AI internship preparation.
> 
```
