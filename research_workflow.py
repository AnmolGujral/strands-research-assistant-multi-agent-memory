#!/usr/bin/env python3
"""
Research Workflow with Multi-Agent System and Memory Integration
"""
import asyncio
from strands import Agent
from strands.models import BedrockModel
from strands_tools import http_request
from memory_agent import check_memory_for_query, store_query_result

bedrock_model = BedrockModel(model_id="us.amazon.nova-lite-v1:0", temperature=0.1)

async def parallel_research(sources, query):
    # Placeholder for parallel web requests using http_request tool
    tasks = []
    for src in sources:
        # In real code, you would call the tool via agent; here we mock URLs
        tasks.append(asyncio.sleep(0.1, result=f"Fetched from {src} about '{query}'"))
    results = await asyncio.gather(*tasks)
    return results

def run_research_workflow(user_input):
    # Check memory first
    previous_result = check_memory_for_query(user_input)
    if previous_result:
        return f"Found previous research in memory:{previous_result}"

    # Step 1: Researcher Agent (prompts not changed)
    researcher_agent = Agent(
        model=bedrock_model,
        system_prompt=(
            "You are a Researcher Agent that gathers information from the web. "
            "1. Determine if the input is a research query or factual claim "
            "2. Use your research tools (http_request, retrieve) to find relevant information "
            "3. Include source URLs and keep findings under 500 words"
        ),
        tools=[http_request]
    )
    sources = ["https://example.com", "https://example.org"]
    research_findings = asyncio.run(parallel_research(sources, user_input))

    # Step 2: Analyst Agent
    analyst_agent = Agent(
        model=bedrock_model,
        system_prompt=(
            "You are an Analyst Agent that verifies information. "
            "1. For factual claims: Rate accuracy from 1-5 and correct if needed "
            "2. For research queries: Identify 3-5 key insights "
            "3. Evaluate source reliability and keep analysis under 400 words"
        ),
    )
    analysis = analyst_agent(f"Analyze: {research_findings}")

    # Step 3: Writer Agent
    writer_agent = Agent(
        model=bedrock_model,
        system_prompt=(
            "You are a Writer Agent that creates clear reports. "
            "1. For fact-checks: State whether claims are true or false "
            "2. Include optional charts/ASCII visuals if helpful. "
            "3. For research: Present key insights in a logical structure "
            "4. Keep reports under 500 words with brief source mentions "
            "5. Provide 'Want more details? Ask follow-up questions!' at the end. "
        )
    )
    final_report = writer_agent(f"Report on '{user_input}' based on this analysis: {analysis}")

    # Store in memory
    store_query_result(user_input, str(final_report))
    return final_report
