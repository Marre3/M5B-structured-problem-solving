#!/usr/bin/env python3

import random

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


def close_target(n, targets):
	targets[n] = closed()
	return targets


def hits(targets):
	return len([t for t in targets if is_closed(t)])


def target_to_string(target):
	return "* " if not is_open(target) else "0 "


def targets_to_string(targets):
	return "".join([target_to_string(target) for target in targets])


def view_targets(targets):
	print(" ".join([str(n + 1) for n in range(len(targets))]))
	print(targets_to_string(targets))


def random_hit():
	return random.choice([True, False])


def shoot(targets, target):
	if random_hit():
		if is_open(targets[target]):
			close_target(target, targets)
			return "Hit on open target"
		else:
			return "Hit on closed target"
	else:
		return "Miss"


def parse_target(string):
	try:
		x = int(string)
	except ValueError:
		return None
	else:
		if 0 < x <= 5:
			return x - 1
		else:
			return None


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
ts = new_targets()
print(ts)
print(f"hits: {hits(ts)}")
for x in ts:
	print(is_open(x), is_closed(x))

ts = close_target(2, ts)
print(ts)
print(f"hits: {hits(ts)}")
for target in ts:
	print(target_to_string(target))
print(targets_to_string(ts))
view_targets(ts)
for i in range(10):
	print(random_hit())

print()
ts = new_targets()
for i in range(3):
	for j in range(len(ts)):
		print(shoot(ts, j))
		view_targets(ts)
		print()

print(parse_target("0"))
print(parse_target("1"))
print(parse_target("2"))
print(parse_target("3"))
print(parse_target("4"))
print(parse_target("5"))
print(parse_target("6"))
print(parse_target("-1"))
print(parse_target("0.5"))
print(parse_target("-123"))
print(parse_target("3.14159"))
print(parse_target("hej"))
print(parse_target("abc123"))
print(parse_target("0x4"))
