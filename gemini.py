"""
Author: Bisnu Ray
Telegram: https://t.me/SmartBisnuBio
"""

import os
import google.generativeai as genai

# Fetch the API key from the environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Check if the API key is available
if GOOGLE_API_KEY is None:
    print("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

# Configure the API key for Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Example: Generate text from text input
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What Can You Do ?")
print(response.text)  # Displaying text directly in the console
