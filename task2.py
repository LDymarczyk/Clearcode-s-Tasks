grim_list=['jee','je','dai','aine','ain','ne']
grimoire={'fe':1,'je':2,'jee':3,'ain':3,'dai':5,'ne':2,'ai':2}
subspells=grimoire.keys()

def count_dmg1(spell):
    """Counts what damage spell deal"""
    dmg, bad_one, i = 0, 0, 0
    while i<len(spell)-2:
        #print str(spell[i:i+2]),str(spell[i:i+3])
        if spell[i:i+3] in subspells:
            dmg+=grimoire[spell[i:i+3]]
            i+=3
        elif spell[i:i+2] in subspells:
            dmg+=grimoire[spell[i:i+2]]
            i+=2
        else:
            bad_one+=1
            i+=1
    if i<len(spell):
        if spell[i:] in subspells:
            dmg+=grimoire[spell[i:]]
            i+=2
        else:
            dmg-=len(spell)-i
	#print dmg-bad_one
    return dmg-bad_one
	
def count_dmg2(spell):
    """Counts what damage spell deal"""
    dmg, bad_one, i = 0, 0, 0
    while i<len(spell)-2:
        #print str(spell[i:i+2]),str(spell[i:i+3])
        if spell[i:i+2] in subspells:
            dmg+=grimoire[spell[i:i+2]]
            i+=2
        elif spell[i:i+3] in subspells:
            dmg+=grimoire[spell[i:i+3]]
            i+=3
        else:
            bad_one+=1
            i+=1
    if i<len(spell):
        if spell[i:] in subspells:
            dmg+=grimoire[spell[i:]]
            i+=2
        else:
            dmg-=len(spell)-i
	#print dmg-bad_one
    return dmg-bad_one

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
    if "ai" in spell and spell.count('fe')==1:
        spell=check_feai(spell)
        if spell!=None:
            dmg+=3
            dmg1,dmg2=count_dmg1(spell),count_dmg2(spell)
            if (dmg1>dmg2): dmg+=dmg1
            else: dmg+=dmg2
    #print dmg
    if dmg<1: return 0
    return dmg