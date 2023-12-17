# 👻Optimized Domain/DNS Whitelists

Whitelists to remove false positives from DNS blocklists, hosts files, Pi-Hole blocklists, and other types of filter lists.
- Curated: carefully selected from many well-known community sources.
- Optimized: deprecated lists excluded + duplicates removed + other optimization.
- Customizable: three versions available, and you can use the [scripts](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/tree/main/.scripts) and [source lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/tree/main/sources) to customize and generate your own whitelist(s).

--- 

#### 💖 Core Domain/DNS Whitelist (optimized)

Direct link:  
[https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/core-domain-whitelist-optimized.txt](https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/core-domain-whitelist-optimized.txt)

The "core" list is our recommended whitelist built from carefully selected community sources, with the following features:  
  
- High Confidence & Lightweight: we only include domains/subdomains that have appeared twice or more in our core sources:
  - If a domain and its subdomain(s) are both in the sources, we only include the subdomain(s) for precision targeting.
  - Other domains are only included if they are in two or more sources (high certainty that they should be whitelisted/unblocked).  
  
  These features help us avoid "over-whitelisting" (unblocking things that should be blocked) while minimizing the size of the whitelist.

- Included:
  - [Core lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_core.txt) (x5)
  - [Windows lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_windows.txt) (x2, only for Windows Update and security-related features)
- Excluded:
  - [Deprecated lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_deprecated.txt)
  - [Syntax-imcompitable lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_for_adblockers.txt)
  - [Other lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_additional.txt) for specific regions/purposes
- Removed:
  - All duplicates and duplicate subdomains. 

--- 

#### 💕 Extended Domain/DNS Whitelist (optimized)

Direct link:  
[https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/extended-domain-whitelist-optimized.txt](https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/extended-domain-whitelist-optimized.txt)

The "extended" list includes the following features:

- All domains/subdomains from the core sources are included, regardless of how many times they have appeared in different sources.
- Suitable for more extensive whitelisting (the rest is the same as the core list).
- Included:
  - [Core lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_core.txt) (x5)
  - [Windows lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_windows.txt) (x2, only for Windows Update and security-related features)
- Excluded:
  - [Deprecated lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_deprecated.txt)
  - [Syntax-imcompitable lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_for_adblockers.txt)
  - [Other lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_additional.txt) for specific regions/purposes
- Removed:
  - All duplicates and duplicate subdomains. 

--- 

#### 💞 Comprehensive Domain/DNS Whitelist (optimized)

Direct link:  
[https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/comprehensive-domain-whitelist-optimized.txt](https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/comprehensive-domain-whitelist-optimized.txt)

The "comprehensive" list includes almost all the sources we have found that are still actively maintained and syntax-compatible:

- Aggregated from a large number of community whitelists.
- Suitable for comprehensive whitelisting (as broad as possible).
- Included:
  - [Core lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_core.txt) (x5)
  - [Windows lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_windows.txt) (x2, only for Windows Update and security-related features)
  - Almost everything from [other lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_additional.txt) (see the link for detail)
- Excluded:
  - [Deprecated lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_deprecated.txt)
  - [Syntax-imcompitable lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_for_adblockers.txt)
- Removed:
  - All duplicates and duplicate subdomains. 

--- 

#### 🛠️ Customizable Domain/DNS Whitelist (optimized)

You can also use the [scripts](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/tree/main/.scripts) and [source lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/tree/main/sources) to customize and generate your own whitelist(s) to suit your needs.

---

#### ✔️ Summary
| Whitelist | Description | Link |
| -------- | -------- | -------- |
| Core | High Confidence & Lightweight Whitelisting | [core-domain-whitelist-optimized.txt](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/whitelists/core-domain-whitelist-optimized.txt) |
| Extended | More Extensive Whitelisting | [extended-domain-whitelist-optimized.txt](https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/extended-domain-whitelist-optimized.txt) |
| Comprohensive | Broad-Spectrum Whitelisting | [comprehensive-domain-whitelist-optimized.txt](https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/comprehensive-domain-whitelist-optimized.txt) |

---

#### ⚙️ Scripts

Most [scripts](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/tree/main/.scripts) in this repo are adapted from [generate-domains-blocklist.py](https://github.com/DNSCrypt/dnscrypt-proxy/blob/master/utils/generate-domains-blocklist/generate-domains-blocklist.py) from the DNSCrypt-proxy project.  
  
The original script was designed to build blocklists - we have re-purposed it with some changes to generate/optimize whitelists.

For example, the original script would remove the duplicates between different sources, and we have used this function to find overlaps between sources to build our high-confidence core list, while generating the extended list at the same time.

---
