# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# load_dotenv()
# from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input_prompt,image):
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     response = model.generate_content([input_prompt,image[0]])
#     return response.text

# def input_image_setup(uploaded_file):
#     # check if a file has been uploaded
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts=[
#             {
#                 "mime_type": uploaded_file.type, # Get the mime type of your image
#                 "data": bytes_data 
#             }
#         ]
#         return image_parts

#     else:
#         return FileNotFoundError("No File Uploaded")

# ## initialize our streamlit app
# st.set_page_config(page_title="Calories Advisor App")
# uploaded_file = st.file_uploader("Choose an image....", type=["jpg","jpeg","png"])
# image = ""
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image,caption = "Uploaded image.",use_column_width=True)

# submit = st.button("Tell me about the total calories")

# input_prompt = """
# Your are an expert in nutritionist where you need to see the food items from the image and calculate the total  calories ,also provide the details of every food items with calories intake in below format

# 1. Item 1  - no of calories
# 2. Item 2  - no of calories
# ----
# ----
# Finally you can also mention whether the food is healthy or not and also mention the percentage split of the ratio of carbohydrates,fats,fibre, sugar and other important things required in our diet


# """

# if submit: 
#     image_parts = input_image_setup(uploaded_file)
#     response = get_gemini_response(input_prompt,image_parts)
#     st.header("The Response is ")
#     st.write(response)

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of your image
                "data": bytes_data 
            }
        ]
        return image_parts

    else:
        raise FileNotFoundError("No File Uploaded")

## Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #FF0000;
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #FFFF00;
        }
        .subheader {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #FFFF00;
        }
        .description {
            font-size: 18px;
            color: #FFFF00;
        }
        .stTextInput > div > input {
            background-color: #001f3f;
            color: #FFFF00;
        }
        .stButton > button {
            background-color: #001f3f;
            color: #FFFF00;
        }
        .stFileUploader > label {
            background-color: #001f3f;
            color: #FFFF00;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

# SVG Animation for Nutritionist App
st.markdown("""
<svg width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <g>
    <title>Nutritionist</title>
    <rect width="100%" height="200" fill="#FF0000" />
    <rect x="10%" y="20" width="80%" height="160" fill="#AAAAAA" />
    <text x="50%" y="100" font-size="24" font-family="Arial" fill="#FFFF00" text-anchor="middle">
      <animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite" />
      🍏 Nutritionist App 🍎
    </text>
  </g>
</svg>
""", unsafe_allow_html=True)

# Streamlit app
# st.set_page_config(page_title="Calories Advisor App")
st.markdown('<div class="header">🍏 Nutritionist App 🍎</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Upload your food image and get a detailed calorie breakdown! 🥗🥘🍕</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image.", use_column_width=True)

submit = st.button("Tell me about the total calories")

input_prompt = """
You are an expert nutritionist. Review the food items from the image and calculate the total calories, also provide the details of every food item with calories intake in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
Finally, mention whether the food is healthy or not and also mention the percentage split of the ratio of carbohydrates, fats, fiber, sugar, and other important things required in our diet.
"""

if submit:
    image_parts = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_parts)
    st.header("The Response is:")
    st.write(response)
