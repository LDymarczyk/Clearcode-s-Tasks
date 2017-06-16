def group_by(stream,sort_type):
    """Input: stream (file), sort_type == ['year','month']
    Output: dictionary {years/months : int}"""
    stream_lines=stream.readlines()
    date_start=stream_lines[0].find("Launch Date")
	return date_start