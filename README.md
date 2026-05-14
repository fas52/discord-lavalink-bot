# MrWrandl Müzik 🎵

Discord sunucuların için geliştirilmiş, Lavalink tabanlı müzik botu.

## Özellikler
- YouTube'dan müzik çalma
- Şarkı sırası (queue) sistemi
- AWS üzerinde 7/24 çalışma

## Komutlar

| Komut | Açıklama |
|-------|----------|
| `m!p <şarkı>` | Şarkı arar ve çalar |
| `m!dur` / `m!stop` | Müziği durdurur ve kanaldan ayrılır |
| `m!atla` / `m!skip` | Sıradaki şarkıya geçer |
| `m!help` | Komutları listeler |

## Kurulum

1. Repoyu klonla
```bash
git clone https://github.com/fas52/discord-lavalink-bot.git
```

2. Gerekli kütüphaneleri kur
```bash
pip install discord.py wavelink python-dotenv
```

3. `.env` dosyası oluştur
DISCORD_TOKEN=buraya_token_yaz
4. Botu başlat
```bash
python bot.py
```

## Teknolojiler
- Python / discord.py
- Wavelink & Lavalink
- AWS EC2
