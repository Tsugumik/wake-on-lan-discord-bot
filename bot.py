import discord
from discord.ext import commands
from wakeonlan import send_magic_packet

bot = commands.Bot(command_prefix='!', description="This is a wol bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name='turnoncomputer', aliases=['toc'])
@commands.is_owner()
async def turnoncomputer(ctx):
    send_magic_packet('MAC ADRESS',
    ip_address='HOST BROADCAST ADRESS', port=9)
    await ctx.send('Package sent')

@bot.command(name='botstop', aliases=['bstop'])
@commands.is_owner()
async def botstop(ctx):
    print('Goodbye')
    await ctx.send('Goodbye')
    await bot.logout()
    return

bot.run('TOKEN')
