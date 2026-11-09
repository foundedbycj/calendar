import supabase

from supabase import create_client,Client
import supabase
import os
from dotenv import load_dotenv
load_dotenv()
# SUPABASE VARIABLEs
url = os.getenv('SUPABASE_URL')
anon_key  = os.getenv('SUPABASE_ANON_KEY')

client = create_client(url,anon_key)

data = {
    "response": "CJ",
    "query": 16
}

response = client.table("history").insert(data).execute()

print(response.data)