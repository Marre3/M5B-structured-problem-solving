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
	print(" ".join([str(n) for n in range(len(targets))]))
	print(targets_to_string(targets))


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
