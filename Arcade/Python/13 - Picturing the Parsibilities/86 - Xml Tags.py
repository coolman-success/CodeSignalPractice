def solution(xml):

    import xml.etree.ElementTree as ET
    from collections import OrderedDict
    
    def maketree(parent, level):
        key = parent.tag, level
        tags.setdefault(key, set()).update(parent.keys())
        for child in parent:
            maketree(child, level + 1)
    
    tags = OrderedDict()
    maketree(ET.fromstring(xml), 0)
    
    return [ '{}{}({})'.format(level*"--", tag, ", ".join(sorted(attrib)))
                for (tag, level), attrib in tags.items() ]
