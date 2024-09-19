% Define the initial state
% state(MonkeyHorizontal, MonkeyVertical, BoxPosition, HasBanana)
initial_state(state(atdoor, onfloor, atwindow, hasnot)).

% Define the goal state
goal_state(state(_, _, _, has)).

% Define the possible moves
move(state(middle, onbox, middle, hasnot), grasp, state(middle, onbox, middle, has)).
move(state(P, onfloor, P, H), climb, state(P, onbox, P, H)).
move(state(P1, onfloor, P1, H), drag(P1, P2), state(P2, onfloor, P2, H)).
move(state(P1, onfloor, B, H), walk(P1, P2), state(P2, onfloor, B, H)).

% Define the rule to check if the monkey can get the banana
canget(state(_, _, _, has)).
canget(State1) :-
    move(State1, _, State2),
    canget(State2).

% Query to solve the problem
solve :-
    initial_state(State),
    canget(State).
