import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from pymongo import MongoClient
import json

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

mongo_client = MongoClient(os.getenv("MONGODB_URI"))  
db = mongo_client['dupshield']  
collection = db['dataset-details'] 


# Function to load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

st.title("Dupshield Chatbot")

def get_data_from_mongo():

    data = list(collection.find())
    
    # Convert data to JSON string format
    json_data = json.dumps(data, default=str)  # Use default=str to handle ObjectId serialization

    return json_data

def get_gemini_model(question,additional_context=""):

     
    prompt = f"""
        You are a chatbot designed exclusively to assist with dataset   downloads. You have access to the following information about each dataset:
        - Dataset name
        - URL for download
        - Number of times it has been downloaded

        These dataset are the usual ones downloaded from the internet and hence whatever knowledge you have about them will be useful.
        

        Usual

        ### Instructions:
        
        1. Do not engage in normal conversation unrelated to dataset downloads.
        2. Keep all answers concise (maximum 3-4 sentences).
        3. If the user asks for a list of datasets, provide it in a clean, formatted list.
        4. Present information in bullet points wherever possible.
        5. If the user asks for a particular kind of dataset, look at all the datasets available and give relevant datasets that you think coulf be useful
        6. If a user asks about a dataset and what it does, tell the user whatever you know about it
        Humbug is about mosquitoes

          
        Below is the list of all available datasets: 
        {additional_context}\n\nUser: {question}\nBot:
        
        """
    
    print(prompt)
    response = chat.send_message(prompt)
    return response


additional_context = get_data_from_mongo()


st.markdown("""
    <style>
    body {
        overflow: hidden;  /* Prevent full page scroll */
    }
    .bot-message {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: left;
        width: fit-content;
        max-width: 80%;
        color: black;
    }
    .user-message {
        background-color: #E1FFC7;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: right;
        width: fit-content;
        margin-left: auto;
        color: black;
        max-width: 80%;
    }
    </style>
    """, unsafe_allow_html=True)


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input = st.chat_input("Type your message...")

# Process the user's input when submitted
if input:
    st.session_state['chat_history'].append(("You", input))

    response = get_gemini_model(input,additional_context=additional_context)
    
    st.session_state['chat_history'].append(("Bot", response.text))
    

# Display chat history inside the scrollable div
for role, text in st.session_state['chat_history']:
    if role == "Bot":
        st.markdown(f'<div class="bot-message">{text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="user-message">{text}</div>', unsafe_allow_html=True)