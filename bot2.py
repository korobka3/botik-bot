import discord
from discord.ext import commands
import os
bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
	print('BOT connected')

@bot.command(pass_context = True)
async def shop(ctx):
	await ctx.send('''
		Роли:

		```1.@Red - 1050💰
2.@blue - 800💰
3.@gold - 1000💰
4.@orange - 794💰
5.@green - 348💰
6.@black - 150💰```''')

@bot.command(pass_context = True)
async def worklist(ctx):
	await ctx.send('''
	Работы:
	
```1. Программист - Доход: 1300💰 Цена: 206
2. Фрилансер - Доход: 1500💰 Цена: 450💰
3. Геймер - Доход: ```''')

@bot.command(pass_context = True)
async def buy1(ctx):
	global balance
	user = ctx.message.author

	role = discord.utils.get(user.guild.roles, id = 692719858068095056)
	
	if balance >= 1050:
		balance - 1050
		await ctx.send(f'Поздравлям {user} вы купили роль @red')
		await user.add_roles(role)
	elif balance < 1050:
		await ctx.send(f'{user} у вас недостаточно средств.')

@bot.command(pass_context = True)
async def buy2(ctx):
	user = ctx.message.author

	role = discord.utils.get(user.guild.roles, id = 692720259869704252)

	global balance
	if balance >= 800:
		balance - 800
		await ctx.send(f'Поздравлям {user} вы купили роль @blue')
		await user.add_roles(role)
	elif balance < 800:
		await ctx.send(f'{user} у вас недостаточно средств.')

@bot.command(pass_context = True)
async def buy3(ctx):
	global balance
	user = ctx.message.author

	role = discord.utils.get(user.guild.roles, id = 692722057426894901)

	if balance >= 1000:
		balance - 1000
		await ctx.send(f'Поздравлям {user} вы купили роль @gold')
		await user.add_roles(role)
	elif balance < 1000:
		await ctx.send(f'{user} у вас недостаточно средств.')

@bot.command(pass_context = True)
async def buy4(ctx):
	user = ctx.message.author

	role = discord.utils.get(user.guild.roles, id = 692722172816523356)

	global balance
	if balance >= 794:
		balance - 794
		await ctx.send(f'Поздравлям {user} вы купили роль @orange')
		await user.add_roles(role)
	elif balance < 794:
		await ctx.send(f'{user} у вас недостаточно средств.')

@bot.command(pass_context = True)
async def buy5(ctx):
	user = ctx.message.author

	role = discord.utils.get(user.guild.roles, id = 692722272749879297)

	global balance
	if balance >= 348:
		balance - 348
		await ctx.send(f'Поздравлям {user} вы купили роль @green')
		await user.add_roles(role)
	elif balance < 348:
		await ctx.send(f'{user} у вас недостаточно средств.')

@bot.command(pass_context = True)
async def buy6(ctx):
	user = ctx.message.author

	role = discord.utils.get(user.guild.roles, id = 692722337207943208)

	global balance
	if balance >= 150:
		balance - 150
		await ctx.send(f'Поздравлям {user} вы купили роль @black')
		await user.add_roles(role)
	elif balance < 150:
		await ctx.send(f'{user} у вас недостаточно средств.')

@bot.command(pass_context = True)
async def balance(ctx):
	global balance
	user = ctx.message.author
	await ctx.send(f'Баланс пользователя {user}:')
	await ctx.send(f'```{balance}```')

balance = 0

token = os.environ.get('BOT_TOKEN')