from os import path as p

class CarBase:


    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext (self):
        extension = p.splitext(self.photo_file_name)
        return extension[-1]




class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'

        dimensions = []
        try:
            for d in body_whl.split("x"):
                dimensions.append(float(d))
            self.body_length = dimensions[0]
            self.body_width = dimensions[1]
            self.body_height = dimensions[2]
        except:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
        if len(dimensions) > 3:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0


    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'

def get_car_list(csv_filename):
    import csv
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            #print(row)
            if len(row) > 6 and row[0] == 'car' and row[1] != '' and row[2].isnumeric() and '.' in row[3] and row[5]!= '':
                car_list.append(Car(row[1], row[3], float(row[5]), row[2]))
            if len(row) > 6 and row[0] == 'truck' and row[1] != '' and '.' in row[3] and row[5] != '':
                car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))
            if len(row) > 6 and row[0] == 'spec_machine' and row[1] != '' and '.' in row[3] and row[6] != '' and row[5] != '':
                car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))

    return car_list




if __name__ == "__main__":
    # execute only if run as a script

    # b = Truck ("Kamaz", "abc.jpegf", 1000, "3x4x5")
    # print(b.get_body_volume())
    #c = [param if param.is_integer() else 0 for param in list (map(float,b.split("x")))]
    #c = [float(param) if param.isdigit() else 0 for param in b.split("x")]

    cars = get_car_list("coursera_week3_cars.csv")
    print(len(cars))

    car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
    print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep = '\n')

    truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
    print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep = '\n')

    spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
    print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep = '\n')

    print(spec_machine.get_photo_file_ext())

    cars = get_car_list("coursera_week3_cars.csv")
    print(len(cars))
    for car in cars:
        print(type(car))
    print ( cars[0].passenger_seats_count)
    print(cars[1].get_body_volume())