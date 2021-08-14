# Direct Product and Semi-Direct Product

Let $N, H$ be two groups. The Cartesian product of them (as *sets* without group structures) is:

$$
N \times H = \{(n,h) \mid n \in N, h \in H\}
$$

We can define various binary operations on this set, leading to different groups. 

## Direct Product

The simplest group structure we can think of leads to the **direct product group** $N \times H$. The group multiplication is a simple combination of those of $N, H$:

$$
(n,h)(n',h') = (nn', hh')
$$

- The identity element is $(1_N, 1_H)$.

- The inverse of $(n,h)$ is simply $(n^{-1}, h^{-1})$.

## Outer Semi-Direct Product

The **outer semi-direct product group** $N \rtimes_\phi H$ is a generalization of the direct product: the element $h$ is not directly multiplied onto $h'$. Introduce a group homomorphism $\phi$:

$$
\phi: H \to \Aut(N), \quad h \mapsto \phi_h
$$ 

The group multiplication of $N \rtimes_\phi H$ is defined as

$$
(n,h)(n',h') = (n \phi_h(n'), h h')
$$

- The identity element is still $(1, 1)$.

- The inverse of $(n,h)$ is $(\phi_{h^{-1}}(n^{-1}), h^{-1})$; let us verify:

    $$
    \begin{align*}
        &(n,h) (\phi_{h^{-1}}(n^{-1}), h^{-1})
        = (n (\phi_h \phi_{h^{-1}})(n^{-1}), hh^{-1})
        \\
        &= (n \phi_{hh^{-1}}(n^{-1}), hh^{-1})
        = (n 1 n^{-1}, 1_h) = (1, 1)
    \end{align*}
    $$

### Subgroups of $N \rtimes_\phi H$

The outer semi-direct group $G \equiv N \rtimes_\phi H$ has two important subgroups:

$$
\begin{align*}
    N' &\equiv \{(n,1) \mid n \in N\} \cong N
    \\
    H' &\equiv \{(1,h) \mid h \in H\} \cong H
\end{align*}
$$

<div class="result">

*Theorem*: The subgroups $N', H'$ have the following properties.

- $N' \lhd G$ ($N'$ is a *normal subgroup* of $G$).
- $G = N'H'$ (every element of $G$ is of the form $(n,1)(1,h)$ for some $n \in N, h \in H$)
- $N' \cap H' = \{(1,1)\}$ (the only common element of $N', H'$ is the identity).

</div>

----

*Proof*: 

- For any $(n',h') \in G, (n,1) \in N'$

    $$
    \begin{align*}
        & (n',h')^{-1} (n,1) (n',h')
        \\
        &= (\phi_{h'^{-1}}(n'^{-1}), h'^{-1})
        (n \phi_h(n'), h')
        \\
        &= (\cdots, 1) \in N'
    \end{align*}
    $$

- For any $(n,1) \in N', (1,h) \in H'$

    $$
    (n,1)(1,h) = (n \phi_1(1), h) = (n,h)
    $$

    This exhaust the entire Cartesian product set $N \times H$. 

- This property is obvious. $\blacksquare$

----

## Inner Semi-Direct Product

Motivated by the properties of the outer semi-direct product, supposed that: 

- $N, H$ are both *subgroups* of a larger group $G$ (hence the name *inner*);
- $N \lhd G$
- $G = NH$
- $N \cap H = \{1_G\}$

In this case $G$ is said to be the **inner semi-direct product** of $N, H$ (denoted by $N \rtimes H$). 

<div class="result">

*Theorem*: The inner semi-direct product $G$ is *isomorphic* to the outer semi-direct product $G' \equiv N \rtimes_\phi H$.

</div>

----

*Proof*: Consider the product of two elements in $G, G'$ respectively.

- For any $(n,h), (n',h') \in G'$

    $$
    (n,h)(n',h') = (n \phi_h(n'), h h')
    $$

- For any $nh, n'h' \in G$, we try to express their product in the form $n'' h''$. Note that $N \lhd G$, thus 

    $$
    \begin{aligned}
        nhn'h' &= n \underbrace{(h n' h^{-1})}_{\in N} h h' \\
        &= n'' h''
    \end{aligned} \quad \text{with} \quad \left\{ \begin{aligned}
        n'' &= n h n' h^{-1} \\
        h'' &= h h'
    \end{aligned} \right.
    $$

Thus we can choose the isomorphism between $G, G'$ as

$$
(n,h) \mapsto nh
$$

The homomorphism $\phi$ can then be determined as

$$
\phi_h(n') = h n' h^{-1} 
\quad \blacksquare
$$

----

