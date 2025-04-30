from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')




client = genai.Client(api_key=API_KEY)



def responding(x):
    
    question   = f"give one word answer for the calories I ate today , the data will be fed to database so pease dont add anything on it , use averages for the unknown or foggy information given and calculate the total calories i ate today , the valus you find must be from a consistent and trustworthy source, situated in india , {x} , again never respond anything other then calories"

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents= question
    )
    return response.text