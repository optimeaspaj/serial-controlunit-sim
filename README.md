# Python Serielles Steuergerät Simulator

Kleines Python Helferskript, um eine Steuergerät zu simulieren, dass sich wie folgt verhält:

Verhalten:
- Öffnet eine serielle Schnittstelle
- wartet bis es ein vorher definiertes steurzeichen(kette) über die offene schnittstelle eingelesen wurde
- schreibt danach auf der offenen schnittstelle einen Block an Daten. 

## Nutzung
Starten des Prozess im Hintergrund ohne hang up:

  nohup ./device-sim.py
