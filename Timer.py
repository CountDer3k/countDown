import time
import os
import emoji

ALARM_CLOCK = emoji.emojize(':alarm_clock:')
MINUTES_IN_HOUR = 60

def intput():
	return int(input())

def finishedCountDown():
	os.system('clear')
	for i in range(50):
		output = ALARM_CLOCK
		for j in range(15):
			output += '     ' + ALARM_CLOCK
		print(output)


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
	finishedCountDown()

print('Input time (in minutes): ')
inputTime = intput()
while(inputTime > 60):
	print('Input time (in minutes - less than 60min): ')
	inputTime = intput()
countDown(inputTime)