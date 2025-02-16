# AI Shopping Agent with ReAct-style Reasoning

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tools](#tools)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Design Decisions](#design-decisions)
- [Challenges & Improvements](#challenges--improvements)
- [Research Analysis](#research-analysis)
- [Open Questions](#open-questions)

## Features

- **ReAct-style Reasoning**: Step-by-step reasoning to determine tool usage
- **Multi-Tool Integration**: Five specialized tools for comprehensive shopping assistance
- **Natural Language Understanding**: Processes complex user queries and constraints
- **Multi-Turn Reasoning**: Maintains context across conversation turns
- **Flexible Tool Architecture**: Easily extensible with new tools and capabilities

## Architecture

```
src/
├── agent/
│   ├── reasoning.py    # ReAct reasoning implementation
│   ├── memory.py       # Conversation context management
│   └── prompt.py       # System and user prompt templates
├── tools/
│   ├── search.py       # E-commerce search aggregator
│   ├── shipping.py     # Shipping estimator
│   ├── discount.py     # Promo code validator
│   ├── competitor.py   # Price comparison
│   └── returns.py      # Return policy checker
└── utils/
    ├── parser.py       # Query parsing utilities
    └── logger.py       # Logging and monitoring
```

## 🛠 Tools

1. **E-Commerce Search Aggregator**
   - Searches products across multiple platforms
   - Filters by price, size, color, and availability

2. **Shipping Time Estimator**
   - Calculates delivery dates and costs
   - Checks feasibility for deadline-constrained orders

3. **Discount/Promo Checker**
   - Validates promotional codes
   - Calculates final prices with discounts

4. **Competitor Price Comparison**
   - Compares prices across platforms
   - Identifies best available deals

5. **Return Policy Checker**
   - Provides return policy summaries
   - Checks return window and conditions

## Installation

```bash
# Clone the repository
git clone https://github.com/AbhinayPoloju/shoppin.git
cd shoppin

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage Examples

```python
from agent.agent import ShoppingAgent

# Initialize agent
agent = ShoppingAgent()

# Example queries
queries = [
    "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?",
    "I need white sneakers (size 8) for under $70 that can arrive by Friday.",
    "I found a 'casual denim jacket' at $80 on SiteA. Any better deals?",
]

# Process queries
for query in queries:
    response = agent.process(query)
    print(f"Query: {query}\nResponse: {response}\n")
```

## Design Decisions

1. **ReAct Framework Implementation**
   - Combines reasoning and action in an interpretable way
   - Enables step-by-step decision making for tool selection

2. **Modular Tool Architecture**
   - Each tool is independent and easily replaceable
   - Standardized input/output interfaces

3. **Context Management**
   - Maintains conversation history for multi-turn interactions
   - Tracks user preferences and constraints

## Challenges & Improvements

### Current Challenges
- Limited to mock tool implementations
- Rule-based query parsing may miss complex intentions
- Tool selection could be more dynamic

### Planned Improvements
- Integration with real e-commerce APIs
- Enhanced natural language understanding
- Dynamic tool learning (Toolformer-inspired)
- Improved error handling and recovery

## Research Analysis

### Key Papers
1. ReAct: Synergizing Reasoning and Acting in Language Models
2. Toolformer: Language Models Can Teach Themselves to Use Tools
3. ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent
4. Chain of Tools: Large Language Model Automatic Tool Learning
5. Language Agent Tree Search: Reasoning, Acting, and Planning

### Methodology Comparison
- ReAct: Foundation for our reasoning system
- Toolformer: Inspiration for tool integration
- ReST: Ideas for self-improvement capabilities
- Chain of Tools: Multi-tool orchestration insights

## Open Questions

1. How can the agent dynamically learn new tools?
2. What's the optimal balance between reasoning steps and tool calls?
3. How can we improve tool selection accuracy?
4. What's the best way to handle tool failures?

