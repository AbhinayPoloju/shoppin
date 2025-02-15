# agent/reasoning.py

from utils.logger import logger

class ReasoningEngine:
    def __init__(self):
        self.reasoning_steps = []

    def parse_query(self, query):
        """Use ReAct-style reasoning to parse the query."""
        self.reasoning_steps = [
            "Identify the user's intent.",
            "Determine which tools are needed.",
            "Extract relevant parameters from the query.",
        ]
        
        # Check for competitor price comparison intent
        if "better deal" in query.lower() or "compare" in query.lower() or "competitor" in query.lower():
            self.reasoning_steps.append("Identified intent: Compare prices across competitors.")
            return "competitor", self.reasoning_steps
        
        # Check for search intent
        if "find" in query.lower() or "search" in query.lower():
            self.reasoning_steps.append("Identified intent: Search for products.")
            return "search", self.reasoning_steps
        
        # Check for shipping intent
        if "shipping" in query.lower() or "arrive" in query.lower():
            self.reasoning_steps.append("Identified intent: Estimate shipping time and cost.")
            return "shipping", self.reasoning_steps
        
        # Check for discount intent
        if "discount" in query.lower() or "promo" in query.lower():
            self.reasoning_steps.append("Identified intent: Apply discount codes.")
            return "discount", self.reasoning_steps
        
        # Check for returns intent
        if "return" in query.lower() or "policy" in query.lower():
            self.reasoning_steps.append("Identified intent: Check return policies.")
            return "returns", self.reasoning_steps
        
        # Default to None if no intent is identified
        self.reasoning_steps.append("Could not identify intent.")
        return None, self.reasoning_steps