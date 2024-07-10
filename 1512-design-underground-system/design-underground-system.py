class UndergroundSystem:

    def __init__(self):
        # init  for mapping checked in
        self.checked_in = dict()

        # init for mapping  route(start,end) with time. and toatl cnt checked out
        self.avg_route_map = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        #  check in person 
        self.checked_in[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # chekc out
        start_route,checke_in_time =  self.checked_in[id]

        # check if route exist in route map
        if (start_route,stationName) not in self.avg_route_map:
            self.avg_route_map[(start_route,stationName)] = [0,0]
        
        # update values for route
        self.avg_route_map[(start_route,stationName)][0]+=(t-checke_in_time)
        self.avg_route_map[(start_route,stationName)][1]+=1    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg_route_map[(startStation,endStation)][0]/self.avg_route_map[(startStation,endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)