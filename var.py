from os import system as console
from objects import mods as sMods

async def printMain():
    console('clear')
    print('\n\x1b[36m ██╗  ██╗ █████╗ ██╗██╗   ██╗ ██████╗')
    print('\x1b[34m ██║ ██╔╝██╔══██╗██║╚██╗ ██╔╝██╔═══██╗')
    print('\x1b[36m █████╔╝ ███████║██║ ╚████╔╝ ██║   ██║')
    print('\x1b[34m ██╔═██╗ ██╔══██║██║  ╚██╔╝  ██║   ██║')
    print('\x1b[36m ██║  ██╗██║  ██║██║   ██║   ╚██████╔╝')
    print('\x1b[34m ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝    ╚═════╝\x1b[0m')

async def scoreMods(mods):
    ScoreMods = ""
    if mods == 0: ScoreMods += "NM"
    if mods & sMods.NOFAIL: ScoreMods += "NF"
    if mods & sMods.EASY: ScoreMods += "EZ"
    if mods & sMods.HIDDEN: ScoreMods += "HD"
    if mods & sMods.HARDROCK: ScoreMods += "HR"
    if mods & sMods.DOUBLETIME: ScoreMods += "DT"
    if mods & sMods.HALFTIME: ScoreMods += "HT"
    if mods & sMods.FLASHLIGHT: ScoreMods += "FL"
    if mods & sMods.SPUNOUT: ScoreMods += "SO"
    if mods & sMods.TOUCHSCREEN: ScoreMods += "TD"
    if mods & sMods.RELAX: ScoreMods += "RX"
    if mods & sMods.RELAX2: ScoreMods += "AP"
    return ScoreMods

ball = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it." ]
messages = ['self love i suppose...', 'this is not possible.', 'don\'t try that in public at least!', 'listen ok... that\'s just weird.']
blushGifs = [ 'https://cdn.discordapp.com/attachments/798068311510351903/798068679107149864/tenor_7.gif', 'https://cdn.discordapp.com/attachments/798068311510351903/798068681187655730/tenor_6.gif', 'https://cdn.discordapp.com/attachments/798068311510351903/798068683167105044/tenor_5.gif', 'https://cdn.discordapp.com/attachments/798068311510351903/798068683586273280/tenor_4.gif', 'https://cdn.discordapp.com/attachments/798068311510351903/798068685117587456/tenor_2.gif', 'https://cdn.discordapp.com/attachments/798068311510351903/798068685637550110/tenor_3.gif', 'https://cdn.discordapp.com/attachments/798068311510351903/798068686501445642/tenor_1.gif', 'https://cdn.discordapp.com/attachments/798068311510351903/798068686527266907/tenor.gif' ]
bonkGif = 'https://cdn.discordapp.com/attachments/637762361503252493/708479358410424350/doggo.gif'
kissGifs = ['https://cdn.discordapp.com/attachments/786129390529675285/797339550450974740/tenor_7.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797339550837374986/tenor_5.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797339551235440670/tenor_6.gif','https://cdn.discordapp.com/attachments/786129390529675285/797339554234761226/tenor_3.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797339556051288104/tenor_1.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797339555777871912/tenor_2.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797339558969737237/tenor.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797339554108407838/tenor_4.gif',]
cGifs = ['https://cdn.discordapp.com/attachments/786129390529675285/797343343243427849/tenor_31.gif','https://cdn.discordapp.com/attachments/786129390529675285/797343345009491968/tenor_30.gif','https://cdn.discordapp.com/attachments/786129390529675285/797343345910349844/tenor_29.gif','https://cdn.discordapp.com/attachments/786129390529675285/797343346967707648/tenor_28.gif','https://cdn.discordapp.com/attachments/786129390529675285/797343347807092766/tenor_25.gif','https://cdn.discordapp.com/attachments/786129390529675285/797343347945111552/tenor_27.gif','https://cdn.discordapp.com/attachments/786129390529675285/797343349706063893/tenor_26.gif','https://cdn.discordapp.com/attachments/786129390529675285/797343349886681148/tenor_24.gif']
hugGifs = ['https://cdn.discordapp.com/attachments/786129390529675285/797341676355584000/tenor_15.gif','https://cdn.discordapp.com/attachments/786129390529675285/797341680013410314/tenor_13.gif','https://cdn.discordapp.com/attachments/786129390529675285/797341680251568148/tenor_14.gif','https://cdn.discordapp.com/attachments/786129390529675285/797341682840502282/tenor_12.gif','https://cdn.discordapp.com/attachments/786129390529675285/797341683536232509/tenor_11.gif','https://cdn.discordapp.com/attachments/786129390529675285/797341685141995521/tenor_10.gif','https://cdn.discordapp.com/attachments/786129390529675285/797341686123986954/tenor_9.gif','https://cdn.discordapp.com/attachments/786129390529675285/797341687940382760/tenor_8.gif',]
patGifs = ['https://cdn.discordapp.com/attachments/786129390529675285/797342556404056104/tenor_23.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797342557227057172/tenor_22.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797342559831195679/tenor_21.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797342560196231179/tenor_20.gif',  'https://cdn.discordapp.com/attachments/786129390529675285/797342563455336528/tenor_19.gif',  'https://cdn.discordapp.com/attachments/786129390529675285/797342564004397086/tenor_18.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797342564989534238/tenor_17.gif', 'https://cdn.discordapp.com/attachments/786129390529675285/797342565619204106/tenor_16.gif',]
females = [107356210486898688]
queries = {
    0: "SELECT username, id, pp_std, pp_taiko, pp_mania, pp_ctb, country FROM users_stats WHERE username = %s",
    1: "SELECT username, id, pp_std, pp_taiko, pp_ctb, country FROM rx_stats WHERE username = %s",
    2: "SELECT username, id, pp_std, country FROM auto_stats WHERE username = %s",
    3: "SELECT username FROM users_stats WHERE discord_id = %s",
    4: "SELECT id, username FROM users WHERE username = %s",
    5: "SELECT country FROM users_stats WHERE id = %s",
    6: "SELECT * FROM beatmaps WHERE beatmap_md5 = %s"
}
recentQueries = {
    0: "SELECT * FROM scores INNER JOIN beatmaps ON scores.beatmap_md5 = beatmaps.beatmap_md5 WHERE userid = %s ORDER BY time DESC;",
    1: "SELECT * FROM scores_relax INNER JOIN beatmaps ON scores_relax.beatmap_md5 = beatmaps.beatmap_md5 WHERE userid = %s ORDER BY time DESC;",
    2: "SELECT * FROM scores_auto INNER JOIN beatmaps ON scores_auto.beatmap_md5 = beatmaps.beatmap_md5 WHERE userid = %s ORDER BY time DESC;",
    3: "SELECT id, username FROM users WHERE username = %s",
    4: "SELECT country FROM users_stats WHERE id = %s"
}
topQueries = {
    0: "SELECT * FROM scores INNER JOIN beatmaps ON scores.beatmap_md5 = beatmaps.beatmap_md5 WHERE userid = %s AND completed = 3 ORDER BY pp DESC;",
    1: "SELECT * FROM scores_relax INNER JOIN beatmaps ON scores_relax.beatmap_md5 = beatmaps.beatmap_md5 WHERE userid = %s AND completed = 3 ORDER BY pp DESC;",
    2: "SELECT * FROM scores_auto INNER JOIN beatmaps ON scores_auto.beatmap_md5 = beatmaps.beatmap_md5 WHERE userid = %s AND completed = 3 ORDER BY pp DESC;",
}
