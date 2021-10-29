# GameOfLifeAndWar
Version modifié du Game of Life à 2 populations (Rouge et Bleue)<br/>
Click droit : Poser une entité bleue<br/>
Click gauche : Poser une entité rouge<br/>
Click molette : Enlever une entité<br/>
Après avoir placer les entités lancer la simulation en appuyant sur "Go!"<br/>
La simulation peut être mise en pause à tout moment en appuyant sur "Stop"<br/>
Des entités peuvent être ajoutées ou enlevées à tout moment, en cours de simulation ou en pause.<br/>
Si une case vide est contestée entre les 2 populations, celle qui a le plus d'entité de sa population autour de la case en prend le contrôle si il y a égalité ni l'une ni l'autre n'en prend le contrôle et la case reste vide<br/>
Une case controlée peut être conquise par la population adverse si celle si est plus nombreuse, par exemple, si 1 entité rouge est au contact de 3 entités bleues, elle sera transformée en entité bleue.<br/>
La surpopulation s'applique respectivement à chaque population, par exemple, si 1 entité bleue est au contact de 2 entités rouges et de 3 entités bleues, elle ne disparaitra pas car seules les entités bleues influe sur la surpopulation et elle ne sera pas conquise car il y a moins d'entités rouges que bleues.
