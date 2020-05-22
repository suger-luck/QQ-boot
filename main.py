# # 更好看的打印
# from pprint import pprint
# from cqhttp import CQHttp
# # 这个是告诉程序:酷Q在5700端口
# bot = CQHttp(api_root='http://127.0.0.1:5700')
#
# # 告诉python 用来处理私聊消息：private，先判断是否是私聊消息
# @bot.on_message('private')
# def handle_msg(ctx):
#     """处理消息:
#     context: 接受一个上下文-->(简写)ctx:
#     包含了别人发的消息、自己的id、现在时间、他的id、你们所在的群；
#     类型：字典"""
#     # 打印字典信息
#     pprint(ctx)
#     msg = ctx['message']
#     user_id = ctx['user_id']
#     # 回复，第一个传入参数必须为ctx
#     bot.send_private_msg()
#     # bot.send(ctx,'你好呀')
#
#
# # 网站的后端：python跑在8080端口
# bot.run('127.0.0.1', 8080)

import nonebot
import config
from os import path
if __name__ == '__main__':
    nonebot.init(config)
    print(config.SUPERUSERS)
    # nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'MyBot', 'plugins'),
        'MyBot.plugins'
    )
    nonebot.run(host='127.0.0.1', port=8080)