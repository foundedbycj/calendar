#import the dependencies 
from  openai import OpenAI 
from agents import Runner,Agent
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

session = composio.create( #make session of composio
    user_id='CJ',
    toolkits=['googlecalendar']


)


agent = Agent(
    name="Calendar Assistant",
    instructions="""
    You are a helpful Google Calendar assistant.

    You can:
    - List upcoming events.
    - Check schedules.
    - Create calendar events.
    - Update existing events.
    - Delete events only after user confirmation.

    Always use the available Composio tools
    to interact with Google Calendar.
    """,
    tools=session.tools()
)


def query (q):

    response = Runner.run_sync(starting_agent=agent,
               input=q)

    print( response.final_output)



query('can you schedule two events of 30 mins tomorrow at time : 8AM and 4PM')