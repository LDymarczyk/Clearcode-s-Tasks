def create_dict(stream_lines,start_point,length,success,suc_pointer):
    """Creating dictionary {years/months : int}"""
    dict={}
    for line in stream_lines:
        if len(line)>=suc_pointer:
            key,suc=line[start_point:start_point+length],line[suc_pointer]
            if success in [suc, None]:#key!='    ' and key!='   ' and success in [suc, None]:
                keys=dict.keys()
                if key in keys:
                    dict[key]+=1
                else:
                    dict[key]=1
    return dict

def group_by(stream,field,success=None):
    """Input: stream (file), field == ['year','month']
    Output: dictionary {years/months : int}"""
    stream_lines=stream.readlines()
    start_point,suc_pointer=stream_lines[0].find("Launch Date"),stream_lines[0].find("Suc")
    length=4
    print suc_pointer, stream_lines[0], len(stream_lines[2])
    if field=="month":
        start_point+=5
        length=3
    if success==True:
        success='S'
    else: success='F'
    return create_dict(stream_lines[2:],start_point,length,success,suc_pointer)