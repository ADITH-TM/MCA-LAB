import streamlit as st
import base64

# Title
st.title("🍽️ Smart Recipe Recommendation System")

# Description
st.write("🔍 Enter the ingredients you have, and we'll find the **best recipes** for you!")

# Input Box
st.header("🛒 Ingredients List")
ingredients_input = st.text_area("Enter ingredients separated by commas", "", height=150)

# Centered Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('🍳 Get Recipes'):
        # Split ingredients and filter out empty spaces
        ingredients_list = [ing.strip() for ing in ingredients_input.split(',') if ing.strip()]
        
        # Ensure at least two ingredients are provided
        if len(ingredients_list) > 1:
            st.session_state.ingredients = ingredients_input
            st.switch_page("pages/Results.py")
        else:
            st.warning("⚠️ Please enter at least two ingredients before proceeding.")
