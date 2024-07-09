# api_setup.py
import google.generativeai as genai

# API setup
API_KEY = "AIzaSyCPDvWZt7wZHMLrXtwbrcRl_AY_-WRnlNw"
genai.configure(api_key=API_KEY)

modelRoomGen = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})
modelDungeonMaster = genai.GenerativeModel('gemini-1.5-flash')

chat = modelDungeonMaster.start_chat()