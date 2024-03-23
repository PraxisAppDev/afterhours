from typing import AsyncIterator
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from asyncio import Queue

def handle_object_id(document):
  document["_id"] = str(document["_id"])
  return document

def stream_jsonl_response(stream: AsyncIterator[BaseModel]) -> StreamingResponse:
  async def mapped_stream(stream_to_map):
    async for obj in stream_to_map:
      yield obj.model_dump_json() + '\n'
  return StreamingResponse(mapped_stream(stream), media_type="application/x-ndjson")

class DatabaseChangeStream:
    def __init__(self):
        self._queues = set()

    async def add_change(self, change):
        for queue in self._queues:
            await queue.put(change)
    
    async def __aiter__(self):
        queue = Queue()
        self._queues.add(queue)
        try:
            while True:
                yield await queue.get()
        except StopAsyncIteration:
            self._queues.remove(queue)