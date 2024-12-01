import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Streamlit app title and setup
st.title("🩺 Symptom Checker")
st.divider()

# Configure SSL and NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load symptoms from the JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'symptoms.json')

if not os.path.exists(file_path):
    st.error(f"symptoms.json not found. Please place the file in: {file_path}")
    st.stop()

try:
    with open(file_path, "r") as file:
        symptoms = json.load(file)
except json.JSONDecodeError:
    st.error("Invalid JSON format in symptoms.json. Please check the file structure.")
    st.stop()
except Exception as e:
    st.error(f"Error loading symptoms.json: {e}")
    st.stop()

# Prepare data for training
tags = []
patterns = []
for intent in symptoms:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

# Train the model
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
x = vectorizer.fit_transform(patterns)
y = tags
clf = LogisticRegression(random_state=0, max_iter=10000)
clf.fit(x, y)

# Chatbot function
def chatbot(input_text):
    input_vector = vectorizer.transform([input_text])
    tag = clf.predict(input_vector)[0]
    for intent in symptoms:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "I'm sorry, I couldn't identify the symptoms. Could you provide more details?"

# Chat history file setup
chat_history_file = 'chat_history.csv'
if not os.path.exists(chat_history_file):
    with open(chat_history_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

# Chat interface
st.subheader("**☮️ Isayu Here!!**")
st.write("Describe your symptoms in detail, and I'll help identify potential conditions or suggest remedies.")

# Chat input
user_input = st.text_input("You:", key="user_input")

if user_input:
    response = chatbot(user_input)
    st.text_area("Isayu_:", value=response, height=120, max_chars=None, key="chatbot_response")

    # Save chat history
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(chat_history_file, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([user_input, response, timestamp])

    # Exit if user says goodbye
    if response.lower() in ["goodbye", "bye"]:
        st.write("Thank you for chatting with me. Have a great day!")
        st.stop()
