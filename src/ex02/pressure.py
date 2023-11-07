import random
import time

def emit_gel(step, initial_pressure):
    pressure = 50
    while True:
        pressure += random.uniform(0, step)
        if pressure > 100:
            pressure = 100
        if pressure < 0: 
            pressure = 0
        step = yield pressure

def valve(step, initial_pressure, sleep_time):
    gen = emit_gel(step, initial_pressure)
    i = next(gen)
    while True:
        if i > 90 or i < 10:
            gen.close()
            print("Generator was closed")
            return 
        if i > 80 or i < 20:
            step = -step
        i = gen.send(step)
        print(f"current pressure is {i}")
        time.sleep(sleep_time)

def main():
    valve(5, 50, 0.001)

if __name__ == "__main__":
    main()