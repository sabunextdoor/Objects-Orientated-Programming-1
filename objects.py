class student:
    grade=11
    name="Sabu"
    def intro(self):
        print("my introduction")
    def details(self):
        print("my grade is",self.grade,"my name is", self.name)
obj=student()
obj.intro()
obj.details()
