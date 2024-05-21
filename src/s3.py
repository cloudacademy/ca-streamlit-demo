import os
import boto3
import streamlit as st

s3 = boto3.client('s3')
bucket_name = os.environ['BUCKET_NAME']

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("File:", uploaded_file.name)
    s3.upload_fileobj(uploaded_file, bucket_name, uploaded_file.name)
