import aiohttp, asyncio, config, discord, json, random, re, requests, string, sys, time, var
from cmyui import AsyncSQLPool
from datetime import datetime
from discord.ext.commands import Bot
from io import StringIO
from objects import glob

intents = discord.Intents.all()
bot = Bot(command_prefix=config.prefix, intents=intents)
glob.db = AsyncSQLPool()

async def randomString(size=8, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

async def ppSize(size=int(16), char=str("=")):
	return "".join([char * random.choice(range(size))])

@bot.event
async def on_ready():
	try:
		await glob.db.connect(glob.config.mysql)
	except Exception as error:
		print(error)
	await var.printMain()
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your every step."))
	print(f'\x1b[36m\n Logged in as {bot.user}\n\x1b[0m')

@bot.event
async def on_member_join(member):
	for channel in member.guild.channels:
		if str(channel) == config.welcome_channel:
			embed = discord.Embed(title=f":two_hearts: Welcome to {member.guild.name}, {member.name}!")
			embed.set_image(url="https://cdn.discordapp.com/attachments/798068311510351903/869459413977669642/image0.gif")
			await channel.send(embed=embed)

@bot.command(pass_context=True)
async def pp(ctx):
	if ctx.author.id in var.females:
		await ctx.send(f"{ctx.message.author.mention} is female 🤠")
	else:
		embed = discord.Embed(title="PEEPEE SIZE MACHINE", color=0x00ffb3)
		embed.add_field(name=ctx.message.author.name + "'s pp size is:", value=" 8{}D".format(await ppSize()), inline=False)
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def roll(ctx):
	embed = discord.Embed(title=":game_die: Roll the die.", color=0x00ffb3)
	embed.add_field(name=ctx.message.author.name + "'s, roll:", value="{}".format(random.randint(1, 1000)), inline=False)
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ball(ctx):
	args = ctx.message.content.split(" ")[1:]
	if args[0][-1] != "?":
		await ctx.send("Please ask a question.")
	else:
		embed = discord.Embed(title=ctx.message.author.name + " asked: " + args[0], description=":8ball: | " + random.choice(var.ball), color=0x00ffb3)
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
	if user == ctx.message.author:
		embed = discord.Embed(color=0x00ffb3, timestamp=datetime.now())
		embed.set_author(name=ctx.message.author.name, url=ctx.message.author.avatar_url, icon_url=ctx.message.author.avatar_url)
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(color=0x00ffb3, timestamp=datetime.now())
		embed.set_author(name=user.name, url=user.avatar_url, icon_url=user.avatar_url)
		embed.set_image(url=user.avatar_url)
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def blush(ctx):
	embed = discord.Embed(title=":two_hearts: " + ctx.message.author.name + " is blushing... awww!" , color=0x00ffb3, timestamp=datetime.now())
	embed.set_image(url="{}".format(random.choice(var.blushGifs)))
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def verify(ctx):
	role = discord.utils.get(ctx.guild.roles, name=config.member_role)
	await ctx.message.delete()
	await ctx.message.author.add_roles(role)

@bot.command(pass_context=True)
async def bonk(ctx, user: discord.User):
	if user == ctx.message.author:
		await ctx.reply("you cannot bonk yourself!")
	else:
		embed = discord.Embed(title=f"{ctx.message.author.name} has bonked {user.name}", color=0x00ffb3, timestamp=datetime.now())
		embed.set_image(url=var.bonkGif)
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def kiss(ctx, user: discord.User):
	if user == ctx.message.author:
		await ctx.reply(random.choice(var.messages))
	else:
		embed = discord.Embed(title=f":two_hearts: {ctx.message.author.name} kissed {user.name} awwww!", color=0x00ffb3, timestamp=datetime.now())
		embed.set_image(url=random.choice(var.kissGifs))
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def stats(ctx):
	args = ctx.message.content.split(" ")[1:]
	mode = 0
	modeName = "Vanilla"
	if "-rx" in args:
		mode = 1
		modeName = "Relax"
		args.remove("-rx")
	elif "-ap" in args:
		mode = 2
		modeName = "Auto"
		args.remove("-ap")
	username = " ".join(args)

	if not args:
		checkUsername = await glob.db.fetch(var.queries[3], [ctx.author.id])
		if checkUsername == None:
			discordUsername = f"{ctx.author.name}#{ctx.author.discriminator}"
			await ctx.reply(f"Your osu account is not linked to discord. please run `{config.prefix}link @{discordUsername}`")
		else:
			userStats = await glob.db.fetch(var.queries[mode], [checkUsername["username"]])
	else:
		userStats = await glob.db.fetch(var.queries[mode], [username])

	if mode == 0:
		desc = "osu!STD pp: **{:,}** \nosu!Taiko pp: **{:,}** \nosu!Mania pp: **{:,}** \nosu!CTB pp: **{:,}**".format(userStats["pp_std"], userStats["pp_taiko"], userStats["pp_mania"], userStats["pp_ctb"])
	elif mode == 1:
		desc = "rx!STD pp: **{:,}** \nrx!Taiko pp: **{:,}** \nrx!CTB pp: **{:,}**".format(userStats["pp_std"], userStats["pp_taiko"], userStats["pp_ctb"])
	elif mode == 2:
		desc = "ap!STD pp: **{:,}**".format(userStats["pp_std"])

	embed = discord.Embed(title="{}'s {} Stats".format(userStats["username"], modeName), description=desc, color=0x00ffb3, timestamp=datetime.now())
	embed.set_author(name="{}".format(userStats["username"]), url="https://{}/u/{}".format(config.server_link, userStats["id"]), icon_url="https://osu.gatari.pw/static/images/flags/{}.png".format(userStats["country"]))
	embed.set_thumbnail(url="https://a.{}/{}".format(config.server_link, userStats["id"]))
	embed.set_footer(text=f"osu!{config.guild_name}", icon_url=config.server_icon_link)
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def recent(ctx):
	args = ctx.message.content.split(" ")[1:]
	mode = 0
	modeName = "Vanilla"
	urlEnd = ""
	if "-rx" in args:
		mode = 1
		modeName = "Relax"
		urlEnd = "rx/"
		args.remove("-rx")
	elif "-ap" in args:
		mode = 2
		modeName = "Auto"
		urlEnd = "ap/"
		args.remove("-ap")
	username = " ".join(args)

	if not args:
		checkUsername = await glob.db.fetch(var.queries[3], [ctx.author.id])
		if checkUsername == None:
			discordUsername = f"{ctx.author.name}#{ctx.author.discriminator}"
			await ctx.reply(f"Your osu account is not linked to discord. please run `{config.prefix}link @{discordUsername}`")
		else:
			userID = await glob.db.fetch(var.queries[4], [checkUsername["username"]])
			recentScore = await glob.db.fetch(var.recentQueries[mode], [userID["id"]])
			bmInfo = await glob.db.fetch(var.queries[6], [recentScore["beatmap_md5"]])
			flag = await glob.db.fetch(var.queries[5], [userID["id"]])
	else:
		userID = await glob.db.fetch(var.queries[4], [username])
		recentScore = await glob.db.fetch(var.recentQueries[mode], [userID["id"]])
		bmInfo = await glob.db.fetch(var.queries[6], [recentScore["beatmap_md5"]])
		flag = await glob.db.fetch(var.queries[5], [userID["id"]])

	embed = discord.Embed(title=recentScore["song_name"], description="Recent {} Score By {}".format(modeName, userID["username"]), color=0x00ffb3, timestamp=datetime.now(), url="https://osu.ppy.sh/beatmapsets/{}".format(recentScore["beatmapset_id"]))
	emoji = discord.utils.get(bot.emojis, name='{}_'.format(recentScore["rank"]))
	embed.add_field(name="Score Info:", value="▸ Rank: {}\n▸ PP: **{:.2f}**\n▸ Score: **{:,}**\n▸ Accuracy: **{:.2f}%**\n▸ Mods: **{}**\n▸ 300/100/50/Miss: **({})/({})/({})/({})**\n▸ Full Combo: **{}** | **({}x/{}x)**\n▸ Done On: **{}**".format(str(emoji), recentScore["display_pp"], recentScore["score"], recentScore["accuracy"], await var.scoreMods(recentScore["mods"]), recentScore["300_count"], recentScore["100_count"], recentScore["50_count"], recentScore["misses_count"], "Yes" if recentScore["full_combo"] == 1 else "No", recentScore["max_combo"], bmInfo["max_combo"], time.ctime(int(recentScore["time"]))))
	embed.set_author(name=userID["username"], url="https://{}/{}u/{}".format(config.server_link, urlEnd, userID["id"]), icon_url="https://osu.gatari.pw/static/images/flags/{}.png".format(flag["country"]))
	embed.set_thumbnail(url="https://a.{}/{}".format(config.server_link, userID["id"]))
	embed.set_image(url="https://assets.ppy.sh/beatmaps/{}/covers/cover.jpg".format(recentScore["beatmapset_id"]))
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def top(ctx):
	args = ctx.message.content.split(" ")[1:]
	mode = 0
	modeName = "Vanilla"
	urlEnd = ""
	if "-rx" in args:
		mode = 1
		modeName = "Relax"
		urlEnd = "rx/"
		args.remove("-rx")
	elif "-ap" in args:
		mode = 2
		modeName = "Auto"
		urlEnd = "ap/"
		args.remove("-ap")
	username = " ".join(args)

	if not args:
		checkUsername = await glob.db.fetch(var.queries[3], [ctx.author.id])
		if checkUsername == None:
			discordUsername = f"{ctx.author.name}#{ctx.author.discriminator}"
			await ctx.reply(f"Your osu account is not linked to discord. please run `{config.prefix}link @{discordUsername}`")
		else:
			userID = await glob.db.fetch(var.queries[4], [checkUsername["username"]])
			topScore = await glob.db.fetch(var.topQueries[mode], [userID["id"]])
			bmInfo = await glob.db.fetch(var.queries[6], [topScore["beatmap_md5"]])
			flag = await glob.db.fetch(var.queries[5], [userID["id"]])
	else:
		userID = await glob.db.fetch(var.queries[4], [username])
		topScore = await glob.db.fetch(var.topQueries[mode], [userID["id"]])
		bmInfo = await glob.db.fetch(var.queries[6], [topScore["beatmap_md5"]])
		flag = await glob.db.fetch(var.queries[5], [userID["id"]])

	embed = discord.Embed(title=topScore["song_name"], description="Top {} Score By {}".format(modeName, userID["username"]), color=0x00ffb3, timestamp=datetime.now(), url="https://osu.ppy.sh/beatmapsets/{}".format(topScore["beatmapset_id"]))
	emoji = discord.utils.get(bot.emojis, name='{}_'.format(topScore["rank"]))
	embed.add_field(name="Score Info:", value="▸ Rank: {}\n▸ PP: **{:.2f}**\n▸ Score: **{:,}**\n▸ Accuracy: **{:.2f}%**\n▸ Mods: **{}**\n▸ 300/100/50/Miss: **({})/({})/({})/({})**\n▸ Full Combo: **{}** | **({}x/{}x)**\n▸ Done On: **{}**".format(str(emoji), topScore["display_pp"], topScore["score"], topScore["accuracy"], await var.scoreMods(topScore["mods"]), topScore["300_count"], topScore["100_count"], topScore["50_count"], topScore["misses_count"], "Yes" if topScore["full_combo"] == 1 else "No", topScore["max_combo"], bmInfo["max_combo"], time.ctime(int(topScore["time"]))))
	embed.set_author(name=userID["username"], url="https://{}/{}u/{}".format(config.server_link, urlEnd, userID["id"]), icon_url="https://osu.gatari.pw/static/images/flags/{}.png".format(flag["country"]))
	embed.set_thumbnail(url="https://a.{}/{}".format(config.server_link, userID["id"]))
	embed.set_image(url="https://assets.ppy.sh/beatmaps/{}/covers/cover.jpg".format(topScore["beatmapset_id"]))
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def cuddle(ctx, user: discord.User):
	if user == ctx.message.author:
		await ctx.reply(random.choice(var.messages))
	else:
		embed = discord.Embed(title=f":two_hearts: {ctx.message.author.name} is cuddling {user.name}", color=0x00ffb3, timestamp=datetime.now())
		embed.set_image(url=random.choice(var.cGifs))
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def hug(ctx, user: discord.User):
	if user == ctx.message.author:
		await ctx.reply(random.choice(var.messages))
	else:
		embed = discord.Embed(title=f":two_hearts: {ctx.message.author.name} is hugging {user.name}", color=0x00ffb3, timestamp=datetime.now())
		embed.set_image(url=random.choice(var.hugGifs))
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def pat(ctx, user: discord.User):
	if user == ctx.message.author:
		await ctx.reply(random.choice(var.messages))
	else:
		embed = discord.Embed(title=f":two_hearts: {ctx.message.author.name} is giving {user.name} headpats!!", color=0x00ffb3, timestamp=datetime.now())
		embed.set_image(url=random.choice(var.patGifs))
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
	await ctx.send('Success! Latency is: {0}ms'.format(round(bot.latency, 5)))

@bot.command(pass_context=True)
async def purge(ctx, limit: int):
	if ctx.author.guild_permissions.administrator:
		await ctx.channel.purge(limit=limit)
		await ctx.send('{} purged {} {}'.format(ctx.author.mention, limit, "message" if limit == 1 else "messages"))
		await ctx.message.delete()
	else:
		await ctx.send('no')

@bot.command(pass_context=True)
async def ban(ctx, user: discord.User):
	if ctx.author.guild_permissions.ban_members:
		await ctx.guild.ban(user, reason=":)")
		await ctx.send(f'{user.name} has been banned.')
	else:
		await ctx.send('no')

@bot.command(pass_context=True)
async def kick(ctx, user: discord.User):
	if ctx.author.guild_permissions.kick_members:
		await ctx.guild.kick(user, reason=":)")
		await ctx.send(f'{user.name} has been kicked.')
	else:
		await ctx.send('no')

@bot.command(pass_context=True)
async def link(ctx, user: discord.User):
	discordUsername = f"{ctx.author.name}#{ctx.author.discriminator}"
	linkCode = await randomString(16)
	checkLinked = await glob.db.fetch("SELECT * FROM linking_codes WHERE `discord_user` = %s", [discordUsername])
	if checkLinked == None:
		await glob.db.execute("INSERT INTO linking_codes (`code`, `discord_user`, `discord_id`) VALUES (%s, %s, %s)", [linkCode, discordUsername, ctx.author.id])
		await user.send(f"Linking process started, log into osu!{config.guild_name} and put this command into #osu `!link {linkCode}` to finish linking your account!")
	else:
		await ctx.send("Your account is already linked! Contact Adobe#8320 if this is a mistake!")

@bot.command(pass_context=True)
async def strings(ctx):
	args = ctx.message.content.split(" ")[1:]
	if int(args[0]) < 1:
		await ctx.send("no sir")
	else:
		passW = await randomString(size=int(args[0]))
		await ctx.send(passW)

@bot.command(pass_context=True)
async def ar(ctx):
	args = ctx.message.content.split(" ")[1:]
	value = args[0]
	mod = args[1]
	availableMods = ["-dt", "-DT", "-hr", "-HR", "-ez", "-EZ"]
	if mod in availableMods:
		if float(value) <= 10 and float(value) >= 1:
			if mod in ["-dt", "-DT"]:
				ar = float(value) * 2 + 13
				dtAR = float(ar) / 3
				await ctx.send(f"AR {value} -> {dtAR:.1f}")
			elif mod in ["-hr", "-HR"]:
				if float(value) <= 10 and float(value) >= 8:
					ar = 10
				else:
					ar = float(value) * 1.4
				await ctx.send(f"AR {value} -> {ar:.1f}")
			elif mod in ["-ez", "-EZ"]:
				if float(value) <= 10 and float(value) >= 1:
					ar = float(value) / 2
					await ctx.send(f"AR {value} -> {ar:.1f}")
		else:
			await ctx.send("Value must be between 1 and 10.")
	else:
		await ctx.send("Invalid mod. Avalible mods are `DT, HR, EZ`")

@bot.command(pass_context=True)
async def bminfo(ctx):
	args = ctx.message.content.split(" ")[1:]
	beatmapLink = args[0]
	if beatmapLink[:31] != "https://osu.ppy.sh/beatmapsets/":
		await ctx.send("Link must be an osu!bancho beatmap link.")
	else:
		beatmapRegex = r'^https?:\/\/osu.ppy.sh\/beatmapsets\/([0-9]*)#(osu|taiko|fruits|mania)\/'
		bid = re.sub(beatmapRegex, '', beatmapLink)
		beatmap = requests.get(f"https://osu.ppy.sh/api/get_beatmaps?k={config.api_key}&b={bid}&limit=1").text
		beatmapInfo = json.loads(beatmap)
		if beatmapInfo[0]["mode"] == "1":
			mode = "taiko"
		elif beatmapInfo[0]["mode"] == "2":
			mode = "fruits"
		elif beatmapInfo[0]["mode"] == "3":
			mode = "mania"
		else:
			mode = "osu"
		if beatmapInfo[0]["approved"] == "1":
			status = "Ranked"
		elif beatmapInfo[0]["approved"] == "-2":
			status = "Graveyard"
		elif beatmapInfo[0]["approved"] == "4":
			status = "Loved"

		embed = discord.Embed(title="{} - {} [{}]".format(beatmapInfo[0]["artist"], beatmapInfo[0]["title"], beatmapInfo[0]["version"]), description="{} beatmap by {}".format(status, beatmapInfo[0]["creator"]), color=0x00ffb3, timestamp=datetime.now(), url="https://osu.ppy.sh/beatmapsets/{}#{}/{}".format(beatmapInfo[0]["beatmapset_id"], mode, bid))
		embed.add_field(name="Beatmap Info:", value="▸ CS: **{}**\n▸ OD: **{}**\n▸ AR: **{}**\n▸ HP: **{}**\n▸ BPM: **{:.0f}**\n▸ Playcount/Passcount: **{:,}/{:,}**\n▸ Max Combo: **{:,}x**\n".format(beatmapInfo[0]["diff_size"], beatmapInfo[0]["diff_overall"], beatmapInfo[0]["diff_approach"], beatmapInfo[0]["diff_drain"], float(beatmapInfo[0]["bpm"]), int(beatmapInfo[0]["playcount"]), int(beatmapInfo[0]["passcount"]), int(beatmapInfo[0]["max_combo"])))
		embed.set_image(url="https://assets.ppy.sh/beatmaps/{}/covers/cover.jpg".format(beatmapInfo[0]["beatmapset_id"]))
		await ctx.send(embed=embed)

bot.run(config.token)
