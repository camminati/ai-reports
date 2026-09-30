import re
from collections import Counter
def split(label):
    m=re.match(r'^(.+?)(?: \(([^)]*)\))?(?:: |, )(.*)$',label)
    if m and len(m.group(1))<60:
        pub,date,title=m.groups()
        # date in parens after title? keep
        return pub,(title+(' ('+date+')' if date else ''))
    return None,label
if __name__=='__main__':
    import srcbuild
