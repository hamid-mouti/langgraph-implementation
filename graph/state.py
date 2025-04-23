from typing import List, TypedDict
from langchain_core.documents import Document
class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """
    #messages: Annotated[Sequence[BaseMessage], add_messages]
    question: str
    generation: str
    web_search: bool
    documents: List[Document]
    loop_counter: int
