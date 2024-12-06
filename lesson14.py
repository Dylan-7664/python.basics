class Criminal:
    def __init__(self, name, id_number, crime, gender):
        self.name = name
        self.id_number = id_number
        self.crime = crime
        self.gender = gender
    def show_details(self):
        print(f"Name : {self.name} \nID: {self.id_number}\nIssue: {self.crime}\nGender: {self.gender}")
c1 = Criminal("John Dukes", "2444555", "Stealing power cables", "M")
c1.show_details()