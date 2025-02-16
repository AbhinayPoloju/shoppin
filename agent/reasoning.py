from utils.logger import logger

class ReasoningEngine:
    def __init__(self):
        self.reasoning_steps = []

    def parse_query(self, query):
        """Use ReAct-style reasoning to parse the query and identify multiple intents."""
        self.reasoning_steps = [
            "Identify the user's intent.",
            "Determine which tools are needed.",
            "Extract relevant parameters from the query.",
        ]
        
        tool_names = []
        
        # Check for search intent
        if "find" in query.lower() or "search" in query.lower():
            tool_names.append("search")
            self.reasoning_steps.append("Identified intent: Search for products.")
        
        # Check for shipping intent
        if "shipping" in query.lower() or "arrive" in query.lower():
            tool_names.append("shipping")
            self.reasoning_steps.append("Identified intent: Estimate shipping time and cost.")
        
        # Check for discount intent
        if "discount" in query.lower() or "promo" in query.lower():
            tool_names.append("discount")
            self.reasoning_steps.append("Identified intent: Apply discount codes.")
        
        # Check for competitor intent
        if "compare" in query.lower() or "competitor" in query.lower() or "better deals" in query.lower():
            tool_names.append("competitor")
            self.reasoning_steps.append("Identified intent: Compare prices across competitors.")
        
        # Check for returns intent
        if "return" in query.lower() or "policy" in query.lower():
            tool_names.append("returns")
            self.reasoning_steps.append("Identified intent: Check return policies.")
        
        if not tool_names:
            self.reasoning_steps.append("Could not identify intent.")
        
        return tool_names, self.reasoning_steps