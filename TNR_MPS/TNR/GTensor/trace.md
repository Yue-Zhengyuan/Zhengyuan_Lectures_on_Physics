# Trace of Grassmann Tensors

*Program implementation: `gtensor.trace`*

The **trace** of a Grassmann tensor over the pairs of axes $(a,b), (c,d), ...$ is defined in similar way to the tensor contraction: 

$$
\begin{align*}
    &[\Tr \mathbf{A}(\theta)]_{i_1 ... \cancel{i_a} \cancel{i_b} \cancel{i_c} \cancel{i_d} ... i_r}^{n_1 ... \cancel{n_a} \cancel{n_b} \cancel{n_c} \cancel{n_d} ... n_r} 
    \\
    &\equiv \sum_{n_a,n_b} \sum_{n_c,n_d} \cdots \sum_{i_a,i_b} \sum_{i_c,i_d} \cdots
    (-1)^{P(a,c,...; b,d,...; \{n\})}
    \\ &\quad \times
    \int g_{...} \theta_a^{n_a} \theta_b^{n_b}
    \int g_{...} \theta_c^{n_c} \theta_d^{n_d} \cdots
    \delta_{i_a i_b} \delta_{i_c i_d} \cdots
    A_{i_1 ... i_r}^{n_1 ... n_r} 
    \\ &\quad \times
    \theta_1^{m_1} \cdots \cancel{\theta_a^{m_a}} \cancel{\theta_b^{m_b}} \cancel{\theta_c^{m_c}} \cancel{\theta_d^{m_d}} \cdots \theta_r^{m_r} 
    \\
    &= \sum_{n_a,n_b} \sum_{n_c,n_d} \cdots \sum_{i_a,i_b} \sum_{i_c,i_d} \cdots
    (-1)^{P(a,c,...; b,d,...; \{n\})}
    \\ &\quad \times
    g_{ab}^{n_a} g_{cd}^{n_c} \cdots
    \delta_{n_a n_b} \delta_{n_c n_d} \cdots
    \delta_{i_a i_b} \delta_{i_c i_d} \cdots
    A_{i_1 ... i_r}^{n_1 ... n_r} 
    \\ &\quad \times
    \theta_1^{n_1} \cdots \cancel{\theta_a^{n_a}} \cancel{\theta_b^{n_b}} \cancel{\theta_c^{n_c}} \cancel{\theta_d^{n_d}} \cdots \theta_r^{n_r} 
\end{align*}
$$

Notes about notation: 

- in indices such as $i_1 ... \cancel{i_a} \cancel{i_b} \cancel{i_c} \cancel{i_d} ... i_r$, we do *not* mean that the axes $a,b,c,d,...$ are consecutive; it just means that that these axes are *removed* in the result;
- $P(a,c,...; b,d,...; \{n\})$ is the parity of the *sub*-permutation derived from the permutation required to bring $\theta_a^{n_a} \theta_b^{n_b} \theta_c^{n_c} \theta_d^{n_d} \cdots$ to the front of the sequence $\theta_1^{n_1} \cdots \theta_r^{n_r}$.

<div class="remark">

*Program usage*: 

By default, `gtensor.trace` assumes that the Grassmann metric goes from `axis1` to `axis2`. Thus the order of each tracing pair matters; when the order of one pair changes, the corresponding Grassmann metric should change sign. For example:

```python
"""
    trace example

                |-→---→-|
                |       |
            |-→-|-→-|   |
            ↑___↑___↓___↓
            0   1   2   3

    0 dim   3   5   3   5
    1 dim   4   3   4   3
"""
a = gt.random(((3,5,3,5), (4,3,4,3)))
# the following two lines are equivalent
tr1 = gt.trace(a, (0,1), (2,3), (1,1))
tr2 = gt.trace(a, (0,3), (2,1), (1,-1))
```

</div><br>

## Parity of Trace

Since the indices are removed in pairs, it is not difficult to see that the trace of a Grassmann tensor has the *same* parity as the  original tensor. 

## Transpose to Simplify Trace

To remove the annoying parity $P$, we can first transpose $A$ so that the axes $a,b,c,d,...$ are *already* put in the front of the sequence of Grassmann numbers, i.e. (suppose there are $q$ pairs of axes to be traced out)

- Put $a,c,...$ to the position $1, 3, ..., 2q-1$ 
- Put $b,d,...$ to the position $2, 4, ..., 2q$

Using this transposed tensor, the formula is simplified to

