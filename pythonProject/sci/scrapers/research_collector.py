import requests
from bs4 import BeautifulSoup
import re
import openpyxl
import openai

# OpenAI API key setup
openai.api_key = "your-api-key"  # Replace with your OpenAI API key


# Function to scrape names from the SoCal Theochem webpage
def get_researcher_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Modify the selector to target the names specifically based on the webpage structure
    names = []
    for name in soup.select('some_selector'):  # Change 'some_selector' based on HTML
        names.append(name.text.strip())
    return names


# Function to find researcher lab websites (using a search engine API or scraping from known sources)
def find_lab_website(name):
    # Implement search logic here. You may need an API for Google Custom Search
    return "http://example.com/lab"  # Placeholder


# Function to extract email from a lab website
def get_email_from_website(url):
    response = requests.get(url)
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
    return emails[0] if emails else "Not found"


# Function to summarize research focus using GPT-4
def summarize_research_llm(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text content from the page
    page_text = soup.get_text()

    # Prompt the GPT-4 model to summarize the research focus in 3 words
    prompt = f"Summarize the research focus described in the following webpage text in 3 words:\n\n{page_text}"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine; or 'gpt-4' if enabled for your account
            prompt=prompt,
            max_tokens=10,  # Since we only need 3 words, a small token count should suffice
            n=1,
            stop=None,
            temperature=0.5
        )

        # Extract the summary from the response
        summary = response.choices[0].text.strip()
    except Exception as e:
        print(f"Error summarizing research focus: {e}")
        summary = "Error summarizing"

    return summary


# Function to create Excel file
def create_excel(data, filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name", "Lab Website", "Email", "Research Focus"])

    for row in data:
        ws.append(row)

    wb.save(filename)


# Main execution
url = 'https://yuenzhougroup.ucsd.edu/socaltheochem2024/program.html'
names = get_researcher_names(url)

data = []
for name in names:
    lab_website = find_lab_website(name)
    email = get_email_from_website(lab_website)
    research_focus = summarize_research_llm(lab_website)
    data.append([name, lab_website, email, research_focus])

# Save to Excel
create_excel(data, 'researchers_info_llm.xlsx')
