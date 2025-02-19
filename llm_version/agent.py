import os
from huggingface_hub import InferenceClient
from tools import (
    ecommerce_search_aggregator,
    shipping_time_estimator,
    discount_checker,
    competitor_price_comparison,
    return_policy_checker,
)

# Using Mixtral 8x7B which is available through the API
MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# System prompt to define the agent's role and capabilities
SYSTEM_PROMPT = """
You are a virtual shopping assistant that helps users find fashion items online. You have access to the following tools:
1. E-Commerce Search Aggregator: Search for products based on name, color, price range, and size.
2. Shipping Time Estimator: Check shipping feasibility, cost, and delivery date.
3. Discount Checker: Apply promo codes to calculate final prices.
4. Competitor Price Comparison: Compare prices of a product across different sites.
5. Return Policy Checker: Provide return policy details for a given site.

Use the following format to invoke tools:
TOOL: <tool_name>
INPUT: <input_parameters>
After receiving the tool's output, integrate it into your response to the user.
"""

def invoke_tool(tool_name, input_parameters):
    """Invoke the appropriate tool based on the tool name."""
    if tool_name == "E-Commerce Search Aggregator":
        return ecommerce_search_aggregator(**input_parameters)
    elif tool_name == "Shipping Time Estimator":
        return shipping_time_estimator(**input_parameters)
    elif tool_name == "Discount Checker":
        return discount_checker(**input_parameters)
    elif tool_name == "Competitor Price Comparison":
        return competitor_price_comparison(**input_parameters)
    elif tool_name == "Return Policy Checker":
        return return_policy_checker(**input_parameters)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")

def format_prompt(messages):
    """Format messages for Mixtral model."""
    formatted_prompt = "<s>"
    for message in messages:
        if message["role"] == "system":
            formatted_prompt += f"[INST] {message['content']} [/INST]"
        elif message["role"] == "user":
            formatted_prompt += f"[INST] {message['content']} [/INST]"
        elif message["role"] == "assistant":
            formatted_prompt += f"{message['content']}"
    return formatted_prompt + "</s>"

def run_agent(user_query):
    """Run the agent to process the user query."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ]

    # Initialize the client with your API key
    client = InferenceClient(
        model=MODEL_NAME,
        token = os.getenv("HF_TOKEN")
    )
    
    try:
        # Generate initial response
        formatted_prompt = format_prompt(messages)
        response = client.text_generation(
            prompt=formatted_prompt,
            max_new_tokens=500,
            temperature=0.7,
            stop=["</s>", "[INST]"]
        )
        agent_response = response
        
        # Parse and execute tool calls if present
        if "TOOL:" in agent_response:
            tool_call = agent_response.split("TOOL:")[1].strip()
            tool_name = tool_call.split("\n")[0].strip()
            try:
                input_parameters = eval(tool_call.split("INPUT:")[1].strip())
                tool_output = invoke_tool(tool_name, input_parameters)

                # Generate final response with tool output
                messages.append({"role": "assistant", "content": agent_response})
                messages.append({"role": "user", "content": f"Tool Output: {tool_output}"})
                
                formatted_prompt = format_prompt(messages)
                final_response = client.text_generation(
                    prompt=formatted_prompt,
                    max_new_tokens=500,
                    temperature=0.7,
                    stop=["</s>", "[INST]"]
                )
                return final_response
            except Exception as e:
                return f"Error processing tool call: {e}\nOriginal response: {agent_response}"
        else:
            return agent_response
            
    except Exception as e:
        return f"Error generating response: {e}"

# Example usage
if __name__ == "__main__":
    test_queries = [
        "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?",
        "I need white sneakers (size 8) for under $70 that can arrive by Friday.",
        "I found a 'casual denim jacket' at $80 on SiteA. Any better deals?",
        "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?",
        "Find a black leather jacket under $100, check shipping to New York by next Monday, and compare prices with SiteC."
    ]
    
    print("Testing shopping assistant with multiple queries...")
    for query in test_queries:
        print("\nTask:", query)
        print(run_agent(query))
        print("---")
