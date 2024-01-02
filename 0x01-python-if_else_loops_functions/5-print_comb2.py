#!/usr/bin/python3
for iter in range(0, 100):
    if (iter == 99):
        print(f"{iter:02d}")
    else:
        print(f"{iter:02d}", end=", ")
    iter += 1
