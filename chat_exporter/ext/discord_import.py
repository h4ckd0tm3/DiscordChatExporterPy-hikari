discord_modules = ['hikari']
for module in discord_modules:
    try:
        hikari = __import__(module)
        hikari.module = module
        break
    except ImportError:
        continue
