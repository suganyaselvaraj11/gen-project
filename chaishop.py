class chai:
    def _init_(self,sweetness,milk_level):
        self.sweetness=sweetness
        self.milk_level=milk_level
    def sip(self):
        print("Sipping chai")
    def add_sugar(self,amount):
       
        mychai = chai(sweetness=3,milk_level=2)
        mychai.add_sugar(3)
        