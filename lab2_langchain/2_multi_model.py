#!/usr/bin/env python3
"""
Task 2: Multi-Model Support - One Interface, Many Providers!
Test OpenAI, Google, and Anthropic models using the same LangChain interface.

Learning Goal: Experience provider flexibility without code changes.
"""

import os
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

def get_context(content):
    if isinstance(content, str):
        return content
    else:
        return content[0]["text"]
def main():
    print("🎯 Task 2: Multi-Model Support with LangChain")
    print("=" * 50)

    print("\n🌐 Initialize Multiple AI Providers")
    print("=" * 50)

    # TODO 1: Initialize OpenAI model
    print("Setting up OpenAI GPT-4o-mini...")
    openai_llm = ChatOpenAI(
        model="gpt-4o-mini",                    # Replace ___ with: "gpt-5.6-luna"
        api_key=os.getenv("OPENAI_API_KEY"),      # Replace ___ with: "OPENAI_API_KEY"
    )

    # TODO 2: Initialize Google Gemini model
    print("Setting up Google Gemini...")
    google_llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",                    # Replace ___ with: "google/gemini-2.5-flash"
        api_key=os.getenv("GOOGLE_API_KEY"),      # Replace ___ with: "OPENAI_API_KEY"    # Replace ___ with: "OPENAI_API_BASE"
    )

    # TODO 3: Initialize anthropic
    print("Setting up Anthropic...")
    anthropic_llm = ChatAnthropic(
        model="claude-haiku-4-5-20251001",                    # Replace ___ with: "x-ai/grok-code-fast-1"
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),      # Replace ___ with: "OPENAI_API_KEY"
    )

    # Compare all models with the same prompt
    print("\n✅ All models initialized! Now let's compare them...")
    print("\nModel Comparison - Same Prompt, Different Models")
    print("=" * 50)

    test_prompt = "Explain cloud computing in one sentence"
    print(f"📝 Prompt: '{test_prompt}'\n")

    # Test all models with the same prompt
    if openai_llm:
        response = openai_llm.invoke(test_prompt)
        print(f"OpenAI: {response.content[:100]}...")

    if google_llm:
        response = google_llm.invoke(test_prompt)
        print(f"Google: {get_context(response.content)[:100]}...")

    if anthropic_llm:
        response = anthropic_llm.invoke(test_prompt)
        print(f"Anthropic: {response.content[:100]}...")

    print("\n💡 Same code, different providers - perfect for A/B testing!")



    print("\n✅ Task 2 completed! You can now switch models at will!")
    print("🎉 You tested 3 different AI providers with identical code!")

if __name__ == "__main__":
    main()