import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevre dostu bir botum!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')


@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

@bot.command()
async def cevre(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız oneri komutunu kullanın!')

@bot.command()
async def oneri(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1)
    await ctx.send(f'Eski eşyaları çöpe atmak yerine geri dönüştürün')
    time.sleep(1)
    await ctx.send(f'Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.')
    time.sleep(1)
    await ctx.send(f'Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.')
    time.sleep(1)
    await ctx.send(f'Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.')
    time.sleep(1)
    await ctx.send(f'Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın..')
    time.sleep(1)
    await ctx.send(f'Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.')
    time.sleep(1)
    await ctx.send(f'Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve kullanmaya çalışın.')

@bot.command()
async def yokolma(ctx):
    await ctx.send(f'Her atık, kendisini oluşturan maddelerden mütevellit, doğadaki serüveninin son bulması için farklı zamanlara ihtiyaç duyar. Bir elma çöpü için 2 ay yeterliyken; plastik bir şişe için 450 yıl, bebek bezleri için 550 yıl, alüminyum kutular için 200-300 yıl geçmesi gerekir.')

bot.run("token")
