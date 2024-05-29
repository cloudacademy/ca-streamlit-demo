import boto3
import json
import base64
import streamlit as st
from io import BytesIO
from helpers.credentials import credential_helper

session = credential_helper.create_new_session()
bedrock = session.client('bedrock-runtime')
bedrock_model_id = "amazon.titan-image-generator-v1"

# Convert image data to BytesIO object
def decode_image(image_data):
    image_bytes = base64.b64decode(image_data)
    return BytesIO(image_bytes)

# Invoke Bedrock model to generate image
def generate_image(prompt):
    body = json.dumps(
        {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {
                "text":prompt
            },
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "quality": "standard",
                "height": 768,
                "width": 768,
                "cfgScale": 8.0,
                "seed": 100             
            }
        }
    )
    
    response = bedrock.invoke_model(
                modelId="amazon.titan-image-generator-v1",
                accept="application/json", 
                contentType="application/json",
                body=body
            )

    response_body = json.loads(response["body"].read())
    image_data = response_body["images"][0]

    return decode_image(image_data)

# Streamlit UI

with st.container():
    st.header("Amazon Bedrock Titan Image Generator", anchor=False, divider="rainbow")

    input_column, result_column = st.columns(2)

    # Text Input
    with input_column:
        st.subheader("Describe an image", anchor=False)
        prompt_text = st.text_input("Example: Two dogs sharing a bowl of spaghetti", key="prompt")

        def clear_field(prompt):
            st.session_state.prompt = prompt

        generate, clear = st.columns(2, gap="small")

        with generate:
            generate_button = st.button("Generate", use_container_width=True)
        with clear:
            st.button('Clear', on_click=clear_field, args=[''], use_container_width=True)

    # Resulting image column
    with result_column:
        st.subheader("Generated image", anchor=False)
        st.caption('Your image will appear here.')
        if generate_button:
            with st.spinner("Generating image..."):
                image = generate_image(prompt_text)
            st.image(image, use_column_width=True)

with st.expander("See code"):
        st.code("""
        import boto3
        import json
        import base64
        from io import BytesIO
        import streamlit as st

        session = boto3.Session(
            aws_access_key_id='####',
            aws_secret_access_key='####',
            region_name='####'
        )

        bedrock = session.client('bedrock-runtime')
        bedrock_model_id = "amazon.titan-image-generator-v1"

        # Convert image data to BytesIO object
        def decode_image(image_data):
            image_bytes = base64.b64decode(image_data)
            return BytesIO(image_bytes)

        # Invoke Bedrock model to generate image
        def generate_image(prompt):
            body = json.dumps(
                {
                    "taskType": "TEXT_IMAGE",
                    "textToImageParams": {
                        "text":prompt
                    },
                    "imageGenerationConfig": {
                        "numberOfImages": 1,
                        "quality": "standard",
                        "height": 768,
                        "width": 768,
                        "cfgScale": 8.0,
                        "seed": 100             
                    }
                }
            )
            
            response = bedrock.invoke_model(
                        modelId="amazon.titan-image-generator-v1",
                        accept="application/json", 
                        contentType="application/json",
                        body=body
                    )

            response_body = json.loads(response["body"].read())
            image_data = response_body["images"][0]

            return decode_image(image_data)

        # Streamlit UI

        with st.container():
            st.header("Amazon Bedrock Titan Image Generator", anchor=False, divider="rainbow")

            input_column, result_column = st.columns(2)

            # Text input column
            with input_column:
                st.subheader("Describe an image to generate", anchor=False)
                prompt_text = st.text_input("Example: Two dogs sharing a bowl of spaghetti", key="prompt")

                def clear_field(prompt):
                    st.session_state.prompt = prompt

                generate, clear = st.columns(2, gap="large")

                with generate:
                    generate_button = st.button("Generate", use_container_width=True)
                with clear:
                    st.button('Clear', on_click=clear_field, args=[''], use_container_width=True)

            # Resulting image column
            with result_column:
                st.subheader("Generated image", anchor=False)
                st.caption('Your image will appear here.')
                if generate_button:
                    with st.spinner("Generating image..."):
                        image = generate_image(prompt_text)
                    st.image(image, use_column_width=True)
        """)