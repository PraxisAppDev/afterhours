from typing import AsyncIterator
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from asyncio import Queue
import json

def handle_object_id(document):
  document["_id"] = str(document["_id"])
  return document

def stream_jsonl_response(stream: AsyncIterator) -> StreamingResponse:
  async def mapped_stream(stream_to_map):
    async for obj in stream_to_map:
      yield json.dumps(obj) + '\n'
  return StreamingResponse(mapped_stream(stream), media_type="application/x-ndjson")

class DatabaseChangeStream:
  def __init__(self):
    self._queues = {}

  async def add_change(self, bucket, change):
    for queue in self._queues.get(bucket, []):
      await queue.put(change)

  async def listen(self, *buckets):
    queue = Queue()
    for bucket in buckets:
      self._queues.setdefault(bucket, []).append(queue)
    try:
      while True:
        change = await queue.get()
        yield change
    finally:
      for bucket in buckets:
        self._queues[bucket].remove(queue)