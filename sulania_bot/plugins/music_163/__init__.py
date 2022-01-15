from nonebot.adapters import Bot, Event, Message
from aiocqhttp import MessageSegment
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from . import requests_to_163
from nonebot.params import State, CommandArg

music = on_command("音乐", rule=to_me(), priority=5)


@music.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State = State(), args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        state["type"] = plain_text


@music.got("type", prompt="你想要听什么歌？")
async def handle_city(bot: Bot, event: Event, state: T_State = State()):
    typek = state["type"]
    if not typek:
        await music.reject("我没有听说过空白的歌哦~")
    else:
        await get_music(typek)
    await music.finish()


async def get_music(musick: str):
    music_get = await(requests_to_163.get(musick))
    await music.send(message=MessageSegment.music(type_=163, id_=music_get))
    return
