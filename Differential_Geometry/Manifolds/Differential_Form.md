# Differential Forms

*Definition*:

- **Differential form of degree $r$ ($r$-form)**: a *totally anti-symmetric* tensor $\omega$ of type $(0,r)$ (sending $r$ vectors to a number)

    The **degree** $r$ is denoted by $\deg{\omega} = r$. 

    The **set of all $r$-forms** defined in $T_p^* M$ is denoted by $\Omega^r_p(M)$. Sometimes the point $p$ will not be specified. 

    *Meaning of total anti-symmetry*:

    If we swap any two vectors that the $r$-form acts on, the result will *change sign*. In other words, for any $r$-form $\omega$, any $r$-permutation $P$ and any $r$ vectors $V_i \in T_p M$:

    $$
    \omega(V_{P(1)}, ..., V_{P(r)})
    = \text{sgn}(P) \, \omega(V_1, ..., V_r)
    $$

    In local coordinates, this requirement can be translated as

    $$
    \begin{align*}
        \omega_{\mu_1 ... \mu_r} 
        V_{P(1)}^{\mu_1} \cdots V_{P(r)}^{\mu_r}
        &= \text{sgn}(P) \,
        \omega_{\mu_1 ... \mu_r} 
        V_{1}^{\mu_1} \cdots V_{r}^{\mu_r}
        \\ 
        &= \text{sgn}(P) \,
        \omega_{\mu_{P(1)} ... \mu_{P(r)}} 
        V_{P(1)}^{\mu_{P(1)}} \cdots V_{P(r)}^{\mu_{P(r)}}
        \\
        \Rightarrow
        \omega_{\mu_1 ... \mu_r} 
        &= \text{sgn}(P) \,
        \omega_{\mu_{P(1)} ... \mu_{P(r)}} 
    \end{align*}
    $$

    or equivalently (since $\text{sgn}(P) = \pm 1$)

    $$
    \omega_{\mu_{P(1)} ... \mu_{P(r)}} 
    = \text{sgn}(P) \, \omega_{\mu_1 ... \mu_r}
    $$

    *Special cases*: 
    
    The concept of "anti-symmetric" does not apply to **0-forms** and **1-forms**, which are defined as

    - **0-Form**: formally *defined* as **functions** in $\mathcal{F}(M)$

    $$ \omega^{(0)} = f \in \mathcal{F}(M) $$

    - **1-Form**: general expression in local coordinates
        
        $$
        \omega^{(1)} = \omega_\mu dx^\mu
        $$

        including the dual basis $dx^\mu$ of $T_p^* M$. 

- **Wedge (exterior) product of differential forms**: 
    
    Let $\omega \in \Omega^r_p(M), \xi \in \Omega^s_p(M)$. The **wedge (exterior) product** $\omega \wedge \xi$ is defined as an $(r+s)$-form:
    
    $$
    \omega \wedge \xi \in \Omega^{r+s}_p(M)
    $$
    
    which acts on $r+s$ vectors $V_i \in T_p M$ as

    $$
    \begin{align*}
        &(\omega \wedge \xi)(V_1, ..., V_{r+s})
        \\ & \quad =
        \frac{1}{q! r!}\sum_{P \in S_{q+r}} \text{sgn}(P) \,
        \omega(V_{P(1)}, ..., V_{P(r)})
        \xi(V_{P(r+1)}, ..., V_{P(r+s)})
    \end{align*}
    $$

    where $S_r$ denotes the **symmetric group** of all $r$-permutations.

## Properties of Wedge Product

Let $\omega, \xi, \eta$ be differential forms defined in $M$, and 

$$
\dim{M} = m, \quad \deg{\omega} = q, \quad
\deg{\xi} = r, \quad \deg{\eta} = s
$$ 

Then

- **Graded anti-commutativity**
    
    $$ \omega \wedge \xi = (-1)^{qr} \xi \wedge \omega $$

    *Proof*:
    
    *Corollary*: 

    - For two 1-forms $\omega, \xi$

        $$ \omega \wedge \xi = - \xi \wedge \omega $$
    
    - If $q$ is odd, then 

        $$ 
        \omega \wedge \omega = (-1)^{q^2} \omega \wedge \omega = -\omega \wedge \omega = 0
        $$

- **Associativity**
  
    $$ (\omega \wedge \xi) \wedge \eta = \omega \wedge (\xi \wedge \eta) $$

## Wedge Product of Dual Basis Vectors

We start from 2 dual basis vectors. In local coordinates, let

