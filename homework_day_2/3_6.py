import math
name=raw_input('Enter employee is name:')
hours=eval(raw_input('Enter number of hours worked in a week:'))
rate=eval(raw_input('Ente hourly pay rate:'))
federal=eval(raw_input('Enter feaderal tax withholding rate:'))
state=eval(raw_input('Enter state tax withholding rate:'))
print('Employee Name:'+name)
print('Hours Worked:'+str(hours))
print('Pay Rate:'+str(rate))
print('Gross Pay:'+str(hours*rate))
print('Deductions:')
print('  Federal Withholding'+'('+str(federal*100)+'%):'+'$'+str(round(hours*rate*federal,2)))
print('  State Withholding'+'('+str(state*100)+'%):'+'$'+str(round(hours*rate*state,2)))
print('  Total Deduction:$'+str(round(hours*rate*(federal+state),2)))
print('Net Pay:$'+str(round(hours*rate*(1-federal-state),2)))
