from textwrap import dedent

from crewai import Agent

from tools import ExaSearchToolset

class HealthReportAgents() :
    def summarizer_agent(self):
        return Agent(
            role='Medical Report Summarizer',
            goal='Analyze the blood test report, summarizing it in an easy-to-understand manner, mentioning details about all the biomarkers.',
            tools= ExaSearchToolset.tools(),
            backstory=dedent("""\
                As a Medical Report Summarizer, your mission is to meticulously analyze blood test reports.
                You will break down complex medical jargon into clear, concise summaries, providing insights
                into each biomarker's significance. Your summaries will empower individuals with a better
                understanding of their health status and guide them towards informed health decisions."""),
            verbose=True
        )


    def web_searcher_agent(self):
        return Agent(
            role='Web Searcher Agent',
            goal=" search the web for articles tailored to the person's health needs based on the blood test results.",
            tools=ExaSearchToolset.tools(),
            backstory=dedent("""\
                As a Web Searcher Agent, your mission is to utilize advanced search tools to find
                relevant articles and resources that address an individual's specific health needs
                based on their blood test results. You will identify and provide links to the most
                relevant and informative articles, ensuring the individual receives accurate and
                valuable health information to understand and manage their condition effectively."""),
            verbose=True
        )