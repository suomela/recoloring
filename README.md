Distributed Recoloring
======================

Marthe Bonamy, Paul Ouvrard, Mikaël Rabie, Jukka Suomela, and Jara Uitto


Background
----------

Consider a 2-dimensional torus grid graph that is properly 4-colored.
In each step, we can change the color of one node such that the result
is again a proper 4-coloring.

Starting from a coloring x, can we reach a coloring y?


Tiles
-----

Classify the 2x2 tiles of properly 4-colored grids as follows:

*Type A* (2 tiles):

    1 3    2 3
    3 2    3 1

*Type B* (14 tiles):

    2 1    4 1
    1 4    1 2

    3 1    4 1
    1 4    1 3

    2 3    4 3
    3 4    3 2

    2 1    4 1
    3 4    3 2

    2 3    4 3
    1 4    1 2

    3 2    4 2
    1 4    1 3

    1 3    2 3
    4 2    4 1

*No type:* everything else.


Results
-------

*Lemma:* If you change the color of one node in the grid,
the total number of type-A tiles mod 2 changes by one if and only if
the total number of type-B tiles mod 2 changes by one.

_Proof:_ See the code in this repository.

*Corollary:* If colorings x and y do not contain any nodes of color 4,
and x and y have a different number of type-A tiles mod 2, then it is
not possible to reach coloring y from x.

_Proof:_ All type-B tiles contain one node of color 4.


Code
----

You can verify the lemma by running the Python script `check-tiles.py`.
It enumerates all 3x3 neighborhoods and all possible ways to change the
color of the middle node, and checks that the claim holds.

It also produces a human-readable output of all cases, available in
the text file `check-tiles.txt`.