$$
\omega = dx^{\mu_1}, \quad \xi = dx^{\mu_2}
$$

then

$$
\begin{align*}
    (\omega \wedge \xi)(V_1, V_2)
    &= \sum_{P \in S_2} \text{sgn}(P) \,
    \omega(V_{P(1)}) \, \xi(V_{P(2)})
    \\
    &= \sum_{P \in S_2} \text{sgn}(P) \,
    V_{P(1)}^{\mu_1} V_{P(2)}^{\mu_2}
    \\
    &= \sum_{P \in S_2} \text{sgn}(P) \,
    V_{1}^{\mu_{P(1)}} V_{2}^{\mu_{P(2)}}
\end{align*}
$$

In the last step we are in fact summing over $P^{-1}$. But $\text{sgn}(P) = \text{sgn}(P^{-1})$, so we need not change the notation. Therefore

$$
dx^{\mu_1} \wedge dx^{\mu_2} 
= \sum_{P\in S_2} \text{sgn}(P) \, dx^{\mu_{P(1)}} dx^{\mu_{P(2)}}
$$

Next we proceed to the product of 3 dual basis vectors (associativity of wedge product makes things easier): let $\eta = dx^{\mu_3}$, then

$$
\begin{align*}
    &\omega \wedge \xi \wedge \eta \, (V_1, V_2, V_3)
    \\
    &= (\omega \wedge \xi) \wedge \eta \, (V_1, V_2, V_3)
    \\ 
    &= \frac{1}{2! 1!}\sum_{P \in S_{3}} \text{sgn}(P) \,
    (\omega \wedge \xi)(V_{P(1)}, V_{P(2)}) \,
    \eta(V_{P(3)})
    \\ 
    &= \frac{1}{2} \sum_{P \in S_3} \text{sgn}(P) 
    \left( 
        V_{P(1)}^{\mu_1} V_{P(2)}^{\mu_2} V_{P(3)}^{\mu_3}
        - V_{P(1)}^{\mu_2} V_{P(2)}^{\mu_1} V_{P(3)}^{\mu_3}
    \right)
    \\ 
    &= \frac{1}{2} \sum_{P \in S_3} \text{sgn}(P) 
    \left( 
        V_{P(1)}^{\mu_1} V_{P(2)}^{\mu_2} V_{P(3)}^{\mu_3}
        - V_{P'(2)}^{\mu_2} V_{P'(1)}^{\mu_1} V_{P'(3)}^{\mu_3}
    \right)
\end{align*}
$$

Here $P' = (12) P \in S_3$ (i.e. $P$ combined with exchange of 1 and 2). Obviously $\text{sgn}(P) = -\text{sgn}(P')$. Therefore we can merge the two terms and cancel the $1/2$ factor:

$$
\begin{align*}
    \omega \wedge \xi \wedge \eta
    &= \sum_{P \in S_3} \text{sgn}(P) \,
    V_{P(1)}^{\mu_1} V_{P(2)}^{\mu_2} V_{P(3)}^{\mu_3}
    \\ 
    &= \sum_{P \in S_3} \text{sgn}(P) \,
    V_{1}^{\mu_{P(1)}} V_{2}^{\mu_{P(2)}} V_{3}^{\mu_{P(3)}}
\end{align*}
$$

Finally, 

$$
dx^{\mu_1} \wedge dx^{\mu_2} \wedge dx^{\mu_3}
= \sum_{P \in S_3} \text{sgn}(P) \,
dx^{\mu_{P(1)}} dx^{\mu_{P(2)}} dx^{\mu_{P(3)}}
$$

Similar process goes on, which finally leads to the *general* expression:

$$
dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
= \sum_{P \in S_r} \text{sgn}(P) \,
dx^{\mu_{P(1)}} \cdots dx^{\mu_{P(r)}}
$$

## General Expression of $r$-Forms

A general $(0,r)$-tensor $\omega$ has the local coordinate expression

$$
\omega^{(r)} = \omega_{\mu_1 ... \mu_r}
dx^{\mu_1} \cdots dx^{\mu_r} 
$$

Recall that *total anti-symmetry* requires that

$$
\omega_{\mu_{P(1)} ... \mu_{P(r)}} 
= \text{sgn}(P) \, \omega_{\mu_1 ... \mu_r}
$$

which means that for nonzero $\omega_{\mu_{P(1)} ... \mu_{P(r)}}$, the indices $\mu_1, ..., \mu_r$ are *all different from each other*. 

