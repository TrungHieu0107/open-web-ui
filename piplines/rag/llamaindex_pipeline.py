"""
title: Llama Index Pipeline
author: open-webui
date: 2024-05-30
version: 1.0
license: MIT
description: A pipeline for retrieving relevant information from a knowledge base using the Llama Index library.
requirements: llama-index
"""

from typing import List, Union, Generator, Iterator
from pydantic import BaseModel


class Pipeline():
    class Valves(BaseModel):
        # Add your custom parameters here
        openai_api_key: str = ""

    def __init__(self):
        self.documents = None
        self.index = None

    async def on_startup(self):
        from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

        self.documents = SimpleDirectoryReader("/app/docs").load_data()
        self.index = VectorStoreIndex.from_documents(self.documents)
        # This function is called when the server is started.
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom RAG pipeline.
        # Typically, you would retrieve relevant information from your knowledge base and synthesize it to generate a response.

        print(messages)
        print(user_message)

        return user_message