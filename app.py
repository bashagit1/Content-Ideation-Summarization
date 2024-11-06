import streamlit as st
import os
from openai import OpenAI

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit app setup
st.set_page_config(page_title="Content Ideation & Summarization", page_icon="✨")

# Sidebar with options
st.sidebar.markdown("<h2>✨ Options Panel</h2>", unsafe_allow_html=True)
content_type = st.sidebar.selectbox("📝 Select Content Type", ["Blog Post", "Article", "Product Description", "Social Media Post"])
summarization_style = st.sidebar.selectbox("📝 Summarization Style", ["Concise", "Detailed", "Key Takeaways"])

# Main title
st.markdown("<h1 style='text-align: center;'>Content Ideation & Summarization Tool 🌟</h1>", unsafe_allow_html=True)

# User input for content ideation and summarization
st.markdown("<h3>📥 Enter a Topic or Content to Summarize:</h3>", unsafe_allow_html=True)
user_topic = st.text_input("💡 Topic/Theme", placeholder="E.g., Benefits of Remote Work")
user_content = st.text_area("📜 Content to Summarize (optional)", placeholder="Paste text here for summarization...")

# Functions for OpenAI requests
def generate_content_ideas(topic, content_type):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Generate 5 {content_type.lower()} ideas about {topic}."}
        ]
    )
    # Updated response handling
    return response.choices[0].message.content.strip()

def summarize_content(content, style):
    prompt = f"Summarize the following content in a {style.lower()} way: {content}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # Updated response handling
    return response.choices[0].message.content.strip()

# Generate content ideas and summary based on inputs
if st.button("✨ Generate Content Ideas"):
    if user_topic:
        ideas = generate_content_ideas(user_topic, content_type)
        st.markdown("<h3>💡 Content Ideas:</h3>", unsafe_allow_html=True)
        st.write(ideas)
    else:
        st.warning("Please enter a topic to generate content ideas.")

if st.button("📜 Generate Summary"):
    if user_content:
        summary = summarize_content(user_content, summarization_style)
        st.markdown("<h3>📜 Summary:</h3>", unsafe_allow_html=True)
        st.write(summary)
    else:
        st.warning("Please enter content to summarize.")

# User guide
st.info("""
### How to Use:
1. **Enter a Topic** for content ideas and select the type of content you want to generate.
2. **Enter Content** if you'd like it summarized in your chosen style.
3. **Click Generate** for content ideas or summary.
""")
