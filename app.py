import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Personal Travel Planner", page_icon="✈️")

st.title("✈️ Personal Travel Planner")
st.write("Generate a personalized trip itinerary based on your destination, budget, dates, and interests.")

destination = st.text_input("Destination", placeholder="Tokyo, Japan")
days = st.number_input("Number of days", min_value=1, max_value=30, value=5)
budget = st.text_input("Budget", placeholder="$1500")
travelers = st.number_input("Number of travelers", min_value=1, value=1)
interests = st.text_area("Interests", placeholder="food, museums, anime, nature")
travel_style = st.selectbox(
    "Travel style",
    ["Relaxed", "Balanced", "Fast-paced", "Budget-friendly", "Luxury"]
)

if st.button("Generate Itinerary"):
    if not destination or not budget or not interests:
        st.warning("Please fill in destination, budget, and interests.")
    else:
        prompt = f"""
        Create a personalized travel itinerary.

        Destination: {destination}
        Trip length: {days} days
        Budget: {budget}
        Travelers: {travelers}
        Interests: {interests}
        Travel style: {travel_style}

        Include:
        - Day-by-day itinerary
        - Morning, afternoon, and evening plans
        - Estimated costs
        - Restaurant/activity suggestions
        - Transportation tips
        - Budget-friendly advice
        """

        with st.spinner("Creating your travel plan..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI travel planner."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            st.subheader("Your Travel Itinerary")
            st.write(response.choices[0].message.content)