def create_dict(stream_lines,start_point,length):
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

def group_by(stream,sort_type):
    """Input: stream (file), sort_type == ['year','month']
    Output: dictionary {years/months : int}"""
    stream_lines=stream.readlines()
    start_point=stream_lines[0].find("Launch Date")
    length=4
    if sort_type=="month":
        start_point+=5
        length=3
    return create_dict(stream_lines[2:],start_point,length)