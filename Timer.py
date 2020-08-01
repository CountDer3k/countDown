import time
import os
import emoji

ALARM_CLOCK = emoji.emojize(':alarm_clock:')
ALARM_CLOCK_2 = ALARM_CLOCK + ALARM_CLOCK
ALARM_CLOCK_3 = ALARM_CLOCK + ALARM_CLOCK + ALARM_CLOCK
ALARM_CLOCK_8 = ALARM_CLOCK_2 + ALARM_CLOCK_2 + ALARM_CLOCK_2 + ALARM_CLOCK
TAB_10 = '\t\t'
TAB_12 = TAB_10 + TAB_10
MINUTES_IN_HOUR = 60

def intput():
	return int(input())

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





def countDown(t):
	totalTime = t
	t = t * MINUTES_IN_HOUR
	while t:
		os.system('clear')
		mins, secs = divmod(t, MINUTES_IN_HOUR)
		timeLeft = '{:02d}:{:02d}'.format(mins, secs)
		print(ALARM_CLOCK + ' Timer is set for: ' + str(totalTime) + ' minutes ' + ALARM_CLOCK)
		print(timeLeft, end='\n')
		time.sleep(1)
		t -= 1
	countDown_finished()


print('Input time (in minutes): ')
inputTime = intput()
while(inputTime > 60):
	print('Input time (in minutes - less than 60min): ')
	inputTime = intput()
countDown(inputTime)