$$
\begin{align*}
    &[\Tr \mathbf{A}(\theta)]_{i_{2q+1} ... i_r}^{n_{2q+1} ... n_r} 
    \\
    &= \sum_{n_1,n_2} \cdots \sum_{n_{2q-1},n_{2q}} 
    \sum_{i_1,i_2} \cdots \sum_{i_{2q-1},i_{2q}}
    g_{1 2}^{n_1} \cdots g_{2q-1,2q}^{n_{2q-1}}
    \\ &\quad \times
    \delta_{n_1 n_2} \cdots \delta_{n_{2q-1} n_{2q}}
    \delta_{i_1 i_2} \cdots \delta_{i_{2q-1} i_{2q}}
    A_{i_1 ... i_r}^{n_1 ... n_r} 
    \theta_{2q+1}^{n_{2q+1}} \cdots \theta_r^{n_r} 
    \\
    &= \sum_{n_2,n_4,...,n_{2q}} 
    \sum_{i_2,i_4,...,i_{2q}}
    g_{1 2}^{n_2} \cdots g_{2q-1,2q}^{n_{2q}}
    \\ &\quad \times
    A_{i_2 i_2 i_4 i_4 ... i_{2q} i_{2q} i_{2q+1} ... i_r}^{n_2 n_2 n_4 n_4 ... n_{2q} n_{2q} n_{2q+1} ... n_r} 
    \theta_{2q+1}^{n_{2q+1}} \cdots \theta_r^{n_r} 
\end{align*}
$$

### Merge Axes for Tracing

Another convenient choice of transposition is provided by (under the constraint $n_1 = n_{2q}, n_2 = n_{2q-1}, ..., n_q = n_{q+1}$)

$$
P(1,2,...,q; \quad 2q,2q-1,...,q+1;\quad \{n\}) = 1
$$

Thus we can also use the following transposition:

- Put $a,c,...$ to the position $1, 2, ..., q$ 
- Put $b,d,...$ to the position $2q, 2q-1, ..., q+1$

Now we are contracting over the pairs $(1,2q), (2,2q-1), ..., (q,q+1)$. Then

$$
\begin{align*}
    &[\Tr \mathbf{A}(\theta)]_{i_{2q+1} ... i_r}^{n_{2q+1} ... n_r} 
    \\
    &= \sum_{n_1,n_{2q}} \cdots \sum_{n_q,n_{q+1}} 
    \sum_{i_1,i_{2q}} \cdots \sum_{i_q,i_{q+1}}
    g_{1, 2q}^{n_1} \cdots g_{q,q+1}^{n_q}
    \\ &\quad \times
    \delta_{n_1 n_q} \cdots \delta_{n_q n_{q+1}}
    \delta_{i_1 i_q} \cdots \delta_{i_q i_{q+1}}
    A_{i_1 ... i_r}^{n_1 ... n_r} 
    \theta_{2q+1}^{n_{2q+1}} \cdots \theta_r^{n_r} 
    \\
    &= \sum_{n_1,n_2,...,n_q} \sum_{i_1,i_2,...,i_q}
    g_{1,2q}^{n_1} \cdots g_{q,q+1}^{n_q}
    \\ &\quad \times
    A_{(i_1 i_2 ... i_q) (i_q ... i_2 i_1) i_{2q+1} ... i_r}^{(n_1 n_2 ... n_q) (n_q ... n_2 n_1) n_{2q+1} ... n_r} 
    \theta_{2q+1}^{n_{2q+1}} \cdots \theta_r^{n_r} 
\end{align*}
$$

In the second way of calculating the trace, we can absorb the $g$'s into the tensor $A$:

$$
\tilde{A}_{(i_1 i_2 ... i_q) (i_q ... i_2 i_1) i_{2q+1} ... i_r}^{(n_1 n_2 ... n_q) (n_q ... n_2 n_1) n_{2q+1} ... n_r} 
\equiv
g_{1,2q}^{n_1} \cdots g_{q,q+1}^{n_q}
    A_{(i_1 i_2 ... i_q) (i_q ... i_2 i_1) i_{2q+1} ... i_r}^{(n_1 n_2 ... n_q) (n_q ... n_2 n_1) n_{2q+1} ... n_r} 
$$

and then merge axes for the tensor $\tilde{A}$ (the first group of axes ($1$ to $q$) is merged as usual, but the second group of axes ($q+1$ to $2q$) should be merged with *reversed order*, i.e. turning on the `order = -1` option in the program):

$$
\tilde{A}_{(i_1 i_2 ... i_q) (i_q ... i_2 i_1) i_{2q+1} ... i_r}^{(n_1 n_2 ... n_q) (n_q ... n_2 n_1) n_{2q+1} ... n_r} 
\xrightarrow{\text{merge axes}}
\tilde{A}_{I I, i_{2q+1} ... i_r}^{N N, n_{2q+1} n_r}
$$

then

$$
\begin{align*}
    &[\Tr \mathbf{A}(\theta)]_{i_{2q+1} ... i_r}^{n_{2q+1} ... n_r} 
    \\
    &= \sum_{N} \sum_{I}
    \tilde{A}_{I I, i_{2q+1} ... i_r}^{N N, n_{2q+1} ... n_r} 
    \theta_{2q+1}^{n_{2q+1}} \cdots \theta_r^{n_r} 
    \\
    &= \sum_{N} \left(\Tr_I 
    \tilde{A}_{I I, i_{2q+1} ... i_r}^{N N, n_{2q+1} ... n_r} \right)
    \theta_{2q+1}^{n_{2q+1}} \cdots \theta_r^{n_r} 
\end{align*}
$$

Here $\Tr_I$ means trace over the index $I$ only.