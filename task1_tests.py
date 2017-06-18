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
