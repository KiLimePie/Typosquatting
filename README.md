# typo-squatting-scripts

These python scripts generate different typo squats of a given domain name.

## Prerequisites

* Python 3.6 or higher

## Scripts

* 'homoglyph.py': This script replaces each letter one at a time in the given domain with a homoglyph.
* 'dupeall.py': This script duplicates each letter one at a time in the given domain name.
* 'remove1letter.py': This script removes each letter one at a time in the given domain name.
* 'TLD.py': This script replaces the top-level domain of domains in the new_domains.txt file with the most common malicious top-level domains and writes the new domain names into a sus.csv file.

## Getting Started

1.  Clone or download this repository
2.  Navigate to the directory where you cloned or downloaded the repository
3.  Run the desired script using 'python script_name.py'
4.  When prompted, enter a domain name and top-level domain

## Input Files

* 'new_domains.txt': This file is used by TLD.py and should contain a list of domain names, one per line.

## Output Files

* 'sus.csv': This file is created by TLD.py and contains a list of the modified domain names.

## Contact

If you have any questions or issues with the scripts, please open an issue in this repository.
