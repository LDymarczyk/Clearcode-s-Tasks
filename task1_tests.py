from task1 import group_by

print group_by(open("launchlog.txt"),'year')
print group_by(open("launchlog.txt"),'month',False)