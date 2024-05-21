import os
import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
bucket_name = os.environ['BUCKET_NAME']
file_name = bucket_name + "/test.txt"

conn = st.connection('s3', type=FilesConnection)
df = conn.read(file_name, input_format="text", ttl=600)

st.write(df)