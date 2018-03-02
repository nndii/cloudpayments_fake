import ujson

import aiohttp.web

from .resources import Transaction


async def send_to(url: str, transaction: Transaction) -> int:
    params = await transaction.jsonify()
    async with aiohttp.ClientSession(
            json_serialize=ujson.dumps,
            headers={'Content-Type': ''}) as session:
        async with session.post(url, data=params) as resp:
            status = await resp.json()

            if 'code' not in status:
                return 55
            else:
                return status['code']