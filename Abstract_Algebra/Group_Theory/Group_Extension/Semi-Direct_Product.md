# Direct Product and Semi-Direct Product

Let $N, H$ be two groups. The Cartesian product of them (as *sets* without group structures) is:

$$
N \times H = \{(n,h) \mid n \in N, h \in H\}
$$

We can define various binary operations on this set, leading to different groups. 

## Direct Product Group

*Definition*:

- **Direct product group** $N \times H$:<br>
    the set $N \times H$ equipped with the following multiplication rule

    $$
    (n,h)(n',h') = (nn', hh')
    $$

    1. The identity element is $(1_N, 1_H)$.
    
    2. The inverse of $(n,h)$ is simply $(n^{-1}, h^{-1})$.

### Product of Subgroups

*Definition*: Suppose $N, H$ are both subgroups of $G$.

- **Product** of $N, H$: the following set

    $$
    NH \equiv \{nh \mid n \in N, h \in H\}
    $$

This set is related to the direct product group by the following theorem:

<div class="result">

*Theorem*: $NH \cong N \times H$ *if and only if* all of the following are true:

- $G = NH$
- $N \cap H = \{1_G\}$
- $N$ commute with every element in $H$ (this is a *stronger* requirement than $N \lhd G$)

</div>

----

*Proof*: We verify that required isomorphism is

$$
f: N \times H \to NH, \quad f(n,h) = nh
$$

- $f$ is a homomorphism, since

    $$
    \begin{align*}
        f(n,h) f(n',h')
        &= nh n'h' = nn' hh' 
        \\
        &= f(nn',hh') = f((n,h)(n',h'))
    \end{align*}
    $$

    <div class="remark">

    *Remark*: If only $N \lhd G$ is required, we cannot obtain the second step $nh n'h' = nn' hh'$.

    </div><br>

- $\ker f = \{(1_N,1_H)\}$; assume there exists $(n,h) \ne (1,1)$ in $\ker f$:

    $$
    f(n,h) = nh = 1 \Rightarrow h = n^{-1} \in N
    $$

    which contradicts the requirement $N \cap H = \{1_G\}$.

- $\im f = NH$, since for any $nh \in NH$ we have $nh = f(n,h)$. $\blacksquare$

----

## Outer Semi-Direct Product Group

*Definition*: Let $\phi$ be a group homomorphism

$$
\phi: H \to \Aut(N), \quad h \mapsto \phi_h
$$ 

- **Outer semi-direct product group** $N \rtimes_\phi H$:<br>
    the set $N \times H$ equipped with the following multiplication rule

    $$
    (n,h)(n',h') = (n \phi_h(n'), h h')
    $$

    1. The identity element is still $(1, 1)$.

    2. The inverse of $(n,h)$ is $(\phi_{h^{-1}}(n^{-1}), h^{-1})$; let us verify:

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

- $G = N'H'$
- $N' \cap H' = \{(1,1)\}$
- $N' \lhd G$

</div>

----

*Proof*: 

- For any $(n,1) \in N', (1,h) \in H'$

    $$
    (n,1)(1,h) = (n \phi_1(1), h) = (n,h)
    $$

    This exhaust the entire Cartesian product set $N \times H$. 

- This property is obvious. 

- For any $(n',h') \in G, (n,1) \in N'$

    $$
    \begin{align*}
        & (n',h')^{-1} (n,1) (n',h')
        \\
        &= (\phi_{h'^{-1}}(n'^{-1}), h'^{-1})
        (n \phi_h(n'), h')
        \\
        &= (\cdots, 1) \in N'
        & \blacksquare
    \end{align*}
    $$

----

## Inner Semi-Direct Product Group

*Definition*: Suppose $N, H$ are both subgroups of $G$ (hence the name *inner*).

- **Inner semi-direct product** $N \rtimes H$:<br>
    the group $G$ itself if all of the following are true:

    - $G = NH$
    - $N \cap H = \{1_G\}$
    - $N \lhd G$

<div class="result">

*Theorem*: The inner semi-direct product $G$ is *isomorphic* to the outer semi-direct product $G' \equiv N \rtimes_\phi H$ with $\phi$ as *conjugation* by elements in $H$.

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

This motivates the following choice of isomorphism between $G, G'$ as

$$
(n,h) \mapsto nh
$$

Then we want

$$
n'' = n h n' h^{-1} \overset{!}{=} n \phi_h(n')
$$

This determines the homomorphism $\phi$ as a conjugation operation:

$$
\phi_h(n) = h n h^{-1} 
\quad \blacksquare
$$

----
