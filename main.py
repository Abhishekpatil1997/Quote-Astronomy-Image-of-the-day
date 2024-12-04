import requests
import time
import streamlit as st

# This is a NASA API for the astronomical image
image_api_key = 'oxe7XaJIe7oqvn8LeS8G0tPCh2heuFH4FGw7qajh'
date = time.strftime("%b-%d-%Y")
image_url = f"https://api.nasa.gov/planetary/apod?api_key={image_api_key}"

# This is a Zen Quote API for the Quote
thought_url = "https://zenquotes.io/api/today"

# Here the data is requested from the API for the quote
thought_response = requests.get(thought_url)
thought = thought_response.json()

# Quote,author is stored in respective variable
quote = thought[0]['q']
author = thought[0]['a']

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([3, 5, 3])

with col1:
    st.write(f"Date: {date}")

with col2:
    "\n"
    "\n"
    "\n"
    "\n"
    st.title("Quote of The Day:")
    st.subheader(f"{quote}")
    st.write(f"~ {author}")
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"




# Here the data is requested from the API for the Image
content_response = requests.get(image_url)
content_data = content_response.json()


# Get Image title
content_title = content_data['title']

# Get the explanation for the image
image_explanation = content_data['explanation']


# Get the credit of the image
content_credit_name = content_data["copyright"]

st.title(f"{content_title}:")

if content_data["media_type"] == "video":
    video_url = content_data['url']

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Today's content is a video:")
        st.subheader(f"[Video Link]({video_url})")
        st.write(f"Credit: {content_credit_name}")

    with col2:
        st.subheader("Explanation:")
        st.info(image_explanation)

elif content_data["media_type"] == "image":
    image_url = content_data['hdurl']
    image = requests.get(image_url)
    image_content = image.content
    with open(f'daily_images/{date}.png', 'wb') as image_file:
        image_file.write(image_content)

    col1, col2 = st.columns(2)

    with col1:
        filepath_image = f"daily_images/{date}.png"
        st.image(filepath_image, use_container_width=True)
        st.write(f"Credit: {content_credit_name}")

    with col2:
        st.subheader("Explanation:")
        st.info(image_explanation)
