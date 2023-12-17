@echo on

:: cd %USERPROFILE%\Downloads\Blocklist\whitelists

:: Generate core and extended domain whitelists
python gen-core-ex-whitelists.py > extended-domain-whitelist-optimized.txt

:: Further optimize core domain whitelist to remove unnecessary duplicates
python optimize-core-list-further.py > core-domain-whitelist-optimized.txt

:: Generate comprehensive domain whitelist
python gen-comp-whitelists.py > comprehensive-domain-whitelist-optimized.txt

:: Add title and timestamp
python set-title-timestamp.py

:: Clean up - ::ove interim file(s)
del overlaps-raw.txt
