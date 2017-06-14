assert damage('feeai') == 2
assert damage('feaineain') == 1 + 2 + 2 + 2 == 7 ##(fe-ai-ne-ai) - not (fe-ain-ai) because 1+3+2 = 6
assert damage('jee') == 0
assert damage('fefefefefeaiaiaiaiai') == 0 ##(more than one 'fe')
assert damage('fdafafeajain') == 1 ##(fe-ai) 3 - 2 ##(because 'aj')
assert damage('fexxxxxxxxxxai') == 0 ##(3-10 = -7 < 0)