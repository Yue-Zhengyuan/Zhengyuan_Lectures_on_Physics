# Conjugation and Norm of Grassmann Tensors

## Grassmann Conjugation

*Program implementation*: `GTensor.gconj`

The **Grassmann conjugation** of a Grassmann tensor $\mathbf{T}$

$$
\mathbf{T}(\theta)_{i_1 ... i_r}^{n_1 ... n_r} 
= T_{i_1 ... i_r}^{n_1 ... n_r} 
\theta_1^{n_1} ... \theta_r^{n_r}
$$

is defined to be 

$$
[\mathbf{T}^\dagger(\theta)]_{i_1 ... i_r}^{n_1 ... n_r} 
= (T^\dagger)_{i_1 ... i_r}^{n_1 ... n_r} 
\theta_1^{n_1} ... \theta_r^{n_r}
$$

The dagger on the ordinary part $T$ is the usual Hermitian conjugation:

$$
(T^\dagger)_{i_1 ... i_r}^{n_1 ... n_r} 
\equiv (T^*)_{i_r ... i_1}^{n_r ... n_1}
$$

We note that the axis order of $\mathbf{T}^\dagger$ is *reversed* compared to $\mathbf{T}$. But sometimes we may want to preserve the axis order; this can be done by a further transposition step:

```python
# the following has the same axis order as T itself
T.gconj().T
# or simply
T.gT
```

We shall use $\mathbf{T}^\Dagger$ to denote the combination of these two operations:

$$
\begin{align*}
    [\mathbf{T}^\Dagger(\theta)]_{i_1 ... i_r}^{n_1 ... n_r} 
    &\equiv [(\mathbf{T}^{\dagger \mathsf{T}}(\theta)]
    _{i_1 ... i_r}^{n_1 ... n_r} 
    \\
    &= (-1)^{P(p|n)} (T^\dagger)_{i_r ... i_1}^{n_r ... n_1}
    \theta_1^{n_1} ... \theta_r^{n_r}
    \\
    &= (-1)^{P(p|n)} (T^*)_{i_1 ... i_r}^{n_1 ... n_r}
    \theta_1^{n_1} ... \theta_r^{n_r}
\end{align*}
$$

where $p$ is the permutation that reverses the axis order, and $P(p|n)$ is the parity of $p$ restricted to nonzero Grassmann indices in $\{n\}$. We shall mainly work with $\mathbf{T}^\Dagger$ below. 

<div class="remark">

*Remark*: 

- We should emphasize that $\theta$'s appearing in $\mathbf{T}^\dagger$ have no connection with the $\theta$'s in $\mathbf{T}$, since the Grassmann numbers are only some labels helping us keep track of the minus signs. 

- We also define **ordinary complex conjugation** of the Grassmann tensor $\mathbf{T}$ as:

    $$
    \mathbf{T}^*(\theta)_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r} 
    = 
    (T^*)_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r}
    \theta_1^{n_1} \theta_2^{n_2} ... \theta_r^{n_r}
    $$

    which is different from $\mathbf{T}^\Dagger$, and seldom used. It is implemented as `GTensor.conj`.

</div><br>

Graphically, $\mathbf{T}, \mathbf{T}^\dagger$ and $\mathbf{T}^\Dagger$ are represented by
    
```
    0   1   2   3       3   2   1   0
    |___|___|___|  -->  |___|___|___|
          T               T.gconj()

                        0   1   2   3
                   -->  |___|___|___|
                            T.gT
```

### Effect on Contraction

A natural question to ask is how to obtain $(\mathbf{A} \mathbf{B})^\Dagger$ from $\mathbf{A}^\Dagger$ and $\mathbf{B}^\Dagger$. We start from the simplest case where we have only one pair of axes (say the $a$th of $\mathbf{A}$ and the $b$th of $\mathbf{B}$) to be contracted. Let $\mathbf{C} = \mathbf{AB}$; then

$$
\begin{align*}
    &[\mathbf{C}(\theta,\eta)]_{i_1 ... \cancel{i_a} ... i_r, j_1 ... \cancel{j_b} ... j_s}^{m_1 ... \cancel{m_a} ... m_r, n_1 ... \cancel{n_b} ... n_s} 
    \\[0.5em]
    &= \sum_{m_a,n_b} \sum_{i_a,j_b} (-1)^{P(a,b; \{m, n\})} g_{ab}^{m_a}
    \delta_{m_a n_b} \delta_{i_a j_b}
    \\[1.2em] &\quad \times
    A_{i_1 ... i_r}^{m_1 ... m_r} 
    B_{j_1 ... j_s}^{n_1 ... n_s} 
    \theta_1^{m_1} ... \cancel{\theta_a^{m_a}} ...\theta_r^{m_r} 
    \eta_1^{n_1} ... \cancel{\eta_b^{n_b}} ...\eta_s^{n_s}
\end{align*}
$$

