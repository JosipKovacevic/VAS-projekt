#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import spade
import random
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
import time

template = spade.template.Template(metadata={"ontology": "game"})
msg_meta = {"ontology": "game", "language": "english", "preformative": "inform"}


class Boja:
    Zuta = '\033[93m'
    Zelena = '\033[92m'
    Kraj = '\033[0m'
    
par = -1
nepar = -1
rezultatPero = 0
rezultatKreso = 0
igraDo = 5

class Golem(Agent):
      
    def __init__(self, *args, imeAgenta, imeProtivnika, igra, boja,  broj, **kwargs):
        super().__init__(*args, **kwargs)
        self.imeAgenta = imeAgenta
        self.imeProtivnika = imeProtivnika
        self.igra = igra
        self.boja = boja
        self.broj = broj

    class Igra(PeriodicBehaviour):
        async def run(self):
            global msg_meta
            time.sleep(1)
            self.agent.broj = random.randint(1,10)
            self.agent.broj = int(self.agent.broj)
            print(f"{self.agent.boja}{self.agent.imeAgenta}: Par-Nepar-Bim-Bam-Bus!! {self.agent.broj}{Boja.Kraj}" )
            msg = spade.message.Message(to=self.agent.imeProtivnika, body=str(self.agent.broj), metadata=msg_meta)
            await self.send(msg)
            self.agent.remove_behaviour(self)
            self.agent.add_behaviour(self.agent.Racunanje(period=2), template)

    class Racunanje(PeriodicBehaviour):
        async def run(self):
            global msg_meta
            global template
            global par
            global nepar
            global rezultatPero
            global rezultatKreso
            global igraDo
            msg = await self.receive(timeout=10)
            
            if par == -1:
                par= int(msg.body)
                nepar = -1
                self.agent.remove_behaviour(self)
                self.agent.add_behaviour(self.agent.Igra(period=2), template)
                return

            if (nepar == -1):
                nepar= int(msg.body)
                score = par+nepar
                score = score % 2

                if(rezultatPero < igraDo and rezultatKreso < igraDo):
                    
                    if (score ==0):
                    	time.sleep(2)
                    	rezultatPero = rezultatPero +1
                    	rezultat = par + nepar
                    	print(par, "+", nepar, "=", rezultat, "To je parno, Pero je pobijedio. Trenutni rezultat je Pero:", rezultatPero, "-- Kreso:", rezultatKreso)
                    	par = -1
                    	
                    	if rezultatPero != igraDo:
                    	    self.agent.remove_behaviour(self)
                    	    self.agent.add_behaviour(self.agent.Igra(period=2), template)
                    	    
                    	else:
                    	    print("Pero je pobjednik igre!! Cestitam!! :)")
                    	    time.sleep(1000)
                    	    return
                
                    if (score ==1):
                    	time.sleep(2)
                    	rezultatKreso = rezultatKreso +1
                    	rezultat = par + nepar
                    	print(par, "+", nepar, "=", rezultat, "To je neparno, Kreso je pobijedio. Trenutni rezultat je Pero:", rezultatPero, "-- Kreso:", rezultatKreso)
                    	par = -1
                    	
                    	if rezultatKreso != igraDo:
                    	    self.agent.remove_behaviour(self)
                    	    self.agent.add_behaviour(self.agent.Igra(period=2), template)
                    	    
                    	else:
                    	    print("Kreso je pobjednik igre!! Cestitam!! :)")
                    	    time.sleep(1000)
                    	    return

    async def setup(self):
        print(f"Pokrecem se!!")
        if self.igra == True:
            behaviour = self.Igra(period=2)
        else:
            start_at = datetime.now() + timedelta(seconds=2)
            behaviour = self.Racunanje(period=2)
        self.add_behaviour(behaviour, template)
        
class neparniGolem(Agent):
      
    def __init__(self, *args, imeAgenta, imeProtivnika, igra, boja,  broj, **kwargs):
        super().__init__(*args, **kwargs)
        self.imeAgenta = imeAgenta
        self.imeProtivnika = imeProtivnika
        self.igra = igra
        self.boja = boja
        self.broj = broj

    class Igra(PeriodicBehaviour):
        async def run(self):
            global msg_meta
            time.sleep(1)
            neparniBrojevi = [1,3,5,7,9]
            self.agent.broj = random.choice(neparniBrojevi)
            self.agent.broj = int(self.agent.broj)
            print(f"{self.agent.boja}{self.agent.imeAgenta}: Par-Nepar-Bim-Bam-Bus!! {self.agent.broj}{Boja.Kraj}" )
            msg = spade.message.Message(to=self.agent.imeProtivnika, body=str(self.agent.broj), metadata=msg_meta)
            await self.send(msg)
            self.agent.remove_behaviour(self)
            self.agent.add_behaviour(self.agent.Racunanje(period=2), template)

    class Racunanje(PeriodicBehaviour):
        async def run(self):
            global msg_meta
            global template
            global par
            global nepar
            global rezultatPero
            global rezultatKreso
            global igraDo
            msg = await self.receive(timeout=10)
            
            if par == -1:
                par= int(msg.body)
                nepar = -1
                self.agent.remove_behaviour(self)
                self.agent.add_behaviour(self.agent.Igra(period=2), template)
                return

            if (nepar == -1):
                nepar= int(msg.body)
                score = par+nepar
                score = score % 2

                if(rezultatPero < igraDo and rezultatKreso < igraDo):
                    
                    if (score ==0):
                    	time.sleep(2)
                    	rezultatPero = rezultatPero +1
                    	rezultat = par + nepar
                    	print(par, "+", nepar, "=", rezultat, ". To je parno, Pero je pobijedio. Trenutni rezultat je Pero:", rezultatPero, "-- Kreso:", rezultatKreso)
                    	par = -1
                    	
                    	if rezultatPero != igraDo:
                    	    self.agent.remove_behaviour(self)
                    	    self.agent.add_behaviour(self.agent.Igra(period=2), template)
                    	    
                    	else:
                    	    print("Pero je pobjednik igre!! Cestitam!! :)")
                    	    time.sleep(1000)
                
                    if (score ==1):
                    	time.sleep(2)
                    	rezultatKreso = rezultatKreso +1
                    	rezultat = par + nepar
                    	print(par, "+", nepar, "=", rezultat, ". To je neparno, Kreso je pobijedio. Trenutni rezultat je Pero:", rezultatPero, "-- Kreso:", rezultatKreso)
                    	par = -1
                    	
                    	if rezultatKreso != igraDo:
                    	    self.agent.remove_behaviour(self)
                    	    self.agent.add_behaviour(self.agent.Igra(period=2), template)
                    	    
                    	else:
                    	    print("Kreso je pobjednik igre!! Cestitam!! :)")
                    	    time.sleep(1000)

    async def setup(self):
        print(f"Pokrecem se!!")
        if self.igra == True:
            behaviour = self.Igra(period=2)
        else:
            start_at = datetime.now() + timedelta(seconds=2)
            behaviour = self.Racunanje(period=2)
        self.add_behaviour(behaviour, template)
        
