# Classification of 2D Space Groups

<font size=5>

**Part 1: Background of Group Cohomology**

</font>

Recall that the wallpaper group $G$ contains a normal subgroup $T$ (the translation group), and $G/T \cong P$ (the point group), thus $G$ is an *extension* of $T$ by $P$:

$$
1 \to T \xrightarrow{\mu} G \xrightarrow{\pi} P \to 1
\quad (\im \mu = \ker \pi)
$$

However, in this case $T$ is *Abelian*, which provides further information. In addition to the exact sequence, we add two additional pieces of information described below.

## Action of $P$ on $T$

Now we describe how the point group elements acts on the lattice (translation group) $T$:

<div class="result">

**Action of $P$ on $T$**:

- Since $\pi$ is surjective, for each $g \in P$ we can choose $x_g \in G$ such that $\pi(x_g) = g$.
- The (left) action on $t \in T$ is chosen as the *conjugation* $g(t) = x_g t x_g^{-1}$.

</div>

----

*Verifying well-definition of the action*: 

There may be multiple elements in $G$ mapped to $g$ by $\pi$. Suppose that $\pi(x_g) = \pi(y_g) = g$; we need to ensure that they give the same action $g(t)$:

$$
x_g t x_g^{-1} \overset{?}{=} y_g t y_g^{-1}
\ \Leftrightarrow \ 
t \overset{?}{=} (x_g^{-1} y_g) t (x_g^{-1} y_g)^{-1}
$$

It turns out that $x_g^{-1} y_g \in T$: since $\pi$ is a homomorphism, we have

$$
\begin{gather*}
    \pi(x_g^{-1} y_g) = \pi(x_g)^{-1} \pi(y_g) = g^{-1} g = 1
    \\ \Downarrow \\
    x_g^{-1} y_g \in \ker \pi \cong T
\end{gather*}
$$

But in current discussion $T$ is already a subgroup of $G$, making the isomorphism an equality. Since $T$ is an Abelian group, we obtain

$$
(x_g^{-1} y_g) t (x_g^{-1} y_g)^{-1}
= t (x_g^{-1} y_g) (x_g^{-1} y_g)^{-1} = t
$$

Thus the action of $P$ on $T$ is well-defined. $\blacksquare$

----

*Verifying group action properties*: 

For any $g, h \in P$, we need to ensure that

$$
gh(t) = x_{gh} t x_{gh}^{-1} 
\overset{?}{=} x_g x_h t x_h^{-1} x_g^{-1}
= g(h(t))
$$

Since $\pi$ is a homomorphism, 

$$
\pi(x_g x_h) = \pi(x_g) \pi(x_h) = gh
$$

Thus we can directly choose $x_{gh} = x_g x_h$; although there may be other possibilities, we have proved earlier that they give the same group action. $\blacksquare$

----

## Introducing Group Cohomology

### 2-Cocycles

Although $x_g \mapsto g$ is achieved by the homomorphism $\pi$, the reverse $g \mapsto x_g$ is *not necessarily a homomorphism*. The failure of this mapping to be a homomorphism is measured by the **2-cocycle**, defined in this context as:

$$
c: P \times P \to T \quad c(g,h) = x_g x_h x_{gh}^{-1}
$$

<div class="remark">

*Remark*: 

- The requirement that $g \mapsto x_g$ is a homomorphism is equivalent to $c(g,h) = 1$ for any $g,h \in P$. 
- Unless necessary, we *choose* $x_1 = 1$. This implies $c(1,g) = c(g,1) = 1$. Under this choice, we say that the 2-cocycles are *normalized*.

</div><br>

The 2-cocycle is not arbitrarily defined: it should satisfy the following requirement

<div class="result">

**Defining property of 2-cocycles**:

$$
\forall g,h,k \in P :\quad c(g,h) c(gh,k) = g(c(h,k)) c(g,hk)
$$

</div>

----

*Proof*: For the current definition

$$
\begin{align*}
    \text{LHS} &= x_g x_h x_{gh}^{-1} x_{gh} x_k x_{ghk}^{-1}
    = x_g x_h x_k x_{ghk}^{-1}
    \\
    \text{RHS} &= x_g c(h,k) x_g^{-1} c(g,hk)\\
    &= x_g x_h x_k x_{hk}^{-1} x_g^{-1} x_g x_{hk} x_{ghk}^{-1} \\
    &= x_g x_h x_k x_{ghk}^{-1} = \text{LHS} 
    & \blacksquare
\end{align*}
$$

----

### 2-Coboundaries

The 2-cocycle $c(g,h)$ is *not uniquely determined* by $g,h$. Let us make new choices $y_g$ such that $\pi(y_g) = g$ (and similarly for other elements in $P$). Then the new 2-cocycle is

$$
c'(g,h) = y_g y_h y_{gh}^{-1}
$$

Let us try to relate it to the old 2-cocycle $c(g,h)$: we proved earlier that $x_g^{-1} y_g \in T$. Then we write $y_g = x_g t_g$ for some $t_g \in T$, and 

$$
\begin{align*}
    c'(g,h) &= x_g t_g x_h t_h (x_{gh} t_{gh})^{-1} \\
    &= x_g t_g x_h t_h t_{gh}^{-1} x_{gh}^{-1}
\end{align*}
$$

### The Second Cohomology Group

We can form 3 groups from all 2-cocycles and 2-coboundaries of $P, T$:

- The **second cocycle group** (Abelian)

    $$
    \begin{gather*}
        Z^2(P,T) = \{c(g,h) \mid g,h \in P\}
        \\
        c(g,h) c(g',h') \equiv c(gg', hh')
    \end{gather*}
    $$

- The **second coboundary group** 

    $$
    B^2(P,T) = \{b(g,h) \mid g,h \in P\} \le Z^2(P,T)
    $$

- The **second cohomology group**

    $$
    H^2(P,T) = Z^2(P,T) / B^2(P,T)
    $$