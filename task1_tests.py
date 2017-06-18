from task1 import group_by

print "test with year, filter: None"
print group_by(open("launchlog.txt"),'year')
print "test with month, filter: None"
print group_by(open("launchlog.txt"),'month')
print "test with year, filter: failure"
print group_by(open("launchlog.txt"),'year',False)
print "test with year, filter: Succed"
print group_by(open("launchlog.txt"),'year',True)
print "test with bad argument"
print group_by(open("launchlog.txt"),'day',True)

assert group_by(open("launchlog.txt"),'year',True)['2016']+group_by(open("launchlog.txt"),'year',False)['2016']==group_by(open("launchlog.txt"),'year')['2016']
assert group_by(open("launchlog.txt"),'year',True)['2010']+group_by(open("launchlog.txt"),'year',False)['2010']==group_by(open("launchlog.txt"),'year')['2010']
assert group_by(open("launchlog.txt"),'year')['1957']==4
assert group_by(open("launchlog.txt"),'year')['1958']==28
assert group_by(open("launchlog.txt"),'year')['1959']==31
assert group_by(open("launchlog.txt"),'year')['1960']==66

assert group_by(open("launchlog.txt"),'year',True)['1958']==8 #I count it by myself