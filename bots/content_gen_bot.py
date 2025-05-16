"""
Content Generation Bot for AI-Influence-as-a-Service Platform
Author: ricobiz
Implements orchestratable AI content generation using OpenAI GPT models.
Provides entrypoint for orchestrator/agents.py.
"""
import os
from typing import Dict, Any
import openai
import logging

# Load API key from environment (assumes set in deployment)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def generate_trending_content(prompt: str, max_tokens=256, model="gpt-4") -> str:
          """Generate trending campaign content using GPT-4 API."""
          try:
                        response = openai.ChatCompletion.create(
                                          model=model,
                                          messages=[{"role": "user", "content": prompt}],
                                          max_tokens=max_tokens,
                                          temperature=0.9
                        )
                        content = response['choices'][0]['message']['content']
                        logging.info(f"[ContentBot] Generated content: {content[:60]}...")
                        return content
except Exception as e:
        logging.error(f"[ContentBot] OpenAI error: {e}")
        return "[Error generating content]"

def run_content_gen_task(topic: str = "", style: str = "", platform: str = "") -> str:
          """Entrypoint for orchestrator: Generate campaign text."""
          if not topic:
                        topic = "новый тренд в социальных сетях и маркетплейсах"
                    prompt = f"Напиши кликабельный пост или заголовок для {platform or 'всех платформ'} о '{topic}' в стиле {style or 'маркетингового инфлюенсера'} для продвижения."
    return generate_trending_content(prompt)

# For direct CLI testing
if __name__ == "__main__":
          import sys
    topic = 
