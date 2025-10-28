class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"you are at floor: {self.current_floor}")
        else:
            print(f"you are already at top floor")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"you are at floor: {self.current_floor}")
        else:
            print(f"you are already at bottom floor")

    def go_to_floor(self, target_floor):
        if self.top < target_floor or self.bottom > target_floor:
            print("Floor is out of range!")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print('Successfully arrived to the target floor!')