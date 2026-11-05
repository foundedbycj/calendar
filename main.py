from  openai import OpenAI 
import agents
from composio import Composio
from composio_openai_agents import OpenAIAgentsProvider 
from composio_client import UserAuth
from dotenv import load_dotenv
import os
load_dotenv()

composio_api_key = os.getenv('COMPOSIO_API_KEY')
openai_api_key   = os.getenv('OPENAI_API_KEY')