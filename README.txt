***PROBLEM STATEMENT***
Key tasks for one of our Ops teams is to identify articles/content of interest. Given specific keywords, the team receives hundreds of links via a media trawler and has to manually look through each link to determine if the content is relevant. 

This process is time-consuming, tedious and requires several personnel. There is also the challenge of processing articles which are not in English.

After identifying relevant content, the Ops team has to prepare slides with key summary information from the articles for presentation.


***PROJECT OBJECTIVE*** 
For this project, we sought to enhance efficiency for the Ops team by streamlining the process. We created a summary tool that reads, compiles and extracts text data from multiple article URLs and leverages LLMs to provide summaries of important points in each article.


***ENVISIONED OUTCOME***
The output reduces the processing time significantly, e.g. it may typically take 2-3 personnel around 30 minutes to manually look through 50 articles. With the help of our Summarizer App, it only requires 1 personnel to upload the URLs, launch the app and identify relevant articles within 5-10 minutes.


***IMPORTANT NOTE***
We created a Streamlit App version but noticed that the App performs significantly worse than the original no-frills Python script version. 

Some challenges faced with the Streamlit App include not being able to properly process the following process data:
- Text files with more than 3 URLs
- Content that is not in English
- Articles from certain websites

However, there were no issues faced processing articles with the original Python script. As such, we are also sharing our Python script via Google Collab. 

***ACCESS LINK***
https://colab.research.google.com/drive/1aTWoTzpjBqqWP4edVDANscQHZNfuy-4M