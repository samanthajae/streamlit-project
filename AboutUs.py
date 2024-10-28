import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About Us"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About The Summarizer App")

with st.expander("Project Scope/Objectives"):
    st.write("1. Aims to provide users with a powerful tool to summarize multiple, complex articles into concise, easily digestible bullet-point content")
    st.write("2. Leverages natural language processing (NLP) algorithms to highlight key insights and details from text data and present them in a customizable format")
    st.write("3. Allows for greater efficiency to identify content of interest without the user having to read through many lengthy articles")

with st.expander("Data Sources & Features"):
    st.write("Data Source: Article URLs")
    st.write("Features: Designed with a user-friendly interface where one can upload a text file with the URLs of articles to retrieve content summary")
        
with st.expander("How To Use This App"):
    st.write("1. Copy/paste URLs of articles to be summarized and save as a single text file. Ensure each URL is on a separate line, no spacing between URLs.")
    st.write("2. Open the streamlit project folder on VS Code and click on main.py")
    st.write("3. Launch the streamlit App by opening a new terminal and running the following line: streamlit run main.py")
    st.write("4. Upload your text file with URLs using the App button. Summaries of the text content will be generated.")
    st.write("5. To save the output, click on the Download button. Voilà!")