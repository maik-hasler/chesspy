# chesspy

# Inhaltsverzeichnis
- [Installation](#installation)
- [Verwendung](#verwendung)

# Installation
Installieren Sie die benötigten Abhängigkeiten.
```
pip install -r requirements.txt
```

# Verwendung
Zuerst muss eine Server-Instanz gestartet werden. Der Server ist dafür zuständig, dass Schachbrett mit den verbundenen Clients zu synchronisieren.
```
python server.py
```
Nachdem der Server gestartet ist, müssen **zwei** Client-Instanzen gestartet werden, die sich dann mit den Server verbinden.
```
python client.py
```
