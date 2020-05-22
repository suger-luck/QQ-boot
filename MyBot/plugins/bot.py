from pprint import pprint
import nonebot
from nonebot import on_request, RequestSession, on_notice, NoticeSession

bot = nonebot.get_bot()

# asyns:异步，private:私聊消息，收到私聊消息，群聊是:group
@bot.on_message('private')
async def handle_msg(ctx):
    pprint(ctx)
    msg = str('别和我说话，说话就是复读机:'+ ctx['raw_message'])
    user_id = ctx['user_id']
    await bot.send_private_msg(user_id=user_id, message=msg)

# 群聊消息
# 发布群公告
# bot._send_group_notice(group_id=群号,title=群公告标题,content=群公告内容)
@bot.on_message('group')
async def group_speak(ctx):
    # 如果是谁说话
    print(ctx['group_id'])
    group_id = ctx['group_id']
    if  group_id == 1091479317:
        # msg = str('别说话说，话就是复读机：' + ctx['raw_message'])
        await bot.send_group_msg(group_id=group_id, message='说的对')
        # await bot.send_group_msg(group_id=907802900, message=msg)
        #user_id = ctx['user_id']
        #if user_id == 1362951170:
         #   await bot.send_group_msg(group_id=group_id, message='说的对')


"""
# 处理是否可以加群
@on_request('group')
async def group_add(session:RequestSession):
    # 判断验证消息是否正确,后面的是验证内容
    if session.ctx['comment'] == '验证消息':
        # 验证消息正确，同意加群
        await session.approve()
        return
    # 验证事物拒绝加群
    await session.reject('请输入验证信息')

# 将函数注册为群成员增加通知处理器
@on_notice('group_increease')
async def group_hello(session: NoticeSession):
    print('有新人来了')
    await session.send('欢迎新朋友')
    
"""


