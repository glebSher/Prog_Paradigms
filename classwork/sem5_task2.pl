% Rules
max_list([X], X).
max_list([H|T], Max) :-
    max_list(t, Max1),
    (H > Max1, Max is H; Max is Max1).

& Query
?- max_list([1,2,3,4], X)