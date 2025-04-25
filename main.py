import random
import re
from astrbot.api import logger
from astrbot.api.event import filter
from astrbot.api.star import Context, Star, register
from astrbot.core.platform.sources.aiocqhttp.aiocqhttp_message_event import (
    AiocqhttpMessageEvent,
)


@register(
    "question_responder",
    "YourName",
    "匹配‘*不*’疑问句并根据前字符随机回复的插件",
    "1.0.0",
)
class QuestionResponderPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.regex(r".*([\w\u4e00-\u9fff\U0001f000-\U0001ffff])不\1.*")
    async def check_question(self, event: AiocqhttpMessageEvent):
        sender_id = event.get_sender_id()
        message_str = event.message_str.strip()  # 去除首尾空白字符

        match = re.match(r".*([\w\u4e00-\u9fff\U0001f000-\U0001ffff])不\1.*", message_str)
        if match:
            char = match.group(1) 
            response = random.choice([char, f"不{char}"])
            yield event.plain_result(response)
