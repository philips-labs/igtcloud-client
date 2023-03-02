import re

key_regex = re.compile(r"\s*(-{5}\bBEGIN\b.*\b-{5})\s*(.*)(-{5}\bEND\b.*\b-{5})\s*", re.DOTALL)


def save_private_key(key, filename):
    match = key_regex.match(key)

    with open(filename, "wt") as f:
        if match:
            lines = [match.group(1)]
            content = match.group(2)
            n = 64
            lines.extend([content[i:i+n] for i in range(0, len(content), n)])
            lines.append(match.group(3))
            f.writelines([line + "\n" for line in lines])
        else:
            f.write(key)
