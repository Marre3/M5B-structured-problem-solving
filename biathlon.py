#!/usr/bin/env python3

splash_str = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              Biathlon

         a hit or miss game
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def open():
	return 0


def closed():
	return 1


def is_open(target):
	return target == open()


def is_closed(target):
	return target == closed()


def new_targets():
	return [open()] * 5


def splash():
	print(splash_str)


def main():
	splash()


if __name__ == "__main__":
	main()


## Test
print(open())
print(closed())
print(is_open(open()))
print(is_closed(open()))
print(new_targets())
for x in new_targets():
	print(is_open(x), is_closed(x))
