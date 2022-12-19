# Efficient Comparison

You would like to write a function that takes integer numbers <code>x</code>, <code>y</code>, <code>L</code> and <code>R</code> as parameters, and returns <code>True</code> if <code>x<sup>y</sup></code> lies within the interval <code>(L, R]</code> and <code>False</code> otherwise. You're considering several different ways to write the conditional statement inside this function:

<ol>
<li><code>if L &lt; x ** y &lt;= R:</code></li>
<li><code>if x ** y &gt; L and x ** y &lt;= R:</code></li>
<li><code>if x ** y in range(L + 1, R + 1):</code></li>
</ol>

Which option would be the most efficient in terms of execution time?

## Question

- [ ] Options <code>1</code> and <code>2</code> are equally good (and better than option <code>3</code>).
- [ ] All of these options are equally good.
- [ ] Option <code>1</code> is the most optimal one.
- [ ] Option <code>3</code> is the most optimal one.
- [ ] Option <code>2</code> is the most optimal one.

## Answer

- [ ] Options <code>1</code> and <code>2</code> are equally good (and better than option <code>3</code>).
- [ ] All of these options are equally good.
- [x] Option <code>1</code> is the most optimal one.
- [ ] Option <code>3</code> is the most optimal one.
- [ ] Option <code>2</code> is the most optimal one.
