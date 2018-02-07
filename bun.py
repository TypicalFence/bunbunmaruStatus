# TODO delete this file before release
import sys
import time
import bunbunmarustatus as bun


try:
    interval = int(sys.argv[1])
except:
    interval = 5


status = bun.Status("{{battery}} {{time}}")

bun.Time().register(status)
bun.Battery().register(status)

while True:
    print(status.get_status())
    time.sleep(interval)