The tensor elements are

$$
\begin{align*}
    &C_{i_1 ... \cancel{i_a} ... i_r, j_1 ... \cancel{j_b} ... j_s}^{m_1 ... \cancel{m_a} ... m_r, n_1 ... \cancel{n_b} ... n_s} 
    \\
    &= \sum_{m_a,n_b} \sum_{i_a,j_b} (-1)^{P(a,b; \{m, n\})} g_{ab}^{m_a}
    \delta_{m_a n_b} \delta_{i_a j_b}
    A_{i_1 ... i_r}^{m_1 ... m_r} 
    B_{j_1 ... j_s}^{n_1 ... n_s} 
\end{align*}
$$

By definition of Grassmann conjugation:

### Effect on Trace

To summarize:

<div class="result">

- Grassmann conjugation reverses all metrics in the Grassmann tensor network.
- On the free ends, ???

</div><br>

## Norm

*Program implementation*: `gtensor.norm` 

As usual, the **(2-)norm** of a Grassmann tensor is defined by

$$
(\text{norm }\mathbf{T})^2
= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r} 
|T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r}|^2
$$

This can be calculated by contracting the pairs of axes $(r,1), (r-1,2), ..., (1,r)$ in $\mathbf{T}^\dagger, \mathbf{T}$ with all Grassmann metrics all set to $+1$; recall that such a set of contraction pairs does not involve reordering of Grassmann variables:

$$
\begin{align*}
    (\text{norm } \mathbf{T})^2
    &= [\mathbf{T}^\dagger(\bar{\theta}) \mathbf{T}(\theta)]
    \\
    &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
    g_{r,1}^{n_1} g_{r-1,2}^{n_2} \cdots g_{1,r}^{n_r}
    (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
    T_{i_1 ... i_r}^{n_1 ... n_r} 
    \\
    &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
    (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
    T_{i_1 ... i_r}^{n_1 ... n_r} 
    \quad \text{(setting all $g$ to 1)}
    \\ & =
    \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r} 
    |T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r}|^2
\end{align*}
$$

Graphically, we flip $\mathbf{T}^\dagger$ horizontally, and connect the axes of $\mathbf{T}^\dagger$ and $\mathbf{T}$ in reversed order with $g = +1$:

```
    3   2   1   0            T†
    |___|___|___|       |‾‾‾|‾‾‾|‾‾‾|
          T†            3   2   1   0
                  -->   ↓   ↓   ↓   ↓
    0   1   2   3       0   1   2   3
    |___|___|___|       |___|___|___|
          T                   T
```

This is done by the following code:

```python
axes = tuple(range(a.ndim))
nrmsqr = gt.tensordot(a.gconj(), a, [axes[::-1], axes]).value()
# or equivalently
nrmsqr = gt.tensordot(a.gT, a, [axes, axes]).value()
```

<div class="remark">

*Remark*: 

- `flip_gSign` does *not* affect the norm of a Grassmann tensor, since it only changes the sign of some tensor elements, and hence does not change its absolute value.

- If $\mathbf{T}$ is of *even-parity*, it does not matter if we set *all* $g$ to $1$ or $-1$. Because the summand

    $$
    \begin{align*}
        &g_{r,1}^{n_1} g_{r-1,2}^{n_2} \cdots g_{1,r}^{n_r}
        (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
        T_{i_1 ... i_r}^{n_1 ... n_r} 
        \\ &\qquad
        \to
        (\pm 1)^{n_1 + \cdots + n_r}
        (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
        T_{i_1 ... i_r}^{n_1 ... n_r} 
    \end{align*}
    $$

    is nonzero only when

    $$
    n_1 + \cdots + n_r = P(T) \pmod{2}
    $$

    For the same reason, if $\mathbf{T}$ is of *odd-parity*, setting all $g$ to $-1$ will only produce an additional negative sign. 

- We can exchange of $\mathbf{T}, \mathbf{T}^\dagger$ in the calculation (the pairs of axes are certainly unchanged, thus we still need not to permute the Grassmann variables) :
    
    $$
    \begin{align*}
        &(\text{norm } \mathbf{T})^2
        = [\mathbf{T}(\theta) \mathbf{T}^\dagger(\bar{\theta})]
        \\
        &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
        g_{r,1}^{n_1} g_{r-1,2}^{n_2} \cdots g_{1,r}^{n_r}
        T_{i_r ... i_1}^{n_r ... n_1} 
        (T^\dagger)_{i_1 ... i_r}^{n_1 ... n_r} 
        \\
        &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
        T_{i_r ... i_1}^{n_r ... n_1} 
        (T^\dagger)_{i_1 ... i_r}^{n_1 ... n_r} 
        \quad \text{(setting all $g$ to 1)}
        \\ & =
        \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r} 
        |T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r}|^2
        \quad \qquad \text{(rename variables)}
    \end{align*}
    $$

</div><br>