#!/usr/bin/env python3
"""
Task 2: Initialize the OpenAI Client
Learn how to connect to OpenAI's servers.
"""

import openai
import os
from dotenv import load_dotenv

load_dotenv()
# The OpenAI client needs two things:
# 1. API Key - Your authentication (like a password)
# 2. Base URL - Where to send requests (like an address)

# TODO: Initialize the OpenAI client
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),    # TODO: Use "OPENAI_API_KEY"
    base_url=os.getenv("OPENAI_API_BASE")     # TODO: Use "OPENAI_API_BASE"
)

print("✅ Step 2 Complete: Connected to OpenAI!")
print(f"- API Key: {os.getenv('OPENAI_API_KEY')[:3]}...")
print(f"- Base URL: {os.getenv('OPENAI_API_BASE')}")

