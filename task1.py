def create_dict(stream_lines,start_point,length,success,suc_pointer):
    """Creating dictionary {years/months : int}"""
    dict={}
    for line in stream_lines:
        #key is a year or a month 
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
        #if key is empty that means it's equal last key we know
        elif success in [suc, None]:
            dict[last_key]+=1
    return dict

def group_by(stream,field,success=None):
    """Input: stream (file), field == ['year','month']
    Output: dictionary {years/months : int}"""
    try:
        assert field in ['year','month'] and success in [True,False,None]
    except: return "Bad inputs"
    else:
        stream_lines=stream.readlines()
        #finding columns 'Launch Date' and 'Suc' in file, length = 4 for year or 3 for month
        start_point,suc_pointer=stream_lines[0].find("Launch Date"),stream_lines[0].find("Suc")
        length=4
        if field=="month":
            start_point+=5
            length=3
        #changing values of success in 'S' or 'F' or None
        if success==True: success='S'
        elif success==False: success='F'
        return create_dict(stream_lines[2:],start_point,length,success,suc_pointer)
