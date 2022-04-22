from random import randint



class Elevator:


    current_floor = 1
    max_passengers = 5
    current_passengers = 0
    passengers_list = []
    status = '<< waitnig for outer request >>'


    def console(self):
        print(f'''
current floor           {self.current_floor}
current passangers      {self.current_passengers}
status                  {self.status}
        ''')


    def __init__(self):
        print('Elevator is switched on')
        self.console()


    def get_passengers(self, passengers):
        print('open door')
        self.current_passengers += len(passengers)
        self.passengers_list.extend(passengers)
        print('get passengers')
        print('close door')


    def go_to_floor(self, passengers: list):
        while self.current_floor != max(passengers):
            self.current_floor += 1
            if self.current_floor in passengers:
                self.current_passengers -= passengers.count(self.current_floor)
            self.console()
            print(self.passengers_list)


        

    def get_building(self, building: dict):
        for floor, passengers in building.items():
            if floor == self.current_floor:
                self.get_passengers(passengers)
                self.status = f'<< go to floor {max(passengers)} >>'
                self.console()
                self.go_to_floor(passengers)



building = {
    5: [1],
    4: [2],
    3: [1],
    2: [1, 5],
    1: [2, 2, 5],
}


a = Elevator()
a.get_building(building)