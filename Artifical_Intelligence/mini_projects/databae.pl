start :-
    questions.

ch:-
check(Career),
write('A career recommendation for you is'),write(Career).
ch :- write('sorry, could not find a career for you :(').

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
    read(B),assertz(professional(B)),

    write('Do you think you are outgoing?'),
    read(C),assertz(outgoing(C)),

    write('Do you think you are Data centric?'),
    read(D),assertz(datacentric(D)),

    write('Do you think you are Detail Oriented?'),
    read(E),assertz(detailoriented(E)),

    write('Do you think you are Detail Oriented?'),
    read(F),assertz(athletic(F)),
    write('Do you think you are thinker?'),
    read(G),assertz(thinker(G)),
    /* write(DO YOU LIKE INTERACTIONS?) */
write('Do you think you are an extrovert?'),
read(H),assertz(extrovert(H)),

write('Do you think you are an introvert?'),
read(I),assertz(introvert(I)).

/* write(WHAT DO YOU THINK YOUR CHOICE IS AFFECTED BY?)
attribute(financialissues) :- is_true('Do you think you are going for this due to financial issues?').
attribute(peerpressure) :- is_true('Do you think you are going for this due to peer pressure?').
attribute(interest) :- is_true('Do you think you are going for this out of interest?').*/

check(medicine) :-
(subject(biology);
subject(science)),
(marks(morethan90);
marks(between75to90)),
professional(yes),
outgoing(yes),
extrovert(yes),
introvert(yes),write('medicine').

check(engineering) :-
(subject(mahematics);
subject(science)),
(marks(morethan90);
marks(between75to90)),
datacentric(yes),
detailoriented(yes),
extrovert(yes),
introvert(yes),write('engineering').

check(writer) :-
subject(literature),
(marks(between50to75);
marks(morethan90);
marks(between75to90)),
professional(yes),
outgoing(yes),
thinker(yes),
introvert(yes),write('writer').
check(artist) :-
subject(art),
(marks(lessthan50);
marks(between50to75)),
creative(yes),
thinker(yes),
extrovert(yes),
introvert(yes),write('artist').

check(sportsperson) :-
subject(pt),
(marks(lessthan50);
marks(between50to75)),
athletic(yes),
outgoing(yes),
extrovert(yes),
introvert(yes),write('sportsperson').


is_true(Q) :-
format("~w?\n", [Q]),
read(yes).
