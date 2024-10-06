distributive_law(A, B, C, Result1, Result2) :-
    Result1 is A * (B + C),
    Result2 is A * B + A * C.

expression1(2, 3, 4).
expression2(5, 6, 7).

derive_results :-
    expression1(A, B, C),
    distributive_law(A, B, C, Result1A, Result2A),
    expression2(X, Y, Z),
    distributive_law(X, Y, Z, Result1B, Result2B),
    write('Result of expression 1 using distributive law is : '), nl,
    write('A * (B + C) = '), write(Result1A), nl,
    write('A * B + A * C = '), write(Result2A), nl,
    write('Result of expression 2 using distributive law is : '), nl,
    write('X * (Y + Z) = '), write(Result1B), nl,
    write('X * Y + X * Z = '), write(Result2B), nl.
