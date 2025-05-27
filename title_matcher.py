# Module to use LLM for identifying the correct title among search results.
from gemini_api import configure_gemini, match_title_with_gemini

def match_title_with_llm(search_results, target_title, model=None):
    """Uses Gemini LLM to match the target title with search results."""
    if model is None:
        model = configure_gemini()
    return match_title_with_gemini(model, target_title, search_results)