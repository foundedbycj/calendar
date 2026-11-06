from  openai import OpenAI 

from composio import Composio
from composio_openai_agents.provider import OpenAIAgentsProvider 
from composio_client import UserAuth
from dotenv import load_dotenv
import os
load_dotenv(override=True)

composio_api_key = os.getenv('COMPOSIO_API_KEY')
openai_api_key   = os.getenv('OPENAI_API_KEY')
provider = OpenAIAgentsProvider()

composio = Composio(provider=provider,api_key=composio_api_key)

session = composio.create(
    user_id='CJ',
    toolkits=['googlecalendar']


)

connection_request = session.authorize(toolkit='googlecalendar')

print(connection_request.redirect_url)
connected_account = connection_request.wait_for_connection()
print(connected_account.id)
tools = session.tools()