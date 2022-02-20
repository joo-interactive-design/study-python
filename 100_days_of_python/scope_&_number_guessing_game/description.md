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


