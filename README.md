# 👻Optimized Domain/DNS Whitelists

Whitelists to unblock websites/apps and remove false positives from DNS blocklists, hosts files, Pi-Hole blocklists, and other types of filter lists.
- Curated: carefully selected from many well-known community sources.
- Optimized: deprecated lists excluded + duplicates removed + other optimization.
- Customizable: three versions available, and you can use the [script](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/tree/main/.scripts) and [source lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/tree/main/sources) to customize and generate your own whitelist(s).

--- 

#### Core Domain/DNS Whitelist (optimized)

Direct link:  
[https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/core-domain-whitelist-optimized.txt](https://raw.githubusercontent.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/main/whitelists/core-domain-whitelist-optimized.txt)

The "core" list is our recommended whitelist built from carefully selected community whitelists, with the following features:  
  
- High Confidence & Lightweight: we only include domains/subdomains that have appeared twice in our sources:
  - If a domain and its subdomain(s) are both in the sources, we only include the subdomain(s) for precision targeting.
  - Other domains are only included if they are in two or more sources (high certainty that they should be whitelisted/unblocked).  
  
  These features help us avoid "over-whitelisting" (unblocking things that should be blocked) while minimizing the size of the whitelist.

- Included:
  - [Core lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_core.txt) (x5)
  - [Windows lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_windows.txt) (x2, only for Windows Update and security-related features).
- Excluded:
  - [Deprecated lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_deprecated.txt)
  - [Syntax-imcompitable lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_for_adblockers.txt)
  - [Other lists](https://github.com/Zen-Initiative/Optimized-Domain-DNS-Whitelists/blob/main/sources/whitelists_additional.txt) for specific regions/purposes
- Removed:
  - All duplicates and duplicate subdomains in the final list. 

--- 

#### Extended Domain/DNS Whitelist (optimized)

Direct link:  


--- 

#### Comprehensive Domain/DNS Whitelist (optimized)

Direct link:  


--- 

#### Customizable Domain/DNS Whitelist (optimized)

---
