#!/usr/bin/python3
def safe_print_division(a, b):
	div = None
	try:
		div = a / b
	except ZeroDivisionError:
		return None
	else:
		return div
	finally:
		if b != 0:
			print("Inside result: {}".format(div))
		else:
			print("Inside result: {}".format(None))
