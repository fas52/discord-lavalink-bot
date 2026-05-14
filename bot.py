import discord
from discord.ext import commands
import wavelink
import os
import traceback
from dotenv import load_dotenv

load_dotenv()

class MuzikBotu(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="m!", intents=intents)

    async def setup_hook(self):
        nodes = [
            wavelink.Node(
                uri="http://lavalink.jirayu.net:13592",
                password="youshallnotpass"
            ),
            wavelink.Node(
                uri="http://n3.nexcloud.in:2026",
                password="nexcloud"
            ),
            wavelink.Node(
                uri="http://lavalinkv4.serenetia.com:80",
                password="https://dsc.gg/ajidevserver"
            ),
        ]
        await wavelink.Pool.connect(client=self, nodes=nodes)

bot = MuzikBotu()

@bot.event
async def on_wavelink_node_ready(payload: wavelink.NodeReadyEventPayload):
    print(f"✅ Lavalink Bağlandı: {payload.node.identifier}")

@bot.event
async def on_ready():
    print(f"✅ Discord'a giriş yapıldı: {bot.user}")

@bot.event
async def on_wavelink_track_end(payload: wavelink.TrackEndEventPayload):
    player: wavelink.Player = payload.player
    if not player.queue.is_empty:
        song = player.queue.get()
        await player.play(song)

@bot.event
async def on_command_error(ctx, error):
    print(f"❌ HATA: {type(error).__name__}: {error}")
    traceback.print_exc()
    await ctx.send(f"❌ Hata: {error}")

@bot.command(name="p")
async def play(ctx, *, sarki_adi: str):
    print(f"▶ play komutu alındı: {sarki_adi}")

    if not ctx.author.voice:
        return await ctx.send("Lütfen önce bir ses kanalına girin!")

    if not ctx.voice_client:
        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    else:
        vc = ctx.voice_client

    sarkilar = await wavelink.Playable.search(sarki_adi)
    print(f"Arama sonucu: {sarkilar}")
    
    if not sarkilar:
        return await ctx.send("Şarkı bulunamadı!")

    sarki = sarkilar[0]
    await vc.queue.put_wait(sarki)
    await ctx.send(f"🎵 **{sarki.title}** sıraya eklendi!")

    if not vc.playing:
        await vc.play(vc.queue.get())

@bot.command(name="dur")
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⏹️ Müzik durduruldu.")

@bot.command(name="atla")
async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.playing:
        await ctx.voice_client.stop()
        await ctx.send("⏭️ Şarkı atlandı.")

bot.run(os.getenv("DISCORD_TOKEN"))
