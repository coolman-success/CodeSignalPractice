def solution(xml):

    import xml.etree.ElementTree as ET
    from collections import OrderedDict
    
    def maketree(parent, level):
        tags.setdefault(parent.tag, {})
        tags[parent.tag].setdefault('attrib', set()).update(parent.keys())
        tags[parent.tag].setdefault('level', level)
        if len(parent) == 0:
            return
        else:
            for child in parent:
                maketree(child, level + 1)
    
    root = ET.fromstring(xml)
    tags = OrderedDict()
    maketree(root, 0)
    
    res = []
    for key, value in tags.items():
        res.append('--'*value['level'] + key + '(' + ', '.join(sorted(value['attrib'])) + ')')
    
    return res
