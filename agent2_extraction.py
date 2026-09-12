import json
import os
from google import genai
from google.genai import types

# Initialize the Gemini client using your GEMINI_API_KEY environment variable
client = genai.Client()

AGENT2_SYSTEM_PROMPT = """
You are a zoning and municipal policy extraction agent. Your job is to read raw text from city council documents and extract structured facts into JSON. You do not summarize or interpret — you only extract explicitly stated facts.

RULES:
1. Extract only explicitly stated fields. If missing, set value to null.
2. Include short source quotes/clauses in "source_clauses" for every extracted item.
3. Return a valid JSON object matching the requested schema.
"""

def run_agent_2(chunk_text: str) -> dict:
    response = client.models.generate_content(
       model="gemini-3.6-flash",
        contents=f"{AGENT2_SYSTEM_PROMPT}\n\nExtract zoning facts from this text:\n\n{chunk_text}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.0
        ),
    )
    return json.loads(response.text)

if __name__ == "__main__":
    sample_text = """
    Section 4.5 Setbacks: Plots abutting 18.0m wide roads require a front setback of 3.5m. 
    Maximum building height is capped at 15m (G+4 structure).
    """
    result = run_agent_2(sample_text)
    print(json.dumps(result, indent=2))