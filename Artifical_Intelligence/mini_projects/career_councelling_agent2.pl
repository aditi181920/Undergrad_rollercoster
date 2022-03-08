
read_interest:-
    assertz(suree(no)),
    write('Enter your interest'),nl,
    read(X),assertz(interest(X)).

read_choice:-
    write('Enter your choice'),nl,
    read(E),assertz(choice(E)).

read_perf:-
    write('how well you have performed till now in choice(good/moderate/bad)'),nl,
    read(Y),assertz(perf(Y)).

read_neg:-
    write('Is your career choice affected by peer pressure or social status'),nl,
    read(Z),assertz(neg(Z)).
read_sat:-
    write('Do you feel a sense of satisfaction when it comes to your career choice?'),nl,
    read(B),assertz(satisfction(B)).

read_fav:-
    write('what is your favourite subject'),nl,
    read(C),assertz(fav(C)).
read_pref:-
    write('What do you think you will love to do the most'),nl,
    write('1. Helping and protecting others.'),nl,
    write('2. Playing outdoor games.'),nl,
    write('3. Embracing nature.'),nl,
    write('4. Creativity.'),nl,
    write('5. Creativity and art.'),nl,
    write('6. Innovation and creation.'),nl,
    read(D), assertz(pref(D)).

gatherinfo:- read_interest,read_choice,read_perf,read_neg,read_sat,read_fav,read_pref.

career(X):-interest(X),write('yes').

func:-
    write('maybe you should think again and look into what you really want.Think for a while and then tell if you want to continue? '),
    read(A),assertz(suree(A)),retractall(suree(no)).


career(X):- \+ interest(X),neg(yes),suree(no),func.


career(X):- \+interest(X),neg(yes),suree(yes),choice(medical),pref(1), write('ok go ahead').
career(X):-  \+interest(X),neg(yes),suree(yes),choice(medical), \+pref(1) , write('no, this is a bad choice').
career(X):- \+interest(X),neg(yes),suree(yes),choice(sportsperson),pref(2), write('ok go ahead').
career(X):- \+interest(X),neg(yes),suree(yes),choice(sportsperson),\+pref(2), write('no, this is a bad choice').
career(X):- \+interest(X),neg(yes),suree(yes),choice(environmentalist),pref(3), write('ok go ahead').
career(X):- \+interest(X),neg(yes),suree(yes),choice(environmentalist),\+pref(3), write('no, this is a bad choice').
career(X):- \+interest(X),neg(yes),suree(yes),choice(writer),pref(4), write('ok go ahead').
career(X):- \+interest(X),neg(yes),suree(yes),choice(writer),\+pref(4), write('no, this is a bad choice').
career(X):- \+interest(X),neg(yes),suree(yes),choice(artist),pref(5), write('ok go ahead').
career(X):- \+interest(X),neg(yes),suree(yes),choice(artist),\+pref(5), write('no, this is a bad choice').
career(X):- \+interest(X),neg(yes),suree(yes),choice(fashiondesigner),pref(5), write('ok go ahead').
career(X):- \+interest(X),neg(yes),suree(yes),choice(fashiondesigner),\+pref(5), write('no, this is a bad choice').
career(X):- \+interest(X),neg(yes),suree(yes),choice(engineer),pref(6), write('ok go ahead').
career(X):- \+interest(X),neg(yes),suree(yes),choice(engineer),\+pref(6), write('no, this is a bad choice').


career(X):- \+ interest(X),\+neg(yes),perf(good),satisfction(yes), write('ok good go ahead').

career(X):- \+interest(X),\+neg(yes),perf(fine),satisfction(dontknow), write('how about you think of career choices related to what you enjoy doing, those may work for you more').



















