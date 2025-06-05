import streamlit as st
import boto3

rekognition = boto3.client('rekognition')
comprehend = boto3.client('comprehend')

def get_labels(bucket, photo):
    res = rekognition.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, MaxLabels=5)
    return [f"{label['Name']} ({round(label['Confidence'], 2)}%)" for label in res['Labels']]

def get_sentiment(text):
    res = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    return res['Sentiment'], res['SentimentScore']

st.title("AWS AI Image & Sentiment App")

bucket = st.text_input("Enter your S3 bucket name")
photo = st.text_input("Enter the image file name in S3")
text_input = st.text_area("Write a comment to analyze sentiment")

if st.button("Analyze"):
    if bucket and photo and text_input:
        st.subheader("Image Labels:")
        labels = get_labels(bucket, photo)
        for l in labels:
            st.write(f"- {l}")
          
        st.subheader("Sentiment:")
        sentiment, scores = get_sentiment(text_input)                                                                                    
        st.write(f"**Sentiment:** {sentiment}")
        st.json(scores)
    else:
        st.warning("Please fill all fields.")

