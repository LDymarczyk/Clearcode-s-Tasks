grimoire={'fe':1,'je':2,'jee':3,'ain':3,'dai':5,'ne':2,'ai':2}
subspells=grimoire.values()

def count_dmg(spell):
	"""Counts what damage spell deal"""
	dmg=0
	
	i=0
	while i<len(spell)-2:
	    if spell[i:i+1] in subspell:
		    dmg+=grimoire[spell[i:i+1]]
			i+=2
		
	return dmg

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
    dmg=0
	if "fe" in spell and "ai" in spell:
	    spell=check_feai(spell)
		if spell!=None:
		    dmg+=3
			dmg+=count_dmg(spell)
    return dmg