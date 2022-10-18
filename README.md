# Python Serielles Steuergerät Simulator

Kleines Python Helferskript, um eine Steuergerät zu simulieren, dass sich wie folgt verhält:

Vrhalten:
- Öffnet zu Anfang eine seriellen Schnittstelle
- wartet bis es ein vorher definiertes steurzeichen(kette) über die offene schnittstelle einliest
- und dann auf der offenen schnittstelle einen Block an Daten schreibt