% Facts
fruit(apple, red).
fruit(apple, green).
fruit(banana, yellow).
fruit(cherry, red).
fruit(orange, orange).
fruit(grape, purple).
fruit(watermelon, green).
% Rule to find the color of a fruit
color(Fruit, Color) :-
    fruit(Fruit, Color).
