import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load preprocessed data and model components
train_data = pd.read_csv('preprocessed_data/train_data.csv')

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('models/X_train_vec.pkl', 'rb') as f:
    X_train_vec = pickle.load(f)

# Function to recommend recipes
def recommend_recipes(ingredients):
    ingredients_vec = vectorizer.transform([' '.join(ingredients)])
    similarities = cosine_similarity(ingredients_vec, X_train_vec).flatten()
    indices = similarities.argsort()[-5:][::-1]  # Get top 5 recipes
    return train_data.iloc[indices][['Title', 'Instructions', 'ingredients']]

# Function to format instructions
def format_instructions(instructions):
    steps = instructions.split('. ')
    formatted_steps = [f"🍽️ **Step {i+1}:** {step.strip()}." for i, step in enumerate(steps) if step]
    formatted_steps.append("🎉 **You're ready to feast! Bon Appétit!** 🍷🍴")
    return '\n\n'.join(formatted_steps)

# Styling
st.markdown("""
    <style>
        .recipe-card {
            background: linear-gradient(135deg, #333, #1e1e1e);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 5px 15px rgba(255, 165, 0, 0.3);
            margin-bottom: 25px;
            transition: transform 0.2s ease-in-out;
        }
        .recipe-card:hover {
            transform: scale(1.03);
            box-shadow: 0px 8px 20px rgba(255, 165, 0, 0.5);
        }
        .recipe-title {
            font-size: 26px;
            font-weight: bold;
            color: #ffcc00;
            text-align: center;
            margin-bottom: 10px;
        }
        .ingredients {
            font-size: 16px;
            margin-top: 10px;
            color: #f8f8f8;
        }
        .back-button {
            background: linear-gradient(90deg, #ff9900, #ff6600);
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 12px;
            text-align: center;
            width: 220px;
            box-shadow: 0px 4px 10px rgba(255, 140, 0, 0.4);
            transition: 0.3s;
            cursor: pointer;
            display: block;
            margin: 20px auto;
            font-weight: bold;
            text-decoration: none;
        }
        .back-button:hover {
            background: linear-gradient(90deg, #ff6600, #ff3300);
            box-shadow: 0px 6px 14px rgba(255, 100, 0, 0.6);
        }
    </style>
""", unsafe_allow_html=True)

# Get ingredients from session state
if "ingredients" in st.session_state:
    ingredients_list = [ingredient.strip().lower() for ingredient in st.session_state.ingredients.split(',')]
    recommended_recipes = recommend_recipes(ingredients_list)

    st.title("🍽️ **Delicious Recipe Recommendations**")

    for index, row in recommended_recipes.iterrows():
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        
        st.markdown(f'<p class="recipe-title">{row["Title"]} 🍜</p>', unsafe_allow_html=True)
        
        # ✅ **Show Ingredients First**
        st.markdown("### 🛒 Ingredients")
        if isinstance(row['ingredients'], float) or pd.isna(row['ingredients']):  
            st.warning("⚠️ Ingredients data is missing for this recipe.")
        else:
            ingredients_text = row['ingredients'].replace(" - ", ", ")  # Handle different separators
            ingredients_list = [item.strip() for item in ingredients_text.split(',') if item.strip()]
            for ingredient in ingredients_list:
                st.write(f"- ✅ {ingredient}")

        # ✅ **Show Steps After Ingredients**
        st.markdown(format_instructions(row['Instructions']))
        
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.error("⚠️ No ingredients provided. Please go back and enter ingredients.")

# # Go back button - FIXED NAVIGATION 
# if st.button("⬅️ Go Back"):
#     st.switch_page("Home")
