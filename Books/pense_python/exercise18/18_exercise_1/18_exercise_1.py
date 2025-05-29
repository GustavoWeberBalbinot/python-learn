'''
Para o seguinte programa, desenhe um diagrama de classe UML que mostre estas classes e as relações entre elas.

class PingPongParent:
    pass

class Ping(PingPongParent):
    def __init__(self, pong):
        self.pong = pong

class Pong(PingPongParent):
    def __init__(self, pings=None):
        if pings is None:
            self.pings = []
        else:
            self.pings = pings
    def add_ping(self, ping):
        self.pings.append(ping)

pong = Pong()
ping = Ping(pong)
pong.add_ping(ping)
'''

#Normal Arrow ->(HAS-A)
#Circle Arrow -o>(IS-A)
#* =(Multiplicity)
#Dashed Arrow -/->(Dependence)

'''
                    -o> Ping -/-> Pong
PingPongParent -o>      ^
                        /
                        -
                    -o> Pong -*-> Ping
            
'''
