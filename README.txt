***PROBLEM STATEMENT***
Key task is to efficiently identify articles/content of interest. Given specific keywords, one of our teams receives hundreds of links via media platform and manually browse links to determine if the content is relevant. This process is time-consuming, tedious and requires several personnel. There is also the challenge of processing articles which are not in English. After identifying relevant content, the team has to prepare slides with key summary information from the articles for presentation.


***PROJECT OBJECTIVE*** 
This project seeks to enhance efficiency by streamlining the process via a Summarizer App. This tool reads, compiles and extracts text data from multiple article URLs, leveraging LLMs to provide summaries of important points in each article.


***ENVISIONED OUTCOME***
The App will significantly reduce the processing time to identify relevant content. The App also assists the team in preparing summary slides, where key information such as date, countries and groups of interest may be automatically extracted and important developments are highlighted. To note, it is still imperative to fact-check the accuracy of the output.


***IMPORTANT NOTE***
We created a Streamlit App version but noticed that the App performs significantly worse than the original no-frills Python script version. Some challenges faced with the Streamlit App include not being able to properly process the following data:
- Text files with more than 3 URLs
- Content that is not in English
- Articles from certain websites

However, there were no issues faced processing articles with the original Python script. As such, we are also sharing our Python script via Google Collab. 

***ACCESS LINK***
https://colab.research.google.com/drive/1aTWoTzpjBqqWP4edVDANscQHZNfuy-4M
