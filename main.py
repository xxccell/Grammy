import os
import streamlit as st
import google.generativeai as genai

# Set up Streamlit page
st.set_page_config(page_title="Grammy", layout="wide", initial_sidebar_state="auto")
st.title("Grammy - Convert recipes to grams!")
st.subheader("This takes the whole recipe and returns it back but everything is in grams now!")

#Initialize Gemini API key from environment variable or use session state
if "GEMINI_API_KEY" not in st.session_state:
    st.session_state.GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

#Function to initialize Gemini model
def gemini_init(api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    return model

#Ask user to input API key if not set
if not st.session_state.GEMINI_API_KEY:
    st.warning("GEMINI API Key not set. Please provide your API Key.")
    api_key_input = st.text_input("Enter your API Key", type="password")

    if api_key_input:
        st.session_state.GEMINI_API_KEY = api_key_input
        st.success("Gemini API Key set successfully.")
        model = gemini_init(st.session_state.GEMINI_API_KEY)
else:
    model = gemini_init(st.session_state.GEMINI_API_KEY)

#Only show the recipe input and conversion button after API key is set
if st.session_state.GEMINI_API_KEY:
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
        result = model.generate_content(prompt)  #Generate the result using Gemini
        
        converted_recipe = ""
        for word in result:
            converted_recipe += word.text  #Put together the generated text in one string

        return converted_recipe

    recipe = st.text_area("Paste ingredients and recipe below to be converted", height=300, placeholder="Ingredients and Recipe...")
    button = st.button("Convert to Grams")

    if recipe and button:  #Perform conversion when user has entered a recipe and clicked the button
        with st.spinner("Converting..."):
            result = convert_recipe_to_grams(recipe)
        st.subheader("Converted Recipe: ")
        st.markdown(result)
