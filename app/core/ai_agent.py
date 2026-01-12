from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from langchain_core.messages import HumanMessage, SystemMessage

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):

    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )

    # Build proper LangChain message objects for the agent (prompt already applied)
    messages = []

    for msg in query:
        if isinstance(msg, str):
            messages.append(HumanMessage(content=msg))
        else:
            messages.append(msg)

    state = {"messages": messages}

    try:
        response = agent.invoke(state)
    except Exception as e:
        logger.exception("Agent invocation failed")
        raise CustomException("Failed to invoke agent", e)

    messages_out = response.get("messages") if isinstance(response, dict) else None
    if not messages_out:
        logger.error("Agent returned no messages, response: %s", response)
        raise CustomException("Agent returned no messages", response)

    ai_messages = [m.content for m in messages_out if isinstance(m, AIMessage)]
    if not ai_messages:
        logger.error("No AIMessage found in response, response: %s", response)
        raise CustomException("No AIMessage found in agent response", response)

    return ai_messages[-1]






