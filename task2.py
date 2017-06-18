grim_list=['jee','je','dai','aine','ain','ai','ne']
grimoire={'fe':1,'je':2,'jee':3,'ain':3,'dai':5,'ne':2,'ai':2, 'aine':4}
subspells=grimoire.keys()

def delete_subspell(spell, subspell, count):
    """Function removes <subspell> from <spell> <count> times"""
    for i in range(count):
        spell=spell.replace(subspell, '')
    return spell
	
def count_dmg(spell):
    """Counts what damage spell deal"""
    dmg=0
    for i in grim_list:
        count=spell.count(i)
        dmg+=count*grimoire[i]
        spell=delete_subspell(spell, i, count)
    return dmg-len(spell)

def check_feai(spell):
    """Checks if there is spell in spell"""
    start, end = 0, 0
    for i in range(len(spell)-1):
        letter=spell[i]
        if letter=='f' and spell[i+1]=='e': start=i
        elif letter=='a' and spell[i+1]=='i': end=i
    if start<end: return spell[start+2:end]
    return None

def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """
    try:
        assert type(spell)==str
    except: return "Bad input, please enter string argument"
    else:
        dmg=0
        if "ai" in spell and spell.count('fe')==1:
            spell=check_feai(spell)
            if spell!=None:
                dmg+=3
                dmg+=count_dmg(spell)
        if dmg<1: return 0
        return dmg