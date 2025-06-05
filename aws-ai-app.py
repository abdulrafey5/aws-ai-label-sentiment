import boto3

# AWS clients
rekognition = boto3.client('rekognition')
comprehend = boto3.client('comprehend')

def detect_labels(bucket, photo):
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=5
    )
    print("Detected Labels:")
    for label in response['Labels']:
        print(f"- {label['Name']} ({round(label['Confidence'], 2)}%)")

def analyze_sentiment(text):
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment']
    print("\nSentiment Analysis:")
    print(f"- Sentiment: {sentiment}")
    print(f"- Confidence Scores: {response['SentimentScore']}")

# --- Replace with your bucket name and image name ---
bucket = 'aws-ai-buck'
image = 'image.jpg'
comment = "This is AI technology baby!"
                                         
# --- Call functions ---
detect_labels(bucket, image)
analyze_sentiment(comment)

