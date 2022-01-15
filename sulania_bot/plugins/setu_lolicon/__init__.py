from aiocqhttp import MessageSegment
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message
from nonebot.params import State, CommandArg
from . import get_setu_json

setu = on_command("setu", rule=to_me(), priority=5)


@setu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State = State(), args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        state["type"] = plain_text


@setu.got("type", prompt="色图？")
async def handle_city(bot: Bot, event: Event, state: T_State = State()):
    typek = state["type"]
    if typek not in ["r18", "n18"]:
        await setu.reject("请重新输入！")
    else:
        await get_setu(typek)
    await setu.finish()


async def get_setu(typek: str):
    menu = await get_setu_json.get_url(typek)
    # setu_url = menu.json()['data'][0]['url'].replace("cat", "re")   对传回来的涩图网址进行数据提取
    await setu.send(message=MessageSegment.image(menu))
    return
