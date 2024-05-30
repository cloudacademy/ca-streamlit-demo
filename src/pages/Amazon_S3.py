import os
import boto3
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from io import BytesIO

s3 = boto3.client('s3')
bucket_name = os.environ['BUCKET_NAME']

st.set_page_config(layout="wide")

upload_s3, read_s3 = st.columns(2)

with upload_s3:
    st.subheader("Upload to Amazon S3")
    obj = st.file_uploader(label=f"Uploading to: :green[{bucket_name}]")
    if obj is not None:
        s3.upload_fileobj(obj, bucket_name, obj.name)

with read_s3:
    st.subheader("Read from Amazon S3")
    response = s3.list_objects_v2(Bucket=bucket_name)
    object_list = []

    if 'Contents' in response:
        for obj in response['Contents']:
            if not obj['Key'].endswith('/'):
                object_list.append(obj['Key'])
    else:
        st.write(f"S3 bucket is empty")

    selected_obj = st.selectbox(f"Selecting from: :green[{bucket_name}]", object_list, index=None)
    st.caption(f"You selected: :blue[{selected_obj}]")

st.divider()

if selected_obj is None:
    st.caption("Please select an object from S3 bucket")
else:
    response = s3.get_object(Bucket=bucket_name, Key=selected_obj)
    body = response['Body'].read()

    if selected_obj.endswith(".png"):
        st.image(BytesIO(body))
    elif selected_obj.endswith(".pdf"):
        pdf_viewer(body)
    else:
        st.write(body.decode('utf-8'))

with st.expander("See code"):
        st.code("""
        import os
        import boto3
        import streamlit as st
        from streamlit_pdf_viewer import pdf_viewer
        from io import BytesIO

        s3 = boto3.client('s3')
        bucket_name = os.environ['BUCKET_NAME']

        st.set_page_config(layout="wide")

        upload_s3, read_s3 = st.columns(2)

        with upload_s3:
            st.subheader("Upload to Amazon S3")
            obj = st.file_uploader(label=f"Uploading to: :green[{bucket_name}]")
            if obj is not None:
                s3.upload_fileobj(obj, bucket_name, obj.name)

        with read_s3:
            st.subheader("Read from Amazon S3")
            response = s3.list_objects_v2(Bucket=bucket_name)
            object_list = []

            if 'Contents' in response:
                for obj in response['Contents']:
                    if not obj['Key'].endswith('/'):
                        object_list.append(obj['Key'])
            else:
                st.write(f"S3 bucket is empty")

            selected_obj = st.selectbox(f"Selecting from: :green[{bucket_name}]", object_list, index=None)
            st.caption(f"You selected: :blue[{selected_obj}]")

        st.divider()

        if selected_obj is None:
            st.caption("Please select an object from S3 bucket")
        else:
            response = s3.get_object(Bucket=bucket_name, Key=selected_obj)
            body = response['Body'].read()

            if selected_obj.endswith(".png"):
                st.image(BytesIO(body))
            elif selected_obj.endswith(".pdf"):
                pdf_viewer(body)
            else:
                st.write(body.decode('utf-8'))
        """)