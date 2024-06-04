from textwrap import dedent

from crewai import Task

class HealthReportTasks() :
    def summarize_task(self, agent, extracted_text):

        return Task (
            description = dedent(f"""\
                input text = {extracted_text}
                Given input text extracted from a medical pdf report, make a list of all biomarkers, their results with unit values, the appropriate reference value given the patient data and which test the biomarker belongs to, if applicable.
                Answer should follow this template :    

                biomarker: namel

                test name: nane

                value: 3.2 mg/dL

                reference ranges: 3 to 5"""),
            expected_output = dedent(f"""\
                A comprehensive medical analysis summary that presents detailed results, 
                reference intervals, and interpretive notes to aid in clinical assessment, 
                in a conscise and easy to understand manner."""
            ),
            agent = agent,
            async_execution = True
        )

    def web_searching_task(self, agent, summarised_text):

        return Task (
            description = dedent(f"""\
                input text = {summarised_text}
                From the given input, which is the summarised text of a person's blood test report , 
                I want to search the internet for articles that fit the person's needs, i.e., 
                It should then search the web for articles tailored to the person's health needs based on the blood test results.
                Provide me only the links."""),
            expected_output = dedent(f"""\
                Links of articles tailored to the health needs based on the provided blood test results."""),
            agent = agent
        )