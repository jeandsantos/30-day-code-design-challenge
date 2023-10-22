import asyncio

import requests

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]


def http_get_sync(url: str) -> JSON:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


async def http_get(url: str) -> JSON:
    return await asyncio.to_thread(http_get_sync, url)