class parniGolem(Agent):
      
    def __init__(self, *args, imeAgenta, imeProtivnika, igra, boja,  broj, **kwargs):
        super().__init__(*args, **kwargs)
        self.imeAgenta = imeAgenta
        self.imeProtivnika = imeProtivnika
        self.igra = igra
        self.boja = boja
        self.broj = broj

    class Igra(PeriodicBehaviour):
        async def run(self):
            global msg_meta
            time.sleep(1)
            neparniBrojevi = [2,4,6,8,10]
            self.agent.broj = random.choice(neparniBrojevi)
            self.agent.broj = int(self.agent.broj)
            print(f"{self.agent.boja}{self.agent.imeAgenta}: Par-Nepar-Bim-Bam-Bus!! {self.agent.broj}{Boja.Kraj}" )
            msg = spade.message.Message(to=self.agent.imeProtivnika, body=str(self.agent.broj), metadata=msg_meta)
            await self.send(msg)
            self.agent.remove_behaviour(self)
            self.agent.add_behaviour(self.agent.Racunanje(period=2), template)

    class Racunanje(PeriodicBehaviour):
        async def run(self):
            global msg_meta
            global template
            global par
            global nepar
            global rezultatPero
            global rezultatKreso
            global igraDo
            msg = await self.receive(timeout=10)
            
            if par == -1:
                par= int(msg.body)
                nepar = -1
                self.agent.remove_behaviour(self)
                self.agent.add_behaviour(self.agent.Igra(period=2), template)
                return

            if (nepar == -1):
                nepar= int(msg.body)
                score = par+nepar
                score = score % 2

                if(rezultatPero < igraDo and rezultatKreso < igraDo):
                    
                    if (score ==0):
                    	time.sleep(2)
                    	rezultatPero = rezultatPero +1
                    	rezultat = par + nepar
                    	print(par, "+", nepar, "=", rezultat, ". To je parno, Pero je pobijedio. Trenutni rezultat je Pero:", rezultatPero, "-- Kreso:", rezultatKreso)
                    	par = -1
                    	
                    	if rezultatPero != igraDo:
                    	    self.agent.remove_behaviour(self)
                    	    self.agent.add_behaviour(self.agent.Igra(period=2), template)
                    	    
                    	else:
                    	    print("Pero je pobjednik igre!! Cestitam!! :)")
                    	    time.sleep(1000)
                
                    if (score ==1):
                    	time.sleep(2)
                    	rezultatKreso = rezultatKreso +1
                    	rezultat = par + nepar
                    	print(par, "+", nepar, "=", rezultat, ". To je neparno, Kreso je pobijedio. Trenutni rezultat je Pero:", rezultatPero, "-- Kreso:", rezultatKreso)
                    	par = -1
                    	
                    	if rezultatKreso != igraDo:
                    	    self.agent.remove_behaviour(self)
                    	    self.agent.add_behaviour(self.agent.Igra(period=2), template)
                    	    
                    	else:
                    	    print("Kreso je pobjednik igre!! Cestitam!! :)")
                    	    time.sleep(1000)

    async def setup(self):
        print(f"Pokrecem se!!")
        if self.igra == True:
            behaviour = self.Igra(period=2)
        else:
            start_at = datetime.now() + timedelta(seconds=2)
            behaviour = self.Racunanje(period=2)
        self.add_behaviour(behaviour, template)
    
if __name__ == '__main__':
    Pero = Golem("pero@localhost", "password", imeAgenta="Pero", imeProtivnika="kreso@localhost", igra=True, boja=Boja.Zuta, broj = 0)
    Kreso = Golem("kreso@localhost", "password", imeAgenta="Kreso", imeProtivnika="pero@localhost", igra=False, boja=Boja.Zelena,  broj = 0)
    Kreso.start()
    Pero.start()
    input("Press Enter to exit.\n")
    Kreso.stop()
    Pero.stop()
    spade.quit_spade()
