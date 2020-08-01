import time
import os
import emoji

ALARM_CLOCK = emoji.emojize(':alarm_clock:')
ALARM_CLOCK_2 = ALARM_CLOCK + ALARM_CLOCK
ALARM_CLOCK_8 = ALARM_CLOCK_2 + ALARM_CLOCK_2 + ALARM_CLOCK_2 + ALARM_CLOCK
TAB_10 = '\t\t'
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
	h = 0
	m = 0
	s = 0
	timeList = []
	if(len(x) == 8):
		# hours + min + sec
		h = int(x[0] + x[1])
		m = int(x[3] + x[4])
		s = int(x[6] + x[7])
	if(len(x) == 5):
		# minutes and seconds
		m = int(x[0] + x[1])
		s = int(x[3] + x[4])
	if(len(x) == 3):
		# seconds only
		s = int(x[1] + x[2])
	if(len(x) == 2):
		# Minutes only
		m = int(x[0] + x[1])
	if(len(x) == 1):
		m = int(x[0])
	timeList.append(h)
	timeList.append(m)
	timeList.append(s)
	return timeList


def countDown(hours, minutes, seconds):
	t = (hours * MINUTES_IN_HOUR * MINUTES_IN_HOUR) + (minutes * MINUTES_IN_HOUR) + seconds
	totalTime = str(minutes) + ':' + str(seconds)
	while t:
		os.system('clear')
		mins, secs = divmod(t, MINUTES_IN_HOUR)
		hour, mins = divmod(mins, MINUTES_IN_HOUR)
		timeLeft = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
		print(ALARM_CLOCK + ' Timer is set for: ' + str(totalTime) + ' minutes ' + ALARM_CLOCK)
		print(timeLeft, end='\n')
		time.sleep(1)
		t -= 1
	countDown_finished()

def showHelp():
	print('\n########################################################')
	print('Insturctions:')
	print('Separated time with \'.\' between hours, minutes & seconds')
	print('Example for 1 hour 10 minutes with 45 seconds: 01.10.45')
	print('For second only do: .XX ')
	print('For minutes only do: XX or X as input')
	print('X is any positive number')
	print('Requires 2 digits per area.')
	print('\n########################################################')
	prepareInput()

def prepareInput():
	print('\nInput time: ')
	inputTime = input()
	if(inputTime == 'help'):
		showHelp()
	else:
		hours = intput(inputTime)[0]
		minutes = intput(inputTime)[1]
		seconds = intput(inputTime)[2]
		while(hours > 24 or minutes > 60 or seconds > 60):
				print('\nHours, minutes, or seconds are too high \nMinutes and seconds must be less than 60 \nHours must be less than 24 \n\nInput time: ')
				inputTime = input()
				hours = intput(inputTime)[0]
				minutes = intput(inputTime)[1]
				seconds = intput(inputTime)[2]
		countDown(hours, minutes, seconds)

def main():
	print('\n########################################################')
	print('Insturctions:')
	print('Enter time separated by \'.\' between hours, minutes & seconds')
	print('For minutes only do: XX or X as input')
	print('X is any positive number')
	print('type \'help\' for more info')
	print('########################################################')
	prepareInput()
	

if __name__ == '__main__':
    main()




