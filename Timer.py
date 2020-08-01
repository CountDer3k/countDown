import time
import os
import emoji

ALARM_CLOCK = emoji.emojize(':alarm_clock:')
ALARM_CLOCK_2 = ALARM_CLOCK + ALARM_CLOCK
ALARM_CLOCK_3 = ALARM_CLOCK + ALARM_CLOCK + ALARM_CLOCK
ALARM_CLOCK_8 = ALARM_CLOCK_2 + ALARM_CLOCK_2 + ALARM_CLOCK_2 + ALARM_CLOCK
TAB_10 = '\t\t'
#TAB_12 = TAB_10 + TAB_10#
MINUTES_IN_HOUR = 60

def countDown_finished():
	os.system('clear')
	print('                                                               ')
	print('    ###########   ##########     ###  ###     ######   ######  ')
	print('         ##           ##        ##  ##  ##    ##       ##      ')
	print('         ##           ##       ##   ##   ##   ##       ##      ')
	print('         ##           ##       ##   ##   ##   ####     ######  ')
	print('         ##           ##       ##   ##   ##   ##           ##  ')
	print('         ##       ##########   ##   ##   ##   ######   ######  ')
	print('                                                               ')
	print('                                                               ')
	print('                ##       ##   ########    ##   ##   ##         ')
	print('                ##       ##   ##     ##   ##   ##   ##         ')
	print('                ##       ##   ##    ##    ##   ##   ##         ')
	print('                ##       ##   #######     ##   ##   ##         ')
	print('                ##       ##   ##          ##   ##   ##         ')
	print('                 ##     ##    ##                               ')
	print('                  #######     ##          ##   ##   ##         ')
	print('                                                               \n\n\n')
	clockEmoji()

def clockEmoji():
	print(TAB_10 + '         ' + ALARM_CLOCK_8 + '       ')
	print(TAB_10 + '     ' + ALARM_CLOCK_2 + '             ' + ALARM_CLOCK_2 + '     ')
	print(TAB_10 + '  ' + ALARM_CLOCK_2 + '                    ' + ALARM_CLOCK_2 + '  ')

	print(TAB_10 + ALARM_CLOCK_2 + '                        ' + ALARM_CLOCK_2)
	print(TAB_10 + ALARM_CLOCK + '             ' + ALARM_CLOCK + '             ' + ALARM_CLOCK)
	print(TAB_10 + ALARM_CLOCK + '             ' + ALARM_CLOCK + '             ' + ALARM_CLOCK)
	print(TAB_10 + ALARM_CLOCK + '             ' + ALARM_CLOCK + '    ' + ALARM_CLOCK + '       ' + ALARM_CLOCK)
	print(TAB_10 + ALARM_CLOCK + '             ' + ALARM_CLOCK + '  ' + ALARM_CLOCK + '         ' + ALARM_CLOCK)
	print(TAB_10 + ALARM_CLOCK + '             ' + ALARM_CLOCK_2 + '           ' + ALARM_CLOCK)
	print(TAB_10 + ALARM_CLOCK + '                            ' + ALARM_CLOCK)
	print(TAB_10 + ALARM_CLOCK + '                            ' + ALARM_CLOCK)
	print(TAB_10 + ALARM_CLOCK_2 + '                        ' + ALARM_CLOCK_2)
	
	print(TAB_10 + '  ' + ALARM_CLOCK_2 + '                    ' + ALARM_CLOCK_2 + '  ')
	print(TAB_10 + '     ' + ALARM_CLOCK_2 + '              ' + ALARM_CLOCK_2 + '     ')
	print(TAB_10 + '         ' + ALARM_CLOCK_8 + '       \n\n')




def intput(x):
	m = ''
	s = ''
	time = []
	splitFound = False
	if('.' in x):
		for i in range (len(x)):
			if(x[i] == '.'):
				splitFound = True
			if(not splitFound):
				m += x[i]
			else:
				if(x[i] != '.'):
					s += x[i]
		time.append(int(m))
		time.append(int(s))
	else:
		time.append(int(x))
		time.append(0)
	return time

def countDown(minutes, seconds):
	t = (minutes * MINUTES_IN_HOUR) + seconds
	totalTime = str(minutes) + ':' + str(seconds)
	while t:
		os.system('clear')
		mins, secs = divmod(t, MINUTES_IN_HOUR)
		timeLeft = '{:02d}:{:02d}'.format(mins, secs)
		print(ALARM_CLOCK + ' Timer is set for: ' + str(totalTime) + ' minutes ' + ALARM_CLOCK)
		print(timeLeft, end='\n')
		time.sleep(1)
		t -= 1
	countDown_finished()



print('\n########################################################')
print('Insturctions:')
print('Enter amount of minutes separated by seconds with a \'.\'')
print('Example for 10 minutes with 45 seconds: 10.45')
print('For second only do: .XX ')
print('For minutes only do: XX')
print('########################################################')
print('\nInput time: ')


inputTime = input()
minutes = intput(inputTime)[0]
seconds = intput(inputTime)[1]
while(minutes > 60 or seconds > 60):
	print('Minutes and seconds must be less than 60 each \n Input time: ')
	time = input()
	minutes = intput(time)[0]
	seconds = intput(time)[1]
countDown(minutes,seconds)


if(False):
	inputTime = input()
	while(inputTime > 60):
		print('Input time (in minutes - less than 60min): ')
		inputTime = input()
	countDown(inputTime)
	#countDown(inputTime)





