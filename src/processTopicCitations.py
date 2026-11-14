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

Usage: python src/processTopicCitations.py
"""

import fileinput
import re
import sys
from urllib.parse import urlsplit
import frontmatter
import os
import json

# Current collection of sources: derived from '_sources' directory metadata information
sources = {}

# Filepaths relative to the 'home' directory of the project
# Expecting the script to be called from there.
topics_filepath = "./docs/topics.md"
citation_filepath = "./docs/_data/citations.yml"
sources_filepath = "./docs/_sources"


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
pattern2b = r"\[([^\[]*)\]\(([^\)]*)\)"

#* _Alternate Names:_
#* _Generic:_ Tacrolimus

pattern3 = r"\*\s+\_([^\_]+)\_\s*"

# Sources found for documentation
found_sources = {}
found_topics = {}

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

for filename in os.listdir(sources_filepath):
    if filename.endswith('.md'):
        identifer_length = len(filename)-3
        identifier = filename[0:identifer_length]
        file_path = os.path.join(sources_filepath, filename)

        # Parse front matter and content
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

            # Fetch all front matter attributes as a dictionary
            metadata = post.metadata
            metadata['filename'] = filename
            metadata['identifier'] = identifier
           # Optional: capture the markdown body text as well
            # metadata['content_body'] = post.content

            extracted_data.append(metadata)

for entry in extracted_data:
    # print(entry['identifier'], entry['name'], file=sys.stderr)
    sources[entry['identifier']]=entry['short-name']

print(f"Found {len(sources.keys())} registered sources\n",  file=sys.stderr)

with open(citation_filepath, "w", encoding="utf-8") as citations_file:

    # This moves the original 'topics_filepath' to a '.bak' version, and writes a new version of 'topics_filepath'
    with fileinput.input(files=topics_filepath, inplace=True, backup=".bak") as file:
        # Loop over all the lines in the file
        subsection3_count = 0
        for line in file:
            # Check for subsection match
            match2 = re.match(pattern2, line)
            if match2:
                subsection3 = match2.group(1)
                subsection3_count += 1
                # found_topics[subsection3]={}
                subsection3_url = ""
                match2b = re.match(pattern2b, subsection3)
                if match2b:
                    subsection3, subsection3_url = match2b.groups()

                subsection3_slug = make_anchor_name(subsection3)
                if not subsection3_url:
                    subsection3_url = "#"+subsection3_slug

                print(f"### [{subsection3}]({subsection3_url})")

                subsection3_prefix = subsection3[0].lower()

                found_topics[subsection3]= {'key': subsection3, 'slug': subsection3_slug,'count': subsection3_count, 'prefix': subsection3_prefix}
                print("Found Subsection:", found_topics[subsection3], file=sys.stderr)
                continue

            # Check for citation match
            match3 = re.match(pattern3, line)
            if match3:
                #found_topics[subsection3]

                keyword = make_anchor_name(match3.group(1))
                text_after : str = line[match3.end():]
                if subsection3:
                    topic_entry = found_topics[subsection3]
                    topic_entry[keyword]=text_after.strip()
                    print("   * Found Subsection Entry:", subsection3, topic_entry,  file=sys.stderr)
                else:
                    print("   * Found Subsection Info:", subsection3, keyword, text_after,  file=sys.stderr)

                print(line, end="")
                continue

            # Check for citation match
            match1 = re.match(pattern1, line)
            if match1:
                number, text, url = match1.groups()
                parsed_url = urlsplit(url)

                hostname = parsed_url.hostname
                hostname_parts = hostname.split(".")

                # Match exactly as possible
                source_tag = "".join(hostname_parts)
                for start in range(0,len(hostname_parts)-1): #0-based indexing
                    test_tag = "".join(hostname_parts[start:])
                    if test_tag in sources:
                        source_tag = test_tag
                        break #Found the tag in sources

                # print("Found:", source_tag, file=sys.stderr)


                # source_tag = ""
                # while ()
                # source_tag = "".join(hostname_parts[-2:])
                # if source_tag.startswith("org"):
                #     source_tag = "".join(hostname_parts[-3:])
                # if source_tag.startswith("co"):
                #     source_tag = "".join(hostname_parts[-3:])

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

any_unregistered = False
for key, value in found_sources.items():
    if key not in sources:
        if value["count"] > 1:
            if not any_unregistered:
                print("The following are currently unregistered sources with more than 1 citation:",  file=sys.stderr)
            any_unregistered = True

            print(f"{key}: {value}",  file=sys.stderr)


relevant_keys = ['generic','brand','alternate-names']
current_prefix = ''
current_count = ''
for key, value in found_topics.items():
    #     result = " ".join(value.values())original.keys() & target_keys
    relevant_values = [value[k] for k in relevant_keys if k in value]
    # print(f"{key}: {"; ".join(relevant_values)}",  file=sys.stderr)
    subsection3_prefix = value['prefix']
    subsection3_count = value['count']
    subsection3_slug = value['slug']
    subsection3_key = value['key']

    # print(f"{key}: {value} • {subsection3_prefix} • {"; ".join(relevant_values)}",  file=sys.stderr)
    if current_prefix != subsection3_prefix:
        current_prefix = subsection3_prefix
        current_count = subsection3_count
        current_slug = subsection3_slug
        print(f"table tr:nth-child({current_count}), /*{current_prefix}*/",  file=sys.stderr)
        print(f"#{current_slug}, ",  file=sys.stderr)
        print(f"|[{subsection3_key} &darr;](#{subsection3_slug}) <a id=\"{current_prefix}\"></a>|{"; ".join(relevant_values)}|",  file=sys.stderr)
    else:
        print(f"|[{subsection3_key} &darr;](#{subsection3_slug})|{"; ".join(relevant_values)}|",  file=sys.stderr)




# table tr:nth-child(1), /*A*/
# table tr:nth-child(21), /*B*/
# table tr:nth-child(30), /*C*/
# table tr:nth-child(42), /*D*/
# table tr:nth-child(54), /*E*/
# table tr:nth-child(68), /*F*/
# table tr:nth-child(76), /*G*/
# table tr:nth-child(83), /*H*/
# table tr:nth-child(101), /*I*/
# table tr:nth-child(109), /*J*/
# table tr:nth-child(112), /*K*/
# table tr:nth-child(116), /*L*/
# table tr:nth-child(131), /*M*/
# table tr:nth-child(140), /*N*/
# table tr:nth-child(146), /*O*/
# table tr:nth-child(149), /*P*/
# table tr:nth-child(165), /*R*/
# table tr:nth-child(170), /*S*/
# table tr:nth-child(180), /*T*/
# table tr:nth-child(202), /*U*/
# table tr:nth-child(208), /*V*/
# table tr:nth-child(213), /*X*/


#acr,
#bactrim,
#camino-hospital-iop,
#deceased-organ-donation,
#edema,
#fib-4,
#gabapentin,
#hcc-ablation,
#icu,
#j-tube,
#ketorolac,
#lactulose,
#medical-marijuana,
#naltrexone,
#optn,
#paracentesis,
#recompensated,
#safety-net,
#tace,
#uacr,
#valcyte,
#xiaflex,