Next, we exploit the anti-symmetry of $\omega$ and collect all terms in $\omega$ which are obtained from an $r$-permutation. For example, the 2-form in $M = \mathbb{R}^3$ is

$$
\begin{align*}
    \omega^{(2)} &= 
    \omega_{12} dx^1 dx^2 + \omega_{13} dx^1 dx^3 
    \\ &\quad 
    + \omega_{21} dx^2 dx^1 + \omega_{23} dx^2 dx^3
    + \omega_{31} dx^3 dx^1 + \omega_{32} dx^3 dx^2
    \\
    &= \omega_{12} (dx^1 dx^2 - dx^2 dx^1)
    \\ &\quad 
    + \omega_{13} (dx^1 dx^3 - dx^3 dx^1)
    + \omega_{23} (dx^2 dx^3 - dx^3 dx^2)
    \\
    &= \sum_{\mu_1 < \mu_2} \omega_{\mu_1 \mu_2}
    (dx^{\mu_1} dx^{\mu_2} - dx^{\mu_2} dx^{\mu_1})
    \\
    &= \sum_{\mu_1 < \mu_2} \omega_{\mu_1 \mu_2}
    \sum_{P\in S_2} \text{sgn}(P) \,
    dx^{\mu_{P(1)}} dx^{\mu_{P(2)}}
\end{align*}
$$

In general, for an $r$-form

$$
\begin{align*}
    \omega^{(r)}
    &= \sum_{\mu_1 < \cdots < \mu_r} 
    \omega_{\mu_1 ... \mu_r}
    \sum_{P\in S_r} \text{sgn}(P) \,
    dx^{\mu_{P(1)}} \cdots dx^{\mu_{P(r)}}
    \\
    &= \sum_{\mu_1 < \cdots < \mu_r} 
    \omega_{\mu_1 ... \mu_r} \,
    dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
\end{align*}
$$

We can also remove the constraint $\mu_1 < \cdots < \mu_r$ and introduce a factor of $1/r!$ to account for repeated counting:

$$
\omega = \frac{1}{r!} \omega_{\mu_1 ... \mu_r} 
dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
$$

*Remark*: 

- We have now shown that an $m$-dimensional manifold $M$ can only have non-vanishing differential forms *up to degree $m$*. 

- All $r$-forms at point $p \in M \, (\dim{M} = m)$ of the form 

    $$
    dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}, \quad
    1 \le \mu_1, ..., \mu_r \le m
    $$

    form a set of *basis* of the vector space $\Omega^r_p(M)$, and

    $$
    \dim{\Omega^r_p(M)} =
    \begin{pmatrix}
        m \\ r
    \end{pmatrix}
    \equiv \frac{m!}{r!(m-r)!}
    $$

    since we are *selecting* $r$ 1-forms from the $m$ dual bases from $T_p^* M$.



- The space of differential forms of *all degree*

    $$
    \Omega^*_p(M) \equiv \bigoplus_{i=1}^m \Omega^i_p(M)
    $$

    is *closed* under the exterior product.

## Exterior Derivatives

*Definition*:

- **Exterior derivative on differential forms**: for a general $r$-form
    
    $$
    \begin{align*}
        \omega 
        &= \sum_{\mu_1 < \cdots < \mu_r} 
        \omega_{\mu_1 ... \mu_r} \,
        dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
        \\
        &= \frac{1}{r!} \omega_{\mu_1 ... \mu_r}
        dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    \end{align*}
    $$

    the exterior derivative $d_r: \Omega^r(M) \to \Omega^{r+1}(M)$ (or simply $d$) is defined to act on $\omega$ as follows:

    $$
    \begin{align*}
        d \omega &\equiv 
        \sum_{\mu_1 < \cdots < \mu_r} \left(
            \frac{\partial}{\partial x^\mu} 
            \omega_{\mu_1 ... \mu_r}
        \right) dx^\mu \wedge
        dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
        \\
        &= \frac{1}{r!} \left( 
            \frac{\partial}{\partial x^\mu}
            \omega_{\mu_1 ... \mu_r}
        \right) dx^\mu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    \end{align*}
    $$

    Due to anti-commutativity of 1-forms with respect to wedge product, we see that nonzero terms must have $\mu \ne \mu_1, ..., \mu_r$. 

## Coordinate-free Expression

