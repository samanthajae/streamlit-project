#import relevant libraries
import os
import re
import numpy as np
import pandas as pd
import json
import tiktoken
import requests

from urllib.request import urlopen
from urllib.parse import urlparse
from datetime import datetime
from htmldate import find_date
from bs4 import BeautifulSoup
from goose3 import Goose
from dotenv import load_dotenv

from openai import OpenAI
from getpass import getpass

load_dotenv('.env')

#use API key to access OpenAI Client
client = OpenAI(api_key=os.getenv('KEY'))

#define function  to send and receive messages from LLM
def get_embedding(input, model='text-embedding-3-small'):
    response = client.embeddings.create(
        input=input,
        model=model
    )
    return [x.embedding for x in response.data]


#define helper function to call LLM
def get_completion(prompt, model="gpt-4o-mini", temperature=0, top_p=1.0, max_tokens=1024, n=1):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1
    )
    return response.choices[0].message.content

#define function to take in "messages" as parameter
def get_completion_from_messages(messages, model="gpt-4o-mini", temperature=0, top_p=1.0, max_tokens=1024, n=1):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1
    )
    return response.choices[0].message.content

#define function to open and read contents of text file
def read_urls_from_file(input_file):
    urls = input_file.readlines()
    return [url.strip() for url in urls if url.strip()]

#define function to extract text data from URLs
def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        #extract the title
        title = soup.title.string if soup.title else 'No title found'
        
        #extract the published date
        date = None
        date_meta = soup.find('meta', {'property': 'article:published_time'})
        if date_meta:
            date = date_meta['content']
        
        #extract text content
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])

        #identify groups of interest
        groups = identify_groups_of_interest(text_content)
        
        #identify potential locations from url domain
        location_pattern = r'(?P<city>[a-zA-Z]+)(?:[.-]?(?P<state>[a-zA-Z]{2,3}))?(?:[.-]?(?P<country>[a-zA-Z]+))?'
    
        #match the pattern against the domain
        match = re.search(location_pattern, domain)
    
        if match:
            city = match.group('city')
            state = match.group('state') if match.group('state') else 'N/A'
            country = match.group('country') if match.group('country') else 'N/A'

        return {
            'Title': title,
            'Date': date,
            'City': city,
            'State': state,
            'Country': country,
            'Group(s)': groups,
            'Content': text_content
        }
    except Exception as e:
        return {'error': str(e)}

#define function to identify groups of interest
def identify_groups_of_interest(text):
    g = os.getenv("GROUP", "") #this reads from a local .env file which stores our curated groups of interest list
    groups = g.split(",") if g else []
    found_groups = []
    for group in groups:
        if re.search(r'\b' + re.escape(group) + r'\b', text, re.IGNORECASE):
            found_groups.append(group)
    
    return found_groups