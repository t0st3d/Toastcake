
def parse_command(cmd):
    commands = {
        "!quiet": "Silencing AI...",
        "!analyze": "Analyzing logs...",
        "!status": "Toastcake is active."
    }
    return commands.get(cmd, "Unknown command.")
