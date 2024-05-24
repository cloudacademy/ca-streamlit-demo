import os
import boto3
import streamlit as st
from helpers.credentials import credential_helper

session = credential_helper.create_new_session()
s3 = session.client('s3')
bucket_name = os.environ['BUCKET_NAME']

pdf = st.file_uploader(label="Drag the PDF file here. Limit 100MB")
if pdf is not None:
    id = 123
    bucket_name = "uploads-bmtrbr"
    print(pdf.name)
    print(type(pdf))
    pdf.seek(0)
    s3.upload_fileobj(pdf, bucket_name, pdf.name)

with st.expander("See code"):
        st.code("""
        import os
        import boto3
        import streamlit as st
        from helpers.credentials import credential_helper

        session = credential_helper.create_new_session()
        s3 = session.client('s3')
        bucket_name = os.environ['BUCKET_NAME']

        pdf = st.file_uploader(label="Drag the PDF file here. Limit 100MB")
        if pdf is not None:
            id = 123
            bucket_name = "uploads-bmtrbr"
            print(pdf.name)
            print(type(pdf))
            pdf.seek(0)
            s3.upload_fileobj(pdf, bucket_name, pdf.name)
        """)