def create_dict(stream_lines,start_point,length,success,suc_pointer):
    """Creating dictionary {years/months : int}"""
    dict={}
    for line in stream_lines:
        key=line[start_point:start_point+length]
        if key!='    ' and key!='   ':
            suc=line[suc_pointer]
            if success in [suc, None]:
                keys=dict.keys()
                if key in keys:
                    dict[key]+=1
                else:
                    dict[key]=1
                last_key=key
        elif success in [suc, None]:
            dict[last_key]+=1
    return dict

def group_by(stream,field,success=None):
    """Input: stream (file), field == ['year','month']
    Output: dictionary {years/months : int}"""
    try:
        assert field in ['year','month'] and success in [True,False,None]
    except: print "Bad inputs"
    stream_lines=stream.readlines()
    start_point,suc_pointer=stream_lines[0].find("Launch Date"),stream_lines[0].find("Suc")
    length=4
    if field=="month":
        start_point+=5
        length=3
    if success==True: success='S'
    elif success==False: success='F'
    return create_dict(stream_lines[2:],start_point,length,success,suc_pointer)