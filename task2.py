def check_feai(spell):
    """Checks if there is spell in spell"""
    start, end = 0, 0
    for i in range(len(spell)-1):
        letter=spell[i]
        if letter=='f' and spell[i+1]=='e': start=i
        elif letter=='a' and spell[i+1]=='i': end=i
    return spell[start+2:end]

def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """
    grimoire={1:'dai',2:'ain',3:'ai',4:'jee',5:'je',6:'fe',7:'ne'}
    subspell_d={'fe':1,'je':2,'jee':3,'ain':3,'dai':5,'ne':2,'ai':2}
    subspells=subspell_d.values()
    dmg=0
    return dmg