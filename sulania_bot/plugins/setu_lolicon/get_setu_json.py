import httpx
from typing import Optional
from nonebot import logger


async def get_url(typek:str) -> Optional[str]:
    async with httpx.AsyncClient() as client:
        try:
            url = 'https://api.lolicon.app/setu?r18='
            if typek == 'r18':
                url += '1'
            else:
                url += '0'
            r = await client.get(url=url)
            pic_url = r.json()['data'][0]['url'].replace("cat", "re")
            return pic_url
        except Exception as e:
            logger.error(f' {type(e)}：{e}')
            return None