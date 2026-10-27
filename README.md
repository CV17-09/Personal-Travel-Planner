# 🌍 Personal Travel Planner

An AI-driven travel planning application that uses Large Language Models (LLMs) to create personalized travel itineraries based on a user’s destination, budget, travel dates, interests, and preferences.

## 📌 Project Overview

Personal Travel Planner helps users generate custom trip plans without manually researching hotels, attractions, restaurants, and schedules. The system takes natural-language input such as:

> “Plan a 5-day trip to Tokyo under $1500. I like food, museums, and anime.”

The AI then creates a structured itinerary with daily activities, estimated costs, travel tips, and recommendations.

## 🎯 Purpose

Planning a trip can be overwhelming because travelers must compare destinations, budgets, activities, transportation, and schedules. This project solves that problem by using AI to generate personalized and organized travel plans quickly.

## ✨ Features

- Generate custom travel itineraries using AI
- Accept natural-language user preferences
- Recommend activities based on interests
- Consider budget, destination, and travel length
- Create day-by-day travel schedules
- Suggest restaurants, attractions, and transportation options
- Provide estimated costs
- Allow users to revise or regenerate plans

## 🧠 AI Component

This project uses an LLM to understand user preferences and generate personalized recommendations.

The AI processes:
- Destination
- Budget
- Travel dates
- Number of travelers
- Interests
- Food preferences
- Travel style
- Activity level

Then it produces:
- Daily itinerary
- Recommended places
- Budget breakdown
- Travel tips
- Personalized suggestions

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenAI API or other LLM API
- Pandas
- JSON
- Optional: Google Maps API / Travel APIs

## 🏗️ System Architecture

```text
User Input
   ↓
Preference Extraction
   ↓
LLM Prompt Processing
   ↓
Itinerary Generation
   ↓
Budget + Recommendation Formatting
   ↓
User-Friendly Travel Plan
