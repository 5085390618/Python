from time import sleep

class TtafficLight:
    __color = ['Red', 'Yellow', 'Green']
    def running(self):
        i = 0
        while i != 3:
            print(TtafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1

trafficlight = TtafficLight()
trafficlight.running()
