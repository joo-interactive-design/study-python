## Number Guessing Game

![Group 3](https://user-images.githubusercontent.com/86972559/154830386-49943933-0397-482f-8b7e-c30d181f4143.png)
Code is on file named code.py

## Scope

#### Local Scope

```python
def drink_potion():
  potion_strength = 2
  print(potion_strength)
```
the result of the code above is '2'.

```python
drink_potion():
print(potion_strength)
```
the result of the code above is 'error: name 'potion_strength' is not defined'.

<br>

#### Global Scope

```python
player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)
  
drink_potion()
print(player_health)
```
Indentation / nesting is important!

```python
game_level = 3
def create_enemy():
  enemy = ["skeleton", "zombie", "alien"]
  if game_level < 5:
    new_enemy = enemy[0]
print(new_enemy)
```
The code above is not working. Make sure that if a variable is created within a function, then it's only available within that function.

```python
game_level = 3
def create_enemy():
  enemy = ["skeleton", "zombie", "alien"]
  if game_level < 5:
    new_enemy = enemy[0]
   print(new_enemy)
```
The code above is working!

<br>

#### Modifying Global Scope

```python
enemies = 1
def increase_enemies():
  #take global variable into the function
  global enemies
  enemies += 1
  print(enemies)
```

<br>
 
#### Better way is use 'return' instead of modifying global scope

```python
enemies = 1
def increase_enemies():
  return enemies + 1

enemies = increase_enemies()
print(enemies)
```

<br>

#### Note
Inside a if/else/for/while code block is the same as outside it.




