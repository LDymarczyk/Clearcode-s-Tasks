def group_by(stream,sort_type):
    """Input: stream (file), sort_type == ['year','month']
    Output: dictionary {years/months : int}"""
    stream_lines=stream.readlines()
    start_point=stream_lines[0].find("Launch Date")
	length=4
	if sort_type=="month":
		start_point+=5
		length=3
    return start_point