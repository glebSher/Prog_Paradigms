female(lubov).
female(galina).
female(vera).
female(anastasiya).
female(olga).
male(sergey).
male(vladimir).
male(alexey).
male(alexander).
male(serafim).
parent(vera, lubov).
parent(vera, sergey).
parent(alexey, galina).
parent(alexey, vladimir).
parent(anastasiya, vera).
parent(anastasiya, alexey).
parent(olga, vera).
parent(olga, alexey).
parent(serafim, anastasiya).
parent(serafim, alexander).

father(X,Y):- parent(X,Y), male(Y).
mother(X,Y):- parent(X,Y), female(Y).
grandfather(X,Z):- parent(X,Y), father(Y,Z).
grandmother(X,Z):- parent(X,Y), mother(Y,Z).

child(X,Y):- parent(Y,X).