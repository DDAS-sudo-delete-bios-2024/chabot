# Chatbot

This chatbot is aimed to complement the **DDAS** system.  
Picture this: You, as a student or researcher in an institute, want to download a dataset related to a classification task. You may not be certain which dataset to use or even if such a dataset exists. In such cases, having access to a database could be helpful as it would give you insight into what others are working on or have worked with.

However, there are challenges:
1. The database could be vast, making it cumbersome to search through.
2. Many datasets do not have self-explanatory names that reveal their purpose.

Hence, in such a scenario, an **LLM-based chatbot** could prove useful. The chatbot will be fed details of all existing datasets in the database. With this, it will possess knowledge of what is available and can also provide insights into the purpose and uses of each dataset, thanks to its broader training on the entire internet. The chatbot will guide the confused user with the necessary details efficiently.

---

## Tools Used

- ![Gemini API](https://img.icons8.com/fluency/24/api.png) **Gemini API**
-  **Streamlit**
- ![MongoDB](https://img.icons8.com/color/24/mongodb.png) **MongoDB**
- ![Python](https://img.icons8.com/color/24/python.png) **Python**
- ![Langchain](https://img.icons8.com/color/24/chain.png) **Langchain** *(in the future maybe)*

---

## How to Replicate

1. **Install the requirements** from the `requirements.txt` using:
   ```bash
   pip install -r requirements.txt
2. **Get your own Gemini API key** from the Gemini website and add it to the `.env` file.

3. **Get the MongoDB URI** from MongoDB Atlas, create a database and a collection within it.  
  Modify the following code in your project accordingly:

  ```python
  mongo_client = MongoClient(os.getenv("MONGODB_URI"))  
  db = mongo_client['dupshield']  
  collection = db['dataset-details']
```

4.Add both API keys (Gemini API and MongoDB URI) to your .env file.

5. Run the application:
```bash
streamlit run chatbot.py
```

## Screenshots

![Sample chat](./sample_chat.png)
