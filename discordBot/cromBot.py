import discord
from discord.ext import commands
from dico_token import cromBotToken

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="!", help_command=None)

# 채널 ID를 저장할 전역 변수
channel_id = 1270216511914770435


@bot.event
async def on_ready():
    print(f'{bot.user}에 로그인하였습니다.')
    print(f'ID: {bot.user.name}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('명령 !로 시작'))


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="!공지 \n 의미없는 내용 \n\n !채널설정\n 해당 메세지 채널을 봇 작동 채널로 설정\n\n !계산\n 크롬계산기 실행")
    await ctx.send(embed = embed)

@bot.command()
async def 공지(ctx) :
    embed = discord.Embed(title = "공지", description = "!공지 \n 의미없는 내용 \n\n !채널설정\n 해당 메세지 채널을 봇 작동 채널로 설정\n\n !계산\n 크롬계산기 실행", color = 0x62c1cc)
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def 채널설정(ctx):
    global channel_id
    channel_id = ctx.channel.id
    await ctx.send(f"타겟 채널이 {ctx.channel.mention}으로 설정되었습니다.")

@bot.command()
async def 계산(ctx):
    # 사용자가 계산식을 입력하도록 요청
    await ctx.send("계산식을 입력하세요 (예: 1 2 3 + + 바스)\n모든 조잡한 메모 내용은 띄워쓰기 해주세요")

    # 사용자로부터 메시지 입력을 기다림
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # 메시지를 입력받을 때까지 대기
        user_input = await bot.wait_for('message', timeout=60.0, check=check)

        # 입력된 내용으로 계산 수행
        parts = user_input.content.split()
        if len(parts)==6:
            result = int(parts[0])
            nums = list(map(int, parts[1:3]))
            calc = parts[3:5]
            word = parts[-1]
        elif len(parts)==5:
            result = int(parts[0])
            nums = list(map(int, parts[1:3]))
            calc = list(parts[3])
            word = parts[-1]

        for i in range(2):
            if calc[i] == "+":
                result += nums[i]
            elif calc[i] == "-":
                result -= nums[i]
            elif calc[i] == "*":
                result *= nums[i]

        result_message = f"{result}{word}"
        if word not in ["바스", "벨테인", "루나사", "삼하인", "임볼릭"]:
            result_message = "문자가 잘못되었습니다."
        embed = discord.Embed(title="계산 결과", description=result_message, color=0x62c1cc)
        await ctx.send(embed=embed)
    except TimeoutError:
        await ctx.send("시간 초과! 계산식을 입력하지 않았습니다.")


bot.run(cromBotToken)
