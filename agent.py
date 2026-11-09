#import the LIBRARIES 
from  openai import OpenAI 
from agents import Runner,Agent
from composio import Composio
from composio_openai_agents.provider import OpenAIAgentsProvider 
from composio_client import UserAuth
from dotenv import load_dotenv
import os
load_dotenv(override=True)
from supabase import create_client,Client
import supabase

# SUPABASE VARIABLEs
url = os.getenv('SUPABASE_URL')
anon_key  = os.getenv('SUPABASE_ANON_KEY')

client = create_client(url,anon_key)

#COMPOSIO VARIABLEs
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


    Some interactions may not use calendar , for such cases just respond normally
    in case if calendar is used type : 'Calendar executed successfuly' alongside the given context

    """,
    tools=session.tools()
)


def query (q):

    response = Runner.run_sync(starting_agent=agent,
               input=q)

    return ( response.final_output)



while True:

    prompt = input('YOU:')

    if prompt=='exit' or prompt=='leave': # if you enter 'exit' or 'leave' , the chat will terminate
            break
    answer = query(prompt) # the agent will answer

    print(f'AI: {answer})')
    data ={
        "query" : prompt,
        "response" : answer
        } # proper data format that will be stored in the supabase db
    
    client.table('chat_history').insert(data).execute() # insert every record of conversation WRT time into the supabase database

    
    
    

    
    