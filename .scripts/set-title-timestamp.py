# Add title and timestamp

from datetime import datetime, timezone

CURRENT_TIME = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

TITLE1 = "# Title: Core domain/DNS whitelist (optimized)"
TITLE2 = "# Title: Extended domain/DNS whitelist (optimized)"
TITLE3 = "# Title: Comprehensive domain/DNS whitelist (optimized)"
TIME = f"# Updated: {CURRENT_TIME}"
EXPIRE = "# Expires: 31 days (update frequency also depends on upstream sources)"
HOME = "# Homepage: https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/"
LICENSE = "# License: https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/LICENSE"

COMMENT_Core = f"{TITLE1}\n{TIME}\n{EXPIRE}\n{HOME}\n{LICENSE}\n\n"
COMMENT_Ex = f"{TITLE2}\n{TIME}\n{EXPIRE}\n{HOME}\n{LICENSE}\n\n"
COMMENT_Comp = f"{TITLE3}\n{TIME}\n{EXPIRE}\n{HOME}\n{LICENSE}\n\n"


with open('core-domain-whitelist-optimized.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines.insert(0, COMMENT_Core)

with open('core-domain-whitelist-optimized.txt', 'w', encoding="utf-8") as file:
    file.writelines(lines)


with open('extended-domain-whitelist-optimized.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines.insert(0, COMMENT_Ex)

with open('extended-domain-whitelist-optimized.txt', 'w', encoding="utf-8") as file:
    file.writelines(lines)
    

with open('comprehensive-domain-whitelist-optimized.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    lines.insert(0, COMMENT_Comp)

with open('comprehensive-domain-whitelist-optimized.txt', 'w', encoding="utf-8") as file:
    file.writelines(lines)