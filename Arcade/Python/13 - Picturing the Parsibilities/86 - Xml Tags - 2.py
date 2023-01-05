def solution(xml):
    import re
    lines = re.sub(r'>\s*<', '>\n<', xml)
    lines = lines.split('\n')
    
    level = 0
    tags = {}
    cur = []
    for line in lines:
        m = re.search(r'<\w+', line)
        if m:
            tag = m.group()[1:]
            print('tag =>', tag)
            if tag not in tags:
                tags[tag] = {}
                tags[tag]['attrib'] = set()
                tags[tag]['level'] = level
            cur.append(tag)
            level += 1
        
        if '=' in line:
            attribs = set(x.split('=')[0] for x in line.split() if '=' in x)
            tags[cur[-1]]['attrib'] |= attribs
        
        if '/' in line:
            cur.pop()
            level -= 1
    
    res = []
    for tag, value in tags.items():
        attribs = ', '.join(sorted(value['attrib']))
        res.append(f'{"--"*value["level"]}{tag}({attribs})')
    
    return res
