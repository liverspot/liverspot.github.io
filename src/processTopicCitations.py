#!/usr/bin/env python
"""\
Process the topics.md file to find citations and hook them to the known sources.

Directly modifies the 'docs/topics.md' file although it creates a backup.  Could change this
to using a '.local' version of those files when working with the script, or to take them in as a parameter.
But given the directory is under 'git' management, wiping the file isn't particularly problematic.

Also regenerates and rewrites the 'docs/_data/citations.yml' file, but that is a derived file and all content
is sourced from the 'topics.md' file.

It expects the file paths to be from the 'home' directory.  Also the 'sources' array is manually synchronized
with the '_sources' directory.

TODO: Ideally this would parameterize the file paths but this is the version available now.
TODO: Should get the 'sources' information by processing the _sources files.

Usage: python src/processTopicCitations.py
"""

import fileinput
import re
import sys
from urllib.parse import urlsplit

# Current collection of sources: derived from '_sources' directory metadata information
sources = {
    "britishlivertrustorguk": "British Liver Trust",
    "clevelandclinicorg": "Cleveland Clinic",
    "chopedu": "CHOP",
    "dairbookcom": "DAIR",
    "hopkinsmedicineorg": "JHM",
    "hrsagov": "HRSA",
    "kidneyorg": "NKF",
    "lwwcom": "LWW",
    "mayoclinicorg": "Mayo Clinic",
    "mdcalccom": "MDCalc",
    "medlineplusgov": "MedlinePlus",

    "mountsinaiorg": "Mount Sinai",

    "nhsuk": "NHS",
    "nihgov": "NIH",
    "ohsuedu": "OHSU",
    "rochesteredu": "URochester",
    "rxlistcom": "RxList",
    "sciencedirectcom": "ScienceDirect",
    "unosorg": "UNOS",
    "upmccom": "UPMC",
    "wikipediaorg": "Wikipedia",
}

# Filepaths relative to the 'home' directory of the project
# Expecting the script to be called from there.
topics_filepath = "./docs/topics.md"
citation_filepath = "./docs/_data/citations.yml"

# Identify citation lines by the pattern:
# * [#] … <url>
pattern1 = r"\*\s+\[(\d+)\]([^\<]+)<([^\>]+)>"

# Break apart the '…' if it matches
# … «citation-description» …
pattern1b = r"([^«]*)«([^»]+)»(.*)"

# Identify Topic lines by the pattern:
# ### Topic-Name
pattern2 = r"\#\#\# (.*)"

# Break apart Topic-Name if it matches
# [Topic-Name](link)
pattern2b = r"\[([^\[]*)\]"

# Sources found for documentation
found_sources = {}


def make_anchor_name(name: str) -> str:
    # 1. Convert to lowercase and strip leading/trailing whitespace
    slug = name.lower().strip()

    # 2. Replace all spaces with hyphens
    slug = slug.replace(' ', '-')

    # 3. Remove any non-alphanumeric characters (excluding hyphens)
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')

    # 4. Remove consecutive hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')

    return slug


with open(citation_filepath, "w", encoding="utf-8") as citations_file:

    # This moves the original 'topics_filepath' to a '.bak' version, and writes a new version of 'topics_filepath'
    with fileinput.input(files=topics_filepath, inplace=True, backup=".bak") as file:
        # Loop over all the lines in the file
        for line in file:
            # Check for subsection match
            match2 = re.match(pattern2, line)
            if match2:
                subsection3 = match2.group(1)
                match2b = re.match(pattern2b, subsection3)
                if match2b:
                    subsection3 = match2b.group(1)

                subsection3_slug = make_anchor_name(subsection3)

            # Check for citation match
            match1 = re.match(pattern1, line)
            if match1:
                number, text, url = match1.groups()
                parsed_url = urlsplit(url)

                hostname = parsed_url.hostname
                hostname_parts = hostname.split(".")
                source_tag = "".join(hostname_parts[-2:])
                if source_tag.startswith("org"):
                    source_tag = "".join(hostname_parts[-3:])
                if source_tag.startswith("co"):
                    source_tag = "".join(hostname_parts[-3:])

                # Check for a description within the line (anywhere in line, although it should be in the text section)
                match1b = re.match(pattern1b, line)
                if match1b:
                    prefix, description, suffix = match1b.groups()
                    if description:
                        description = f"«{description}» "
                        # print(source_tag, url, description, file=sys.stderr)
                else:
                    description = ""

                if source_tag in found_sources:
                    found_sources[source_tag]["count"] = found_sources[source_tag]["count"]+1
                else:
                    found_sources[source_tag] = {"count": 1}

                # Output the citation information to the 'citations_file' if the source is in our list of mappings
                if source_tag in sources:
                    source_entry = sources[source_tag]
                    citations_file.write(f"- url: {url}\n")
                    citations_file.write(f"  source: {source_tag}\n")
                    citations_file.write(f"  topic-name: {subsection3}\n")
                    citations_file.write(f"  topic-slug: {subsection3_slug}\n")
                    citations_file.write(f"  path: /topics/#{subsection3_slug}\n")
                    citations_file.write(f"  description: \"{description}\"\n")

                    # Augment the citation with a source reference
                    source_text = f" [{source_entry}](/source/{source_tag}/) {description}— "
                else:
                    # Otherwise, the source_text is just the original text [untouched]
                    source_text = text

                print(f"* [{number}]{source_text}<{url}>")
            else:
                print(line, end="")


# Informational output to look for new entries to add to '_sources'
print(f"Processed citations from {len(found_sources.keys())} sources out of {len(sources.keys())} registered sources\n",  file=sys.stderr)
print("The following are currently unregistered sources with more than 1 citation:",  file=sys.stderr)
for key, value in found_sources.items():
    if key not in sources:
        if value["count"] > 1:
            print(f"{key}: {value}",  file=sys.stderr)
