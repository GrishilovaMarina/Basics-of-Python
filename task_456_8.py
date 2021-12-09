class Warehouse:
    technique_dict = {}
    def __init__(self, techniques):
        self.techniques = techniques

class OfficeEquipment:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def add_technique(self, num):
        try:
            if str(num).isdigit():
                if self.name in Warehouse.technique_dict:
                    Warehouse.technique_dict[self.name] = Warehouse.technique_dict[self.name] + num
                else:
                    Warehouse.technique_dict[self.name] = num
            else:
                raise Exception()
        except:
            print('Некорректный ввод')

    def give_technique(self, num):
        if  self.name in Warehouse.technique_dict and Warehouse.technique_dict[self.name] >= num:
            Warehouse.technique_dict[self.name] = Warehouse.technique_dict[self.name] - num
            if self.name in Department.dep_technique_dict:
                Department.dep_technique_dict[self.name] = Department.dep_technique_dict[self.name] + num
            else:
                Department.dep_technique_dict[self.name] = num
        else:
            print('Недостаточное количество на складе')

class Printer(OfficeEquipment):
    def __init__(self, name, country = None, type = None, color = None):
        super().__init__(name, country)
        self.type = type
        self.color = color

class Scaner(OfficeEquipment):
    def __init__(self, name, country, scan_res):
        super().__init__(name, country)
        self.scan_res = scan_res

class Copier(OfficeEquipment):
    def __init__(self, name, country, speed):
        super().__init__(name, country)
        self.speed = speed

class Department:
    dep_technique_dict = {}
    name = 'Marketing'
    def __init__(self, name):
        self.name = name


Printer('Printer', 'China', 'laser', 'color').add_technique(5)
Scaner('Scaner', 'China', '4800').add_technique(2)
Copier('Copier', 'Japan', '20 page/min').add_technique(1)
print(Warehouse.technique_dict)
Printer('Printer').give_technique(2)
print(Warehouse.technique_dict)
print(Department.name, Department.dep_technique_dict)
