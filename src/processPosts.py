#!/usr/bin/env python
"""\
Process the files in 'sources_filepath' to create make H3 headers linkable and build a TOC that can be used by the file.

Usage: python src/processPosts.py
"""

import fileinput
import re
import sys
import os

# Current collection of sources: derived from '_sources' directory metadata information
sources = {}

# Filepaths relative to the 'home' directory of the project
# Expecting the script to be called from there.
sources_filepath = "./docs/_posts"
includes_filepath = "./docs/_includes/posts"


# Identify citation lines by the pattern:
# * [#] … <url>
pattern1 = r"\*\s+\[(\d+)\]([^\<]+)<([^\>]+)>"

# Break apart the '…' if it matches
# … «citation-description» …
pattern1b = r"([^«]*)«([^»]+)»(.*)"

# Identify Topic lines by the pattern:
# ### Topic-Name
pattern2 = r"\#(\#+) (.*)"

# Break apart Topic-Name if it matches
# [Topic-Name](link)
pattern2b = r"\[([^\[]*)\]\(([^\)]*)\)"

# Identify Topic lines by the pattern:
# <h#>Topic-Name</h#>
pattern2h = r"<h(\d)([^\>]*)>(.*)</h(\d)>"

# Break apart Topic-Name if it matches
# <a...>Topic Name</a>
pattern2hb = r"<a([^\>]*)>(.*)</a>"



# Identify Topic lines by the pattern:
# ## Topic-Name
pattern3 = r"\#\# (.*)"

# Break apart Topic-Name if it matches
# [Topic-Name](link)
pattern3b = r"\[([^\[]*)\]\(([^\)]*)\)"


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


extracted_data = []
files = []

file_ext_map = {".md": 1, ".markdown": 1}

for root, _, filenames in os.walk(sources_filepath):
    for filename in filenames:
        # Combine the folder path and file name
        file_name, file_ext = os.path.splitext(filename)
        infile = f"{root}/{filename}"
        outfile = f"{includes_filepath}/{file_name}_toc.txt"
        files.append(infile);
        files.append(outfile);
        if (file_ext not in file_ext_map):
            print("Ignore:", filename, file_ext, file_ext_map, file=sys.stderr)
            continue

        with fileinput.input(files=infile, inplace=True) as infile_file:
            with open(outfile, "w", encoding="utf-8") as outfile_file:
                # Loop over all the lines in the file
                for line in infile_file:
                    # Check for subsection match
                    match2 = re.match(pattern2, line)
                    if match2:
                        subsectionDepthStr = match2.group(1)
                        subsectionDepth = len(subsectionDepthStr)+1

                        if subsectionDepth < 5:
                            subsection3 = match2.group(2)
                            subsection3_url = ""
                            match2b = re.match(pattern2b, subsection3)
                            if match2b:
                                subsection3, subsection3_url = match2b.groups()

                            subsection3_slug = make_anchor_name(subsection3)
                            if not subsection3_url:
                                subsection3_url = "#"+subsection3_slug

                            print(f"#{subsectionDepthStr} [{subsection3}]({subsection3_url})")
                            print("Found-hash:", subsectionDepth, subsection3_slug, subsection3_url, file=sys.stderr)
                            if subsectionDepth == 3:
                                print(f"  * [{subsection3}]({subsection3_url})", file=outfile_file)
                            elif subsectionDepth == 2:
                                print(f"* [{subsection3}]({subsection3_url})", file=outfile_file)

                            continue

                    # Check for subsection match
                    match2h = re.match(pattern2h, line)
                    if match2h:
                        subsectionDepthStr = match2h.group(1)
                        subsectionDepth = int(subsectionDepthStr)

                        if subsectionDepth < 5:
                            subsection3 = match2h.group(3)
                            subsection3_url = ""
                            match2hb = re.match(pattern2hb, subsection3)
                            if match2hb:
                                subsection3 = match2hb.group(2)
    #<a href="#multidimensional-relationship">Multidimensional Relationship</a>

                            subsection3_slug = make_anchor_name(subsection3)
                            if not subsection3_url:
                                subsection3_url = "#"+subsection3_slug

                            print(f"<h{subsectionDepthStr} id='{subsection3_slug}'><a href='{subsection3_url}'>{subsection3}</a></h{subsectionDepthStr}>")
                            print("Found-tag:",  subsectionDepth, subsection3_slug, subsection3_url, file=sys.stderr)
                            if subsectionDepth == 3:
                                print(f"  * [{subsection3}]({subsection3_url})", file=outfile_file)
                            elif subsectionDepth == 2:
                                print(f"* [{subsection3}]({subsection3_url})", file=outfile_file)

                            continue


                    print(line, end="")

print(files)

