-- paste this table schema into your supabase tables--

-- for creating table -- 
create table chat_history(

    id integer primary key not null ,
    created_at timestamptz default now(), 
    query text not null , -- query of the user--
    response text not null -- response of the AI assistant--


)