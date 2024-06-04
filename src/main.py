from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

print("## Welcome to the Health Report Crew ##")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    # Convert PDF to a list of image objects
    pages = convert_from_path(pdf_path, 300)  # 300 is the resolution in DPI

    # Extract text from each page
    full_text = ""
    for page_num, img in enumerate(pages):
        text = pytesseract.image_to_string(img)
        full_text += f"Text from page {page_num + 1}:\n{text}\n"
    
    return full_text

# Specify the path to your PDF
pdf_path = 'BTreport.pdf'
# Extract and print the text
extracted_text = extract_text_from_pdf(pdf_path)



from tasks import HealthReportTasks
from agents import HealthReportAgents

tasks = HealthReportTasks()
agents = HealthReportAgents()

# Create Agents
summarizer_agent = agents.summarizer_agent()
web_searcher_agent = agents.web_searcher_agent()

# Create Tasks
summarize_task = tasks.summarize_task(summarizer_agent, extracted_text)
web_searching_task = tasks.web_searching_task(web_searcher_agent, web_searcher_agent)

web_searching_task.context = [summarize_task]


# Create Crew responsible for Copy
crew = Crew(
	agents=[
		summarizer_agent,
		web_searcher_agent
	],
	tasks=[
		summarize_task,
		web_searching_task
	]
)

result = crew.kickoff()


# Print results
print("## Here is the result")
print(result)
