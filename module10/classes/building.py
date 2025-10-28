from .elevator import Elevator

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))
        print(f"Building created with {num_elevators} elevators "
              f"({bottom_floor} to {top_floor}).")

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number.")
            return
        print(f"\nRunning elevator {elevator_number}:")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("FIRE ALARM! Moving all elevators to bottom floor!")
        for i, elevator in enumerate(self.elevators):
            print(f"Moving elevator {i} to safety:")
            elevator.go_to_floor(self.bottom_floor)