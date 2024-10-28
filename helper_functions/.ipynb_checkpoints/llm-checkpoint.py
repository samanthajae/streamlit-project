import os
import re
import numpy as np
import pandas as pd
import json
import tiktoken
import requests

from urllib.request import urlopen
from datetime import datetime
from htmldate import find_date
from bs4 import BeautifulSoup
from goose3 import Goose
from dotenv import load_dotenv

from openai import OpenAI
from getpass import getpass

load_dotenv('.env')

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('KEY'))

def get_embedding(input, model='text-embedding-3-small'):
    response = client.embeddings.create(
        input=input,
        model=model
    )
    return [x.embedding for x in response.data]


#helper function for calling LLM
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

#takes in "messages" as parameter
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

#open file
def read_urls_from_file(input_file):
    urls = input_file.readlines()
    return [url.strip() for url in urls if url.strip()]

#extract text data from URLs
def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title
        title = soup.title.string if soup.title else 'No title found'
        
        # Extract the publish date
        date = None
        date_meta = soup.find('meta', {'property': 'article:published_time'})
        if date_meta:
            date = date_meta['content']
        
        # Extract text content
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])

        # Identify potential regions or countries (simple keyword matching)
        regions_or_countries = identify_regions_or_countries(text_content)
        groups = identify_groups_of_interest(text_content)

        return {
            'Title': title,
            'Date': date,
            'Region': regions_or_countries,
            'Group(s) of Interest': groups,
            'Content': text_content
        }
    except Exception as e:
        return {'error': str(e)}

#identify countries or regions mentioned
def identify_regions_or_countries(text):
    # Simple list of countries
    countries = ['US','Indonesia', 'Malaysia', 'North Korea', 'Israel', 'Cuba', 'Philippines', 'Iran', 'Iraq']
    found_countries = []
    
    for country in countries:
        if re.search(r'\b' + re.escape(country) + r'\b', text, re.IGNORECASE):
            found_countries.append(country)
    
    return found_countries

#identify groups of interest
def identify_groups_of_interest(text):
    g = os.getenv("GROUP", "") #this reads from a local .env file which stores our curated groups of interest list
    groups = g.split(",") if g else []
    found_groups = []
    for group in groups:
        if re.search(r'\b' + re.escape(group) + r'\b', text, re.IGNORECASE):
            found_groups.append(group)
    
    return found_groups