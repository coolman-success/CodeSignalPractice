# Collections Truthness

What will be the value of `res` after the following snippet is executed:

```python
xs = [()]
res = [False]*2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True
```

## Question

- [ ] `[True, False]`
- [ ] `[False, True]`
- [ ] `[False, False]`
- [ ] `[True, True]`

## Answer

- [x] `[True, False]`
- [ ] `[False, True]`
- [ ] `[False, False]`
- [ ] `[True, True]`
