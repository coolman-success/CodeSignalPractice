import sys
import re

# get markdown file as parameter
mdfile = [param for param in sys.argv if param[-3:] == ".md"]

if len(mdfile) == 0:
    print("Should be provided with the path to a markdown filename (.md)")
    sys.exit()

# read markdown file
f = open(mdfile[0], "r")
lines = f.readlines()
f.close()

# reformatting
f_param = False
for i, line in enumerate(lines):
    if line == "\n":
        continue
    elif line == "Example\n":
        lines[i] = "\n## Example\n\n"
    elif line == "Input/Output\n":
        lines[i] = "\n## Input/Output\n\n"
        f_param = True
    elif re.match(r"^(\[input\]|\[output\]|\[execution time limit\])\s", line, re.IGNORECASE):
        lines[i] = "- **" + line[:-1] + "**\n\n"
    elif f_param:
        lines[i] = "\t" + line + "\n"

# write updated format markdown
with open(mdfile[0], "w") as f:
    content = ''.join(lines)
    content = re.sub(r"\n\n\n", "\n\n", content)
    f.write(content)
