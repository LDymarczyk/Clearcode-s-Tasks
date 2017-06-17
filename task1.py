def create_dict(stream_lines,start_point,length,success,suc_pointer):
    """Creating dictionary {years/months : int}"""
    dict={}
    for line in stream_lines:
        key=line[start_point:start_point+length]
        if key!='    ' and key!='   ':
            keys=dict.keys()
            if key in keys:
                dict[key]+=1
            else:
                dict[key]=1
    return dict

def group_by(stream,field,succes):
    """Input: stream (file), field == ['year','month']
    Output: dictionary {years/months : int}"""
    stream_lines=stream.readlines()
    start_point,suc_pointer=stream_lines[0].find("Launch Date"),stream_lines[0].find("Suc")
    length=4
    if field=="month":
        start_point+=5
        length=3
    return create_dict(stream_lines[2:],start_point,length,success,suc_pointer)