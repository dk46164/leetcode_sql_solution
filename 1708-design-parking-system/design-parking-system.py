class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # car slot space mapping
        self.car_slot_map = {1:big,2:medium,3:small}
        
    def addCar(self, carType: int) -> bool:
        # check if car slot space is available
        avl_flg = self.car_slot_map[carType]>0
        
        # update variable
        self.car_slot_map[carType] = self.car_slot_map[carType]-1  if \
                                                self.car_slot_map[carType]>0  else 0
        return avl_flg



        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)