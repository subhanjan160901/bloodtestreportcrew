## Steps to run the code :

Easy and Simple ! Just install all the pre-dependencies from requirements.txt, and run the python script main.py

## Brief Description of the project :

### `tasks.py`
This file defines a class `HealthReportTasks` which contains methods to create specific tasks using the `Task` class from the `crewai` framework.

- **Imports**: `dedent` from `textwrap` and `Task` from `crewai`.
- **HealthReportTasks Class**:
  - **summarize_task**: Creates a task to summarize medical data extracted from a PDF report. It specifies the task's description, expected output, agent to perform the task, and sets asynchronous execution.
  - **web_searching_task**: Creates a task to search the web for articles based on summarized blood test results. It defines the task's description, expected output, and the agent responsible for execution.

### `agents.py`
This file defines a class `HealthReportAgents` which contains methods to create agents using the `Agent` class from the `crewai` framework.

- **Imports**: `dedent` from `textwrap`, `Agent` from `crewai`, and `ExaSearchToolset` from `tools`.
- **HealthReportAgents Class**:
  - **summarizer_agent**: Creates an agent with the role of "Medical Report Summarizer" to analyze and summarize blood test reports, using tools from `ExaSearchToolset`. The agent has a defined goal and backstory for guidance, with verbose output enabled.
  - **web_searcher_agent**: Creates an agent with the role of "Web Searcher Agent" to find and provide links to relevant health articles based on blood test results. This agent also uses tools from `ExaSearchToolset` and has a goal and backstory, with verbose output enabled.

### `tools.py`
This file defines a class `ExaSearchToolset` which provides a search tool that can be used by the agents.

- **Imports**: `os`, `Exa` from `exa_py`, and `tool` from `langchain.agents`.
- **ExaSearchToolset Class**:
  - **search**: A method to search for a webpage based on a query using the `Exa` API. It is decorated with `@tool`, making it available as a tool for agents.
  - **tools**: Returns a list of available tools, currently including the `search` method.
  - **_exa**: Initializes and returns an `Exa` object using an API key from environment variables.

### `main.py`
This file orchestrates the entire process of extracting text from a PDF, creating agents and tasks, and executing the tasks using a crew.

- **Imports**: Modules for PDF and image processing (`pdf2image`, `PIL`), text extraction (`pytesseract`), environment variable loading (`dotenv`), and `Crew` from `crewai`.
- **Load Environment Variables**: Using `load_dotenv` to load API keys and other configurations.
- **Welcome Message**: Prints a welcome message.
- **extract_text_from_pdf Function**: Converts a PDF to images and extracts text from each page using `pytesseract`.
- **PDF Path**: Specifies the path to the PDF file and extracts text from it.
- **Tasks and Agents Creation**: Imports and initializes `HealthReportTasks` and `HealthReportAgents`, creates summarizer and web searcher agents, and assigns tasks to these agents.
- **Task Context**: Sets the context of `web_searching_task` to include the output of `summarize_task`.
- **Crew Initialization and Execution**: Creates a `Crew` object with the agents and tasks, then kicks off the execution.
- **Results**: Prints the results of the crew's execution.

### How It Works
1. **PDF Text Extraction**: The main script extracts text from a specified PDF file.
2. **Agent and Task Setup**: It then sets up agents and tasks defined in `agents.py` and `tasks.py`.
3. **Task Execution**: The tasks are assigned to the appropriate agents, and a `Crew` is created to manage the execution.
4. **Output**: The results of the tasks are printed out.

This setup allows for automated extraction, summarization, and web searching based on medical report data using specialized agents and tasks.
