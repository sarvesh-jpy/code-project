import random
import time

# Constants
DIRECTIONS = ["North", "South", "East", "West"]
CYCLE_TIME = 10  # seconds for green signal per cycle
SIMULATION_CYCLES = 5  # total traffic light cycles
MAX_ARRIVAL = 5  # max cars arriving per second
MAX_DEPARTURE = 2  # max cars leaving per second during red
GREEN_DEPARTURE = 7  # max cars leaving per second during green


class TrafficQueue:
    def __init__(self, direction):
        self.direction = direction
        self.queue_length = random.randint(10, 30)
        self.total_arrived = 0
        self.total_departed = 0

    def update_queue(self, green=False):
        # Simulate new vehicles arriving
        arrivals = random.randint(0, MAX_ARRIVAL)
        self.queue_length += arrivals
        self.total_arrived += arrivals

        # Simulate vehicles departing
        if green:
            departed = min(self.queue_length, GREEN_DEPARTURE)
        else:
            departed = min(self.queue_length, random.randint(0, MAX_DEPARTURE))

        self.queue_length -= departed
        self.total_departed += departed

        return arrivals, departed


class SignalController:
    def __init__(self, queues):
        self.queues = queues

    def decide_signal(self):
        # Choose the direction with the longest queue
        decision = max(self.queues, key=lambda q: q.queue_length)
        return decision.direction


def display_status(cycle, queues, green_direction):
    print(f"\n--- Cycle {cycle + 1} ---")
    for queue in queues:
        status = "GREEN" if queue.direction == green_direction else "RED"
        print(
            f"{queue.direction}: {queue.queue_length} vehicles | Signal: {status}"
        )


def simulation():
    queues = [TrafficQueue(direction) for direction in DIRECTIONS]
    controller = SignalController(queues)

    for cycle in range(SIMULATION_CYCLES):
        green_direction = controller.decide_signal()

        print("\n[Traffic Flow Optimization System - Real-Time Cycle Update]")
        display_status(cycle, queues, green_direction)

        # Simulate the cycle
        for queue in queues:
            is_green = queue.direction == green_direction
            arrivals, departures = queue.update_queue(green=is_green)
            print(
                f"{queue.direction}: +{arrivals} arrived, -{departures} departed"
            )

        time.sleep(2)  # simulate time delay

    print("\n--- Simulation Completed ---")
    print("\nFinal Statistics:")
    for queue in queues:
        print(
            f"{queue.direction}: Arrived={queue.total_arrived}, "
            f"Departed={queue.total_departed}, "
            f"Remaining={queue.queue_length}"
        )


if __name__ == "__main__":
    simulation()
		
		
		
