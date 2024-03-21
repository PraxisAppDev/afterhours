from typing import AsyncIterator
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


def handle_object_id(document):
  document["_id"] = str(document["_id"])
  return document

def stream_jsonl_response(stream: AsyncIterator[BaseModel]) -> StreamingResponse:
  async def mapped_stream(stream_to_map):
    async for obj in stream_to_map:
      yield obj.model_dump_json() + '\n'
  return StreamingResponse(mapped_stream(stream), media_type="application/x-ndjson")