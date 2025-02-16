import json
import asyncio
from tools.search import ecommerce_search_aggregator
from tools.shipping import shipping_time_estimator
from tools.discount import discount_checker
from tools.competitor import competitor_price_comparison
from tools.returns import return_policy_checker
from .reasoning import ReasoningEngine
from .memory import Memory
from utils.parser import extract_parameters
from utils.logger import logger

class ShoppingAgent:
    def __init__(self):
        self.tools = {
            "search": ecommerce_search_aggregator,
            "shipping": shipping_time_estimator,
            "discount": discount_checker,
            "competitor": competitor_price_comparison,
            "returns": return_policy_checker,
        }
        self.reasoning_engine = ReasoningEngine()
        self.memory = Memory()

    async def respond(self, query):
        """Generate a response using ReAct-style reasoning."""
        logger.info(f"Received query: {query}")
        
        # Parse the query and get reasoning steps
        tool_names, reasoning_steps = self.reasoning_engine.parse_query(query)
        if not tool_names:
            logger.warning("Could not understand the query.")
            return "I'm sorry, I couldn't understand your request. Please try again."
        
        # Extract parameters using the parser utility
        params = extract_parameters(query)
        logger.info(f"Extracted parameters: {params}")
        
        # Invoke tools asynchronously and collect results
        responses = {}
        for tool_name in tool_names:
            try:
                # Filter parameters based on the tool being invoked
                filtered_params = self.filter_parameters(tool_name, params)
                logger.info(f"Filtered parameters for {tool_name}: {filtered_params}")
                
                # Invoke the tool asynchronously
                tool_output = await self.tools[tool_name](**filtered_params)
                responses[tool_name] = tool_output
            except Exception as e:
                logger.error(f"Tool execution failed for {tool_name}: {e}")
                responses[tool_name] = {"error": f"Tool execution failed: {e}"}
        
        # Integrate the outputs into a coherent response
        response = self.format_response(responses, reasoning_steps)
        logger.info(f"Generated response: {response}")
        
        # Store the interaction in memory
        self.memory.add_interaction(query, response)
        
        return response

    def filter_parameters(self, tool_name, params):
        """Filter parameters to only include those required by the tool."""
        if tool_name == "search":
            return {
                "product_name": params.get("product_name"),
                "color": params.get("color"),
                "price_range": params.get("price_range"),
                "size": params.get("size"),
            }
        elif tool_name == "shipping":
            return {
                "product_name": params.get("product_name"),
                "size": params.get("size"),
                "user_location": "New York",  # Mock user location
                "delivery_date": params.get("delivery_date"),
            }
        elif tool_name == "discount":
            return {
                "base_price": params.get("price_range", 0),  # Default to 0 if not provided
                "promo_code": params.get("promo_code"),
            }
        elif tool_name == "competitor":
            return {
                "product_name": params.get("product_name"),
                "price": params.get("price_range"),
            }
        elif tool_name == "returns":
            return {
                "site": params.get("site"),
            }
        return {}

    def format_response(self, responses, reasoning_steps):
        """Format the tool outputs and reasoning steps into a user-friendly response."""
        response = "Reasoning Steps:\n"
        for step in reasoning_steps:
            response += f"- {step}\n"
        
        response += "\nResults:\n"
        for tool_name, tool_output in responses.items():
            if "error" in tool_output:
                response += f"\n{tool_name.capitalize()} Error: {tool_output['error']}"
            else:
                response += f"\n{tool_name.capitalize()} Results: {json.dumps(tool_output, indent=2)}"
        
        return response