from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel
from typing import Optional

class IMDbMatch(BaseModel):
    title: Optional[str]
    url: Optional[str]

# Load environment variables
load_dotenv()

def configure_gemini():
    """Configure the Gemini API with the provided API key."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")

    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",  # Using Flash 2.0 model
        google_api_key=api_key,
        convert_system_message_to_human=True,
        temperature=0.7,
        top_p=0.9,  # Add Flash-specific parameters
        max_output_tokens=2048
    )

def match_title_with_gemini(model, target_title, search_results):
    """Use Gemini to find the best match for the target title among search results."""
    try:
        prompt = f"""
        Task: Find the best matching IMDb title for "{target_title}" from these search results:
        {search_results}
        
        Return ONLY a JSON object like this:
        {{"title": "<exact title from results>", "url": "<corresponding url>"}}
        
        If no good match found, return: {{"title": null, "url": null}}
        """
        
        # Use LangChain's chat interface instead of generate_content
        messages = [HumanMessage(content=prompt)]
        response = model.invoke(messages)
        
        # Extract text from LangChain response
        response_text = response.content
        return json.loads(response_text)
    except Exception as e:
        print(f"Error matching title: {e}")
        return {"title": None, "url": None}