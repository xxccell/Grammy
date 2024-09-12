import os
import streamlit as st
import google.generativeai as genai

#Set up Gemini API key and Gemini Pro model
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key = GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro") 

#Set up Streamlit page
st.set_page_config(page_title="Grammy", layout="wide", initial_sidebar_state="auto")
                   
#Function for conversion to grams
def convert_recipe_to_grams(recipe):
    prompt = f"""
    Convert the following recipe measurements from cups to grams and also millilitres to grams:

    {recipe}

    Assume standard ingredient densities unless otherwise specified.
    Make sure liquids are also given in grams. 
    After converting the ingredients, provide the complete recipe, including the directions.
    If no directions or instructions are given, do not generate any directions or instructions.
    """
    result = model.generate_content(prompt)   #Generate the result using Gemini
    
    converted_recipe = ""
    for word in result:
        converted_recipe += word.text   #Put together the generated text in one string

    return converted_recipe

#Page UI
st.title("Grammy - Convert recipes to grams!")
st.subheader("This takes the whole recipe and returns it back but everything is in grams now!")
recipe = st.text_area("Paste ingredients and recipe below to be converted",height=300 , placeholder="Ingredients and Recipe...")
button = st.button("Convert to Grams")

#Perform conversion when user has entered a recipe and clicked the button
if recipe and button:
    with st.spinner("Converting..."):
        result = convert_recipe_to_grams(recipe)
    st.subheader("Converted Recipe: ")
    st.markdown(result)

