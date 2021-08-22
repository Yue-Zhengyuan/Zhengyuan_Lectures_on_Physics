# Bosonization of Grassmann Tensor Network

## Conversion to Ordinary Tensor

*Program implementation: `gtensor.gt_to_np`*

When the normal index dimension is *independent* of the Grassmann index, we can convert the Grassmann tensor to an ordinary tensor (by analogy, we call this process as **bosonization**):

$$
\mathbf{A}_{j_1 ... j_r}^{n_1 ... n_r} 
\to A_{\alpha_1 ... \alpha_r}^{(b)}
$$

where the ordinary indices $\alpha_a \, (a = 0, ..., r)$ are defined as

$$
\alpha_a = 2j_a + n_a
$$

The resulting ordinary tensor will have **$Z_2$ symmetry**, i.e. the nonzero elements satisfy

$$
\sum_{a=0}^r \alpha_a = \sum_{a=0}^r n_a = P(\mathbf{A}) \pmod{2}
$$

We can also perform the inverse operation (*implemented in `gtensor.np_to_gt`*) to formally convert an ordinary tensor with $Z_2$ symmetry to a Grassmann tensor. 

## PBC/Anti-PBC of Transfer Matrices

### Simplest Case: 1 $\times$ 1 Transfer Matrix

We start with the simplest case: consider a rank-4 Grassmann tensor of *even* parity

$$
\mathbf{A}_{j_0 ... j_3}^{n_0 ... n_3} 
\leftrightarrow A_{\alpha_0 ... \alpha_3}^{(b)}
$$

Imagine a square lattice tensor network consisting $\mathbf{A}$ only. The Grassmann metric and the axis order is chosen as below:

```
        1
        ↓
    2 → A → 0
        ↓
        3
```

The $1 \times 1$ (say) horizontal transfer matrix can be constructed by tracing:

```
        1               :
        ↓               ↓
    2 → A → 0  -->  1 → A → 0
        ↓               ↓
        3               :
```
```python
# e.g. transfer in horizontal direction
tm_pbc  = gt.trace(a,3,1,1)`   # PBC
tm_apbc = gt.trace(a,3,1,-1)`   # Anti-PBC
```

$$
\begin{align*}
    \mathbf{T}(\theta)_{j_0 j_2}^{n_0 n_2}
    &= [\Tr \mathbf{A}(\theta)]_{j_0 j_2}^{n_0 n_2}
    \\
    &= \sum_{n_1,n_3} \sum_{j_1,j_3}
    (-1)^{P(1; 3; \{n\})} g_{13}^{n_1} 
    \delta_{n_1 n_3} \delta_{j_1 j_3}
    A_{j_0 ... j_3}^{n_0 ... n_3} 
    \theta_0^{n_0} \theta_2^{n_2}
    \\
    &= \sum_{n,j} (-1)^{P(1;3;\{n_0,n,n_2,n\})} g_{13}^n
    A_{j_0 j j_2 j}^{n_0 n n_2 n} 
    \theta_0^{n_0} \theta_2^{n_2}
\end{align*}
$$

The Grassmann metric $g_{13}$ is

$$
g_{13} = \begin{cases}
    -1, & \text{PBC} \\
    +1, & \text{Anti-PBC}
\end{cases}
$$

The number $P(1; 3; \{n\})$ is the parity of the *sub*-permutation derived from the permutation 

$$
p: \theta_0^{n_0} \theta_1^{n_1} \theta_2^{n_2} \theta_3^{n_3}
\to 
\theta_1^{n_1} \theta_3^{n_3} \theta_0^{n_0} \theta_2^{n_2} 
$$

We ask what is the relation between them and the bosonized trace

```python
# bosonize the tensor
anp = gt.gt_to_np(a)
tm_np = np.trace(anp, 0, 1, 3)
```

$$
\begin{align*}
    T_{\alpha_0 \alpha_2}^{(b)} 
    &= \sum_{\alpha_1 \alpha_3} \delta_{\alpha_1 \alpha_3} A_{\alpha_0 ... \alpha_3}^{(b)}
    = \sum_{i} A_{\alpha_0 i \alpha_2 i}^{(b)}
    \\
    &\to 
    \sum_{n,j} A_{j_0 j j_2 j}^{n_0 n n_2 n}
    = T_{j_0 j_2}^{n_0 n_2}
\end{align*}
$$

Let us list the factor $(-1)^{P(1;3;\{n_0,n,n_2,n\})} g_{13}^n$ of all terms ($n = n_1 = n_3$) in the following table:

<center>

| $(n_0,...,n_3)$ |  $n$  | $(n_0,n_2)$ |  PBC  | APBC  |
| :-------------: | :---: | :---------: | :---: | :---: |
| `(0, 0, 0, 0)`  |  `0`  |  `(0, 0)`   |   1   |   1   |
| `(0, 1, 0, 1)`  |  `1`  |  `(0, 0)`   |  -1   |   1   |
| `(1, 0, 1, 0)`  |  `0`  |  `(1, 1)`   |   1   |   1   |
| `(1, 1, 1, 1)`  |  `1`  |  `(1, 1)`   |   1   |  -1   |

</center>

We notice that in the `(0,0)` block, the factor happens to be 1 when anti-PBC is used; in the `(1,1)` block, the factor is 1 when PBC is used. 

Therefore, **the 1 $\times$ 1 bosonized transfer matrix contains the `a0` and `p1` sectors of the Grassmann transfer matrix**. 

### 1 $\times$ 2 Transfer Matrix

We contract the 1 $\times$ 2 transfer matrix according to the following order:

```
        :
        1   
        ↓
    2 → A → 0
        ↓
        3
        :
        5
        ↓
    6 → A → 4
        ↓
        7
        :
```

$$
\begin{align*}
    &\mathbf{T}(\theta)_{j_0 j_2 j_4 j_6}^{n_0 n_2 n_4 n_6}
    \\
    &= \sum_{n,j} (-1)^{P(1,3; \, 7,5; \{n\})} 
    g_{3,5}^{n_3} g_{1,7}^{n_1}
    \\ & \qquad
    \delta_{n_1 n_7} \delta_{j_1 j_7}
    \delta_{n_3 n_5} \delta_{j_3 j_5}
    A_{j_0 j_1 j_2 j_3}^{n_0 n_1 n_2 n_3}
    A_{j_4 j_5 j_6 j_7}^{n_4 n_5 n_6 n_7}
    \theta_0^{n_0} \theta_2^{n_2} \theta_4^{n_4} \theta_6^{n_6} 
\end{align*}
$$

The Grassmann metrics are

$$
\begin{align*}
    g_{3,5} &= 1
    \\
    g_{1,7} &= \begin{cases}
        -1, & \text{PBC} \\
        +1, & \text{Anti-PBC}
    \end{cases} 
\end{align*}
$$

After the transposition $(0,2,4,6) \to (2,6,0,4)$ (the permutation $p = (1,3,0,2)$), each term in the sum acquires an additional factor of 

$$
(-1)^{P(p,\{n_0, n_2, n_4, n_6\})}
$$