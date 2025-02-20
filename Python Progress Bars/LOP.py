import sys
import time
from threading import Thread

class IndefiniteProgress(Thread):
	"""
	Implements a sub-class of threads for loading animations when progress
	is unknown
	"""
	
	def __init__(self, number_of_dots, text):
		Thread.__init__(self)
		self._number_of_dots = number_of_dots
		self._text = text
		self._exit_thread = False
		
	def clear(self):
		sys.stdout.write(f"\r{self._text}{' '*self._number_of_dots}")
		
	def run(self):
		counter = 0
		while not self._exit_thread:
			sys.stdout.write(f"\r{self._text}{'.'*counter}")
			time.sleep(0.5)
			counter += 1
			
			if counter >= self._number_of_dots+1:
				counter = 0
				self.clear()
		self.clear()
		sys.stdout.write(f"\r{self._text}{'.'*self._number_of_dots}Done\n")
			
	def kill(self):
		self._exit_thread = True

# Definite Progress
	"""
	Contains implementations of progress bars where progress is between
	0% and 100%
	"""
def progressBar(percent, size=50, opening='[', closing=']', head='>', fill='=', empty='.'):
	if percent >= 1.0:
		sys.stdout.write(f"\r{opening}{fill*round(percent*size)}{empty*(size-round(percent*size))}{closing} {percent*100:.2f}%")
	else:
		sys.stdout.write(f"\r{opening}{fill*round(percent*size)}{head}{empty*(size-round(percent*size))}{closing} {percent*100:.2f}%")
	

def main():
#	total = 17
#	for x in range(1, total+1):		
#		progressBar(x/total, size=25)
#		time.sleep(0.5)
#	print()

	IP = IndefiniteProgress(3, "Loading")
	IP.start()
	time.sleep(5)
	IP.kill()

if __name__ == "__main__":
	main()