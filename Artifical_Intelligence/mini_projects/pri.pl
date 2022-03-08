start :-
questions,
check(Career),
write('A career recommendation for you is'),write(Career).
start :- write('sorry, could not find a career for you :(').

questions:-

/* write("WHAT WAS YOUR FAVOURITE SUBJECT IN SCHOOL?") */
write('Which subject do you like?'),
read(X),assertz(subject(X)),

/* write(WHAT IS YOUR PERFORMANCE IN THIS SUBJECT?) */
write('How is your performance in this subject?'),
read(Y), assertz(marks(Y)),
/* write(WHAT KIND OF PERSONALITY DO YOU HAVE?) */
write('Do you think you are creative?'),
read(A),assertz(creative(A)),

write('Do you think you are professional?'),[04:22, 09/06/2021] Priyal: start :-
questions,
check(Career),
write('A career recommendation for you is'),write(Career).
start :- write('sorry, could not find a career for you :(').

questions:-

/* write("WHAT WAS YOUR FAVOURITE SUBJECT IN SCHOOL?") */
write('Which subject do you like?'),
read(X),assertz(subject(X)),

/* write(WHAT IS YOUR PERFORMANCE IN THIS SUBJECT?) */
write('How is your performance in this subject?'),
read(Y), assertz(marks(Y)),
/* write(WHAT KIND OF PERSONALITY DO YOU HAVE?) */
write('Do you think you are creative?'),
read(A),assertz(creative(A)),

write('Do you think you are professional?'),
read(A),assertz(professional(A)),

write('Do you think you are outgoing?'),
read(A),assertz(outgoing(A)),

write('Do you think you are Data centric?'),
read(A),assertz(datacentric(A)),

write('Do you think you are Detail Oriented?'),
read(A),assertz(detailoriented(A)),

write('Do you think you are Detail Oriented?'),
read(A),assertz(athletic(A)),

write('Do you think you are thinker?'),
read(A),assertz(thinker(A)),
[04:22, 09/06/2021] Priyal: /* write(DO YOU LIKE INTERACTIONS?) */
write('Do you think you are an extrovert?'),
read(A),assertz(extrovert(A)),

write('Do you think you are an introvert?'),
read(A),assertz(introvert(A)).

check(medicine) :-
(subject(biology);
subject(science)),
(marks(morethan90);
marks(between75to90)),
professional(yes),
outgoing(yes),
extrovert(yes),
introvert(yes).

check(engineering) :-
(subject(mahematics);
subject(science)),
(marks(morethan90);
marks(between75to90)),
datacentric(yes),
detailoriented(yes),
extrovert(yes),
introvert(yes).

check(writer) :-
subject(literature),
(marks(between50to75);
marks(morethan90);
marks(between75to90)),
professional(yes),
outgoing(yes),
thinker(yes),
introvert(yes).
[04:22, 09/06/2021] Priyal: check(artist) :-
subject(art),
(marks(lessthan50);
marks(between50to75)),
creative(yes),
thinker(yes),
extrovert(yes),
introvert(yes).

check(sportsperson) :-
subject(pt),
(marks(lessthan50);
marks(between50to75)),
athletic(yes),
outgoing(yes),
extrovert(yes),
introvert(yes).

is_true(Q) :-
format("~w?\n", [Q]),
read(yes).









