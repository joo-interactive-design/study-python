## Scope

#### Local Scope

```python
def drink_potion():
  potion_strength = 2
  print(potion_strength)
```
the result of the code above is 2

```python
drink_potion():
print(potion_strength)
```
the result of the code above is error:name 'potion_strength' is not defined

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
