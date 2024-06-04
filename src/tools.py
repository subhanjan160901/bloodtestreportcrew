import os
from exa_py import Exa
from langchain.agents import tool

class ExaSearchToolset() :
    @tool
    def search(query:str) :
        """Search for a webpage based on the query."""
        return ExaSearchToolset._exa().search(f"{query}", use_autoprompt = True, num_results = 5)

    def tools():
        return [
            ExaSearchToolset.search
        ]
    
    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))