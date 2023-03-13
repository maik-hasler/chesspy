# Projektantrag

Im Rahmen des Schulprojektes habe ich mich dazu entschieden ein Schachspiel zu entwickeln. Das Spiel wird mithilfe der Pygame-Bibliothek in Python umgesetzt und soll eine Registrierungs- und Anmeldemöglichkeit für Spieler bieten. Um die Spielerinformationen, wie Siege, Niederlagen und Unentschieden, sowie jedes Schachspiel und deren Züge zu speichern, nutze ich eine SQLite Datenbank.

Für ein vereinfachtes Datenbank-Management werde ich voraussichtlich SQLAlchemy nutzen.

Der Spieler tritt gegen einen Bot an, dessen Schwierigkeit über die Tiefe gesteuert werden kann. Die Tiefe gibt an, wie viele Schritte der Bot bei seinem nächsten Zug berücksichtigt. Durch die Anpassung der Tiefe kann die Schwierigkeit des Spiels erhöht werden und somit die Herausforderung für den Spieler gesteigert werden.
