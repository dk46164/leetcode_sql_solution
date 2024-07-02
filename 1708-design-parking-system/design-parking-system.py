class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # car slot space mapping
        self.car_slot_map = {1:big,2:medium,3:small}
        
    def addCar(self, carType: int) -> bool:
        
        # update variable
        self.car_slot_map[carType] = avl_flg = max( self.car_slot_map[carType]-1,-1)
        return avl_flg>-1



        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)