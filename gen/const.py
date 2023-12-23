import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
CACHE_DIR = ROOT_DIR / ".cache" / "tgxgen"
GEN_DIR = ROOT_DIR / "gen"
TGX = ROOT_DIR / "src" / "tgx"

# bot
BOT = TGX / "bot"
BOT_API_HTML = CACHE_DIR / "bot_api.html"
BOT_SCHEMAS_DIR = BOT / "schemas"
BOT_PATHS_DIR = BOT / "paths"
BOT_ENUMS_DIR = BOT / "enums"
BOT_GEN_DIR = GEN_DIR / "bot"
BOT_CONFIG_DIR = GEN_DIR / "config"