- Action on 1-forms

    $$
    (d\omega)(X,Y) = X[\omega(Y)] - Y[\omega(X)] - \omega([X,Y])
    $$

    *Proof*: Using the coordinate expression

    $$
    X = X^\mu \partial_\mu, \quad
    Y = Y^\mu \partial_\mu, \quad
    \omega = \omega_\mu dx^\mu
    $$

    we obtain

    $$
    \begin{align*}
        \text{LHS}
        &= \partial_\mu \omega_{\nu}
        (dx^\mu \wedge dx^{\nu})(X, Y)
        \\
        &= \partial_\mu \omega_{\nu} (
            X^\mu Y^\nu - Y^\mu X^\nu
        )
        \\
        \text{RHS} 
        &= X^\mu \partial_\mu (\omega_\nu Y^\nu)
        - Y^\mu \partial_\mu (\omega_\nu X^\nu)
        \\ &\quad
        - \omega_\nu (
            X^\mu \partial_\mu Y^\nu 
            - Y^\mu \partial_\mu X^\nu
        )
        \\
        &= \partial_\mu \omega_\nu (X^\mu Y^\nu - X^\nu Y^\mu) = \text{LHS} \qquad \blacksquare
    \end{align*}
    $$

- General formula for $r$-forms
    
    $$
    \begin{align*}
        &(d\omega)(X_1, ..., X_r, X_{r+1}) \\
        &= \sum_{i=1}^r (-1)^{i+1} X_i[\omega(X_1, ..., \cancel{X_i}, ..., X_{r+1})]
        \\ &\quad
        + \sum_{i<j} (-1)^{i+j} 
        \omega([X_i,X_j], X_1, ..., \cancel{X_i}, ..., \cancel{X_j}, ..., X_{r+1})
    \end{align*}
    $$


## Properties of Exterior Derivative

- Exterior derivative is **nilpotent**:
    
    $$
    d^2 \equiv d_{r+1} \circ d_r = 0
    $$

- Exterior derivative with exterior product

    Let $\xi \in \Omega^q(M), \omega \in \Omega^r(M)$.
    
    $$
    d(\xi \wedge \omega) = d\xi \wedge \omega + (-1)^q \xi \wedge d\omega
    $$

- Exterior derivative **commutes** with pullback
    
    Let $\omega \in \Omega^r(N), \, f: M \to N$

    $$
    d(f^* \omega) = f^*(d \omega)
    $$
    
    <span style="color:red">
    
    *Proof*: Let the coordinates used in $M, N$ be $x, y$ respectively. Using the coordinate expression, we obtain

    $$
    \begin{align*}
        &d (f^*\omega) 
        = \frac{1}{r!} 
        \partial_\mu (f^* \omega)_{\mu_1 ... \mu_r}
        dx^\mu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
        \\
        &= \frac{1}{r!} 
        \partial_\mu \left(
            \omega_{\nu_1 ... \nu_s}
            \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}} \cdots
            \frac{\partial y^{\nu_s}}{\partial x^{\mu_s}}
        \right)
        dx^\mu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    \end{align*}
    $$

    On the other hand,

    $$
    \begin{align*}
        &f^* (d\omega)
        = f^* \left(
            \frac{1}{r!} \left( 
                \frac{\partial}{\partial y^\mu}
                \omega_{\mu_1 ... \mu_r}
            \right) dy^\mu \wedge dy^{\mu_1} \wedge \cdots \wedge dy^{\mu_r}
        \right)
        \\
        &= \frac{1}{r!} \left( 
            \frac{\partial}{\partial y^\nu}
            \omega_{\nu_1 ... \nu_r}
        \right)
        \frac{\partial y^{\nu}}{\partial x^{\mu}} dx^{\mu}
        \wedge
        \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}} dx^{\mu_1}
        \wedge \cdots \wedge
        \frac{\partial y^{\nu_r}}{\partial x^{\mu_r}} dx^{\mu_r}
        \\
        &= \frac{1}{r!} ( 
            \partial_\mu \omega_{\nu_1 ... \nu_r}
        )
        \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}}
        \cdots
        \frac{\partial y^{\nu_r}}{\partial x^{\mu_r}} \,
        dx^{\mu} \wedge dx^{\mu_1}
        \wedge \cdots \wedge dx^{\mu_r}
    \end{align*}
    $$

    Thus the two sides are equal. $\blacksquare$

    </span>

- Pullback is **distributive** over exterior product:
    
    Let $\xi, \omega$ be differential forms defined in $N$, and $f: M \to N$

    $$
    f^*(\xi \wedge \omega) = (f^* \xi) \wedge (f^* \omega)
    $$

## Interior Product and Lie Derivative of Forms

*Definition*:

- **Interior product**

## Application to Classical Mechanics