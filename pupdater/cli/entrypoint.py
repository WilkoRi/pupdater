import sys

def main():
    if sys.argv[1:] == ["config", "install"]:
        from pupdater.cli import config
        config.install()
    else:
        print("❌ Unknown command. Try: pupdater config install")
