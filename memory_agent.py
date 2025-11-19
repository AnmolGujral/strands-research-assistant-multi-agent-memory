#!/usr/bin/env python3
"""
Memory Agent for storing and retrieving user information
"""
from strands import Agent
from strands.models import BedrockModel
from strands_tools import mem0_memory

bedrock_model = BedrockModel(model_id='us.amazon.nova-pro-v1:0', temperature=0.1)
USER_ID = 'J'

memory_agent = Agent(model=bedrock_model, system_prompt="Memory agent", tools=[mem0_memory])

# Simple in-memory store for demo
memory_store = {}

def check_memory_for_query(query):
    return memory_store.get(query)

def store_query_result(query, result):
    memory_store[query] = result
