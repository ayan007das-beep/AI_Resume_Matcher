import streamlit as st
from openai import OpenAI
import os

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(page_title="Generative AI Playground", layout="centered")

st.title("🤖 Generative AI Prompt Playground")
st.write("Enter your prompt below and get AI-generated results instantly.")

# --------------------------
# API Key Input
# --------------------------
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    # --------------------------
    # Prompt Input Area
    # --------------------------
    user_prompt = st.text_area("Enter your prompt here:", height=200)

    # Temperature Control
    temperature = st.slider("Creativity Level (Temperature)", 0.0, 1.0, 0.7)

    if st.button("🚀 Generate Response"):
        if user_prompt.strip() == "":
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("Generating response..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "You are a helpful AI assistant."},
                            {"role": "user", "content": user_prompt}
                        ],
                        temperature=temperature,
                    )

                    result = response.choices[0].message.content

                    # --------------------------
                    # Output Section
                    # --------------------------
                    st.success("Response Generated Successfully!")
                    st.markdown("### 🧠 AI Response")
                    st.write(result)

                except Exception as e:
                    st.error(f"Error: {e}")

else:
    st.info("Please enter your API key to begin.")