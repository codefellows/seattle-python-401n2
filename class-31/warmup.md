# Warm-Up Exercise

> Write a script to produce the following output

```text
* 
* * 
* * * 
* * * * 
* * * * * 
```

## Feature Tasks

Once required output complete refactor to as few lines as possible.

### Solution

```python
n = 5
print('\n'.join('* ' * i for i in range(1, n + 1))) 
```
