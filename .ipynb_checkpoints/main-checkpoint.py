# Set up and run this Streamlit App
import streamlit as st
from helper_functions import llm

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Streamlit Summary App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Article Summarizer")

# Read file
input_file = st.file_uploader("Upload text file")
if input_file:
    urls = llm.read_urls_from_file(input_file)
    
    results = []
    for url in urls:
        data = llm.extract_data(url)
        results.append(data)
        
    lst1 = []
    for r in results:
        prompt = f"""
        Follow these steps based on the text which is delimited with triple backticks. 
        
        Step 1: For URL address, return the url address from Source with same or similar text to Title and Date. 
        If no url address is found, return the url address from results list [].
        
        Step 2: For Content, your task is to generate 3 most important key points based on the text which is delimited with triple backticks. 
        Important events or developments in the text should be highlighted. 
        Include details and information such as date, time, or topics relating to weapons, smuggling, attacks,  
        injuries, deaths, arrests, surrenders, propaganda, funding or terrorism-related matters, highlighting
        important events/ developments. The bullet points should be as concise as possible. Complete sentence is not needed.
        After processing URL, translate text Content into English if needed. Make sure the statements are factually accurate.

        Step 3: Extract Group(s) strictly based on text Content or text in results list. Make sure the statements are factually accurate.
        
        Step 4: For Category, categorize Content into one of the following labels: Propaganda, Incitement to Terror, Financing, Smuggling, Surrender, Arrest, Physical Attack, Counter-Terrorism, or Type (Group or Lone Wolf). 
        If Content cannot be categorized, please specify "Unknown".
        
        <Examples>
        Content: "celebrating the late Hamas leader, depicting as a martyr, reinforcing the idea of resistance against Israel, an alleged MYS pro-ISIS media center published a third poster focused on the anti-ISIS coalition; 
        the top half of the poster showed a picture of the Meeting of the Ministers of the Global Coalition to Counter Daesh in Washington, while the bottom half showed what it portrays to be innocents Muslim suffering from 
        attacks and bombings carried out by coalition countries"
        Category: Propaganda

        Content: "pro-ISIS media outlet uses online platforms to promote media jihad or virtual jihad; media group aligned with the Islamic State (IS) reminded jihadists of the true meaning of jihad, 
        promoted the resilience of the IS; group aligned with IS continues to issue graphics, lauding suicide attacks"
        Category: Incitement to Terror
        
        Content: "group has made frequent calls for donations to help support Jihadists, families of Jihadi prisoners, and widows of martyrs"
        Category: Financing
        
        Content: "smuggling of weapons and drugs in Zamboanga del Norte"
        Category: Smuggling
        
        Content: "AFP announced that 13 ASG members had surrendered in Sulu" 
        Category: Surrender
        
        Content: "a soldier was killed and a civilian wounded following a drive-by shooting, two attackers killed five people and wounded 22 others at the Turkish Aerospace Industries headquarters"
        Category: Physical Attack
        
        Content: "arrested under the Internal Security Act (ISA) before planned attack, DENSUS 88 arrested terrorist suspects from group supporting ISIS"
        Category: Arrest

        Content: "the National Police's counter-terrorism squad arrested 24 individuals suspected of supporting Poso-based East Indonesia Mujahideen (MIT) and the Islamic State of 
        Iraq and Syria (ISIS) terrorist groups"
        Category: Counter-Terrorism

        Content: "ISEAP-linked group threatens Philippine president with sniper attack; Singaporean ISIS fighter urged friend to stage terror attacks on crowds, tried to radicalize 
        friends on social media to  commit lone wolf attacks to crowds"
        Category: Type (Group or Lone Wolf)
        
        Extract the following information. 
        Your response MUST be in the following format:

        - URL: 
        - Title: 
        - Date: dd-MM-yyy
        - Category:
        - City:
        - State:
        - Country:
        - Group(s) of Interest:
        - Source:
        - Content:
            <bullet point #1>
            <bullet point #2>
            <bullet point #3>
        
        text: '''{r}'''
        """
        response = llm.get_completion(prompt)
        lst1.append(response)
        st.write("ARTICLE SUMMARY" + "\n")
        st.write("=" * 40 + "\n")
        st.write(response)

# Button to save responses to a text file
if st.button("Save Output"):
    if lst1:
        with open("article_summaries.txt", "w") as f:
            for idx, res in enumerate(lst1, start=1):
                f.write(f"Summary {idx}:\n")
                f.write(res + "\n\n")
        
        st.success("File saved.")
    else:
        st.warning("No summaries to save.")