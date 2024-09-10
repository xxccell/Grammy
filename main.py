import os
import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key = GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro") 

st.title("Grammy - Convert recipes to grams!")
st.subheader("This takes the whole recipe and returns it back but everything is in grams now!")

chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question, stream=True)
    return response

def convert_recipe_to_grams(recipe):
    prompt = f"""
    Convert the following recipe measurements from cups to grams:

    {recipe}

    Assume standard ingredient densities unless otherwise specified.
    After converting the ingredients, provide the complete recipe, including the directions.
    """
    result = LLM_Response(prompt)

    converted_recipe = ""
    for word in result:
        converted_recipe += word.text

    return converted_recipe


recipe = st.text_area("Paste recipe below to be converted")
button = st.button("Convert to Grams")

if recipe and button: 
    result = convert_recipe_to_grams(recipe)
    st.subheader("Converted Recipe: ")
    st.markdown(result)

