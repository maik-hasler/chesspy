# Projektdokumentation
Das Schachspielprojekt ist ein Multiplayer-Schachspiel, das aus einem Server und einem oder zwei Clients besteht. Der Server synchronisiert das Schachbrett zwischen den verbundenen Clients und überwacht das Spiel. Der Client ermöglicht es dem Benutzer, das Schachspiel über eine grafische Benutzeroberfläche zu spielen.

# Inhaltsverzeichnis
- [Einleitung](#projektdokumentation)
- [Inhaltsverzeichnis](#inhaltsverzeichnis)
- [Voraussetzungen](#voraussetzungen)
- [Funktionen](#funktionen)
- [Erweiterungsmöglichkeiten]()
- [Technische Details](#technische-details)

# Voraussetzungen
- Python Version 3.5 oder höher
- pygame
- sqlalchemy
- SQLAlchemy-Utils

# Verwendung
Um dieses Schachspielprojekt zu verwenden, müssen Sie die unten aufgeführten Schritte ausführen.

Zunächst müssen Sie eine Serverinstanz starten. Der Server ist dafür verantwortlich, das Schachbrett mit den verbundenen Clients zu synchronisieren. Sie können den Server mit dem folgenden Befehl starten:
```
python server.py
```
Sobald der Server läuft, müssen Sie zwei Clientinstanzen starten, die sich mit dem Server verbinden werden. Sie können die Clients mit dem folgenden Befehl starten:
```
python client.py
```
Nachdem Sie die Clients gestartet haben, werden sie sich mit dem Server verbinden und auf den Beitritt des anderen Clients warten. Sobald beide Clients beigetreten sind, beginnt das Spiel und sie können anfangen zu spielen.

# Funktionen
- Zwei Clients können über einen Server Schach spielen
- Highlighten von validen Zügen
- Alle Züge jeden Spiels werden in einer SQLite Datenbank gespeichert

# Erweiterungsmöglichkeiten
Aufgrund des zeitlichen Rahmens, habe ich mir dazu entschlossen folgende Funktionen nicht zu implementieren:
- Rochade
- En passant
- Feststellen des Spielendes

# Technische Details
Das Schachspielprojekt wurde mit Python und der Pygame-Bibliothek entwickelt. Der Server und die Clients kommunizieren über Socket-Verbindungen. Das Schachbrett und die Spielzüge werden als Python-Objekte mit Hilfe der Pickle-Bibliothek serialisiert.
