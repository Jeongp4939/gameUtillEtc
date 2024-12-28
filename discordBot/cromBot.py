import discord
from discord.ext import commands
from discordBot.dico_token import cromBotToken
import re

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

@bot.event
async def on_message(message):
    pattern1 = r'\d{1,2} \d{1,2} \d{1,2} [+\-*][+\-*] [가-힣]{2,3}'
    pattern2 = r'\d{1,2} \d{1,2} \d{1,2} [+\-*] [+\-*] [가-힣]{2,3}'

    if re.search(pattern1, message.content) or re.search(pattern2, message.content):
        parts = message.content.split()
        result = int(parts[0])
        nums = list(map(int, parts[1:3]))
        word = parts[-1]

        # 연산자 처리: pattern1과 pattern2에 따른 연산자 위치 처리
        if len(parts[3]) == 2:  # pattern1에 해당하는 경우
            calc = list(parts[3])  # 연산자가 붙어 있는 경우
        else:  # pattern2에 해당하는 경우
            calc = [parts[3], parts[4]]  # 연산자가 띄어져 있는 경우

        for i in range(2):
            if calc[i] == "+":
                result += nums[i]
            elif calc[i] == "-":
                result -= nums[i]
            elif calc[i] == "*":
                result *= nums[i]
            else:
                result_message = "입력이 잘못되었습니다."
                embed = discord.Embed(
                    title="계산 결과", description=result_message, color=0x62c1cc)
                await message.channel.send(embed=embed)
                return

        # 유효한 한글 문자 체크
        valid_words = ["바스", "벨테인", "루나사", "삼하인", "임볼릭"]
        if word not in valid_words:
            result_message = "문자가 잘못되었습니다."
        else:
            result_message = f"{result}{word}"

        embed = discord.Embed(
            title="계산 결과", description=result_message, color=0x62c1cc)
        await message.channel.send(embed=embed)

    await bot.process_commands(message)  # 커맨드가 처리되도록 함


@bot.command(aliases=['헬프', '도움'])
async def help(ctx):
    embed = discord.Embed(
        title="Help", description="!공지 \n 계산기 기능은 [숫자] [숫자] [숫자] [계산기호][계산기호] [문자] 형식으로 입력하면 자동으로 계산됩니다. \n\n !채널설정\n 해당 메세지 채널을 봇 작동 채널로 설정\n\n !경로\n 각 난이도별 경로 설명")
    await ctx.send(embed=embed)


@bot.command()
async def 공지(ctx):
    embed = discord.Embed(
        title="공지", description="!공지 \n 계산기 기능은 [숫자] [숫자] [숫자] [계산기호][계산기호] [문자] 형식으로 입력하면 자동으로 계산됩니다. \n\n !채널설정\n 해당 메세지 채널을 봇 작동 채널로 설정\n\n !경로\n 각 난이도별 경로 설명", color=0x62c1cc)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def 채널설정(ctx):
    global channel_id
    channel_id = ctx.channel.id
    await ctx.send(f"타겟 채널이 {ctx.channel.mention}으로 설정되었습니다.")


@bot.command(aliases=['ㄱㄹ', '길'])
async def 경로(ctx):
    embed = discord.Embed(
        title="난이도 별 경로 안내", description="[30 길]\n 초 -> 초 -> 초 -> 초(무시) -> 노 -> 빨 -> 빨 -> 빨(악령 방) -> 빨 \n\n [50 길]\n 빨 -> 초 -> 빨 -> 초(무시) -> 초 -> 빨-> 빨(악령 방) -> 빨(추격자 20%) -> 이루샤 -> 빨 \n 무조건 왼쪽으로 이동 \n\n [100 길]\n 빨 -> 빨(추격자 28% 추천) -> 노 -> 빨(다잡기) -> 빨 -> 빨-> 빨(악령 방) -> 빨(추격자 48%) -> 이루샤 -> 빨  \n\n")
    await ctx.send(embed=embed)

bot.run(cromBotToken)
