import streamlit as st
import urllib.parse

# Streamlit app title and instructions
st.title("Comprehensive Social Media and Information Search (Arabic and English)")

st.write("""
This tool helps you search for individuals on multiple platforms in both English and Arabic. You can also explore potential salary information, translate text, and access any available public registries for Egypt.
""")

# Input fields for user data
name = st.text_input("Enter the name to search (in English or Arabic)")
location = st.text_input("Enter the location (optional, in English or Arabic)")
phone_number = st.text_input("Enter a phone number (optional, for Google search)")


# Function to encode search terms for URL compatibility
def encode_query(query):
    return urllib.parse.quote_plus(query)


# Button to display search links
if st.button("Generate Search Links"):
    if name:
        # Encode name and location for URL compatibility with Arabic characters
        encoded_name = encode_query(name)
        encoded_location = encode_query(location) if location else ""

        # Construct URLs with encoded search terms
        facebook_url = f"https://www.facebook.com/search/top/?q={encoded_name} {encoded_location}"
        linkedin_url = f"https://www.linkedin.com/search/results/people/?keywords={encoded_name} {encoded_location}"
        glassdoor_url = f"https://www.glassdoor.com/Reviews/{encoded_name}-reviews-SRCH.htm"
        twitter_url = f"https://twitter.com/search?q={encoded_name} {encoded_location}"

        # Display clickable links for iOS compatibility
        st.markdown(f"[Search '{name}' on Facebook]({facebook_url})")
        st.markdown(f"[Search '{name}' on LinkedIn]({linkedin_url})")
        st.markdown(f"[Search '{name}' on Glassdoor (for possible salary info)]({glassdoor_url})")
        st.markdown(f"[Search '{name}' on Twitter]({twitter_url})")

        # Message to indicate links are ready for tapping
        st.write("Tap on the links above to open each search in a new tab in your browser.")

    if phone_number:
        # Google search for the phone number
        encoded_phone_number = encode_query(phone_number)
        google_url = f"https://www.google.com/search?q={encoded_phone_number}"
        st.markdown(f"[Search for phone number on Google]({google_url})")

# Translation Link
st.subheader("Translation")
st.write("Use Google Translate to translate text between English and Arabic.")
translate_url = "https://translate.google.com"
st.markdown(f"[Open Google Translate]({translate_url})")

# Additional Information Section
st.subheader("Additional Information")
st.write("""
- **Search Tips**: Search both English and Arabic names to cover more results.
- **Glassdoor for Salaries**: Glassdoor can provide insights into salaries for certain roles. To get the best results, try searching with specific job titles.
- **Twitter**: Twitter can be useful to find recent posts, opinions, or other relevant public information.
- **Public Registries in Egypt**: There is limited access to public information in Egypt due to privacy laws. However, some sources might include:
  - [Egyptian Bar Association](https://www.egyls.com/): Search for legal professionals.
  - [Egyptian General Authority for Investment - Company Registry](https://www.gafi.gov.eg/English/Pages/default.aspx): For registered business entities in Egypt.
""")