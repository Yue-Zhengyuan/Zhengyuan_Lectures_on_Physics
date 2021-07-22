# Complex Gaussian Integral

Sometimes (when considering complex valued fields) we need to consider Gaussian integrals of pairs of "conjugate" complex variables.

<div class="result">

**Complex Gaussian integral (one variable-pair):**

- Generating function

    $$
    Z(\bar{J},J)
    = \int \frac{d\bar{z} \, dz}{2\pi i}
    \exp (- \bar{z} a z + \bar{z} J + \bar{J} z)
    $$

    - $a$ is a complex number.
    - $z, \bar{z}$ are independent, *not* the complex conjugate of each other. 
    - $J, \bar{J}$ are two independent complex numbers (the **sources**).

- Integration result

    $$
    \begin{align*}
        Z(0,0) &= a^{-1}
        \\[0.5em]
        Z(\bar{J},J)
        &= Z(0,0) \exp (\bar{J} a^{-1} J)
    \end{align*}
    $$

</div><br>

<div class="remark">

*Remark*: The integration measure $d\bar{z} \, dz$ needs clarification. The additional $2\pi i$ factor is motivated by boson coherent state path integral. To really do the integration, we need to use real variables. 

- In Cartesian coordinates

    $$
    z=x+i y \qquad \bar{z}=x-i y
    $$

    $$
    d\bar{z} \, dz
    = \frac{\partial(\bar{z},z)}{\partial(x,y)} dx \, dy
    = 2i \, dx \, dy
    $$

- In polar coordinates

    $$
    z = r e^{i \theta}, \quad \bar{z} = r e^{-i \theta}
    $$

    $$
    d\bar{z} \, dz
    = \frac{\partial (\bar{z},z)}{\partial (r,\theta)}dr \, d\theta 
    = 2i r \, dr \, d\theta
    $$

</div><br>

*Proof*:

Using Cartesian coordinates, we find

$$
\begin{align*}
    Z(\bar{J}, J)
    &= \frac{1}{\pi}\int dx \, dy \exp \left(
        -a (x^2+y^2) + (x-i y)J + \bar{J} (x+i y)
    \right)
    \\
    &= \frac{1}{\pi}
    \int dx \, dy 
    \exp \left[-a x^2+ (J+ \bar{J})x \right] 
    \exp \left[-a y^2+i (-J+ \bar{J})y \right]
    \\
    &= \frac{1}{\pi} 
    \times \sqrt{\frac{\pi}{a}} \exp
    \frac{\left(J+ \bar{J}\right)^2}{4a}
    \times \sqrt{\frac{\pi}{a}} \exp
    \frac{\left[i \left(-J+ \bar{J}\right)\right]^2}{4a}
    \\
    &= a^{-1}\exp \left(\bar{J} a^{-1}J\right)
    \qquad \blacksquare
\end{align*}
$$

## Multi-Variable-Pair Case

The generalization to multi-variable-pair case is straightforward.

<div class="result">

**Complex Gaussian integral (multiple variable-pair):**

- Generating function

    $$
    \begin{align*}
        Z(\bar{J}, J)
        &= \int D\bar{z} \, Dz
        \exp \left(
            - \bar{z}_i A_{ij} z_j
            + \bar{z}_i J_i + \bar{J}_i z_i
        \right)
        \\
        &= \int D\bar{z} \, Dz
        \exp \left(
            - \bar{z} A z + \bar{z} J + \bar{J} z
        \right)
        \\
        \text{with} \quad
        D\bar{z} \, Dz &\equiv 
        \prod_{j=1}^n \frac{d\bar{z}_j dz_j}{2\pi i}
    \end{align*}
    $$

    - $A$ is an $n \times n$ *Hermitian* matrix. 
    - $J$ is an $n$-dimensional column vectors (the **sources**).
    - When a bar is added on a column vector, it is "conjugated" and transposed to a row vector (similar to the Hermitian conjugation $\dagger$). E.g. $z, J \in \mathbb{C}^{n\times 1} \rightarrow \bar{z}, \bar{J} \in \mathbb{C}^{1\times n}$.

- Integration result
    
    $$
    \begin{align*}
        Z(0,0) &= \frac{1}{\det A}
        \\[1em]
        \frac{Z(\bar{J}, J)}{Z(0,0)}
        &= \exp [
            \bar{J}_i (A^{-1})_{i j} J_j
        ] \equiv \mathcal{Z}(\bar{J}, J)
    \end{align*}
    $$

</div><br>

*Proof*:

Since $A$ is Hermitian, we can diagonalize it with a *unitary* matrix
$U$ with determinant 1:

$$
\Lambda =U^{\dagger}A U \Rightarrow \left\{
\begin{align*}
     A &=U \Lambda U^{\dagger}
     \\
     A^{-1} &= (U^{\dagger})^{-1} \Lambda^{-1} O^{-1}
     = U \Lambda^{-1} U^{\dagger}
\end{align*}
\right.
$$

Introduce new variables and new sources

$$
\begin{align*}
    w &= U^{\dagger}z, &\quad 
    \bar{w} &= \bar{z} U
    \\
    \mathcal{J} &= U^{\dagger}J, &\quad
    \bar{\mathcal{J}} &= \bar{J} U
\end{align*}
$$

Then

$$
\begin{align*}
    Z(\bar{J}, J)
    &= \int D\bar{z} \, Dz 
    \exp \left(- \bar{z}A z+ \bar{z}J+ \bar{J}z\right)
    \\
    &= \int D\bar{z} \, Dz
    \exp \left(- \bar{z}U \Lambda  U^{\dagger} z+ \bar{w}U^{\dagger}J+ \bar{J}U
    w\right)
    \\
    &= \int D\bar{z} \, Dz
    \exp \left(- \bar{w}\Lambda  w+ \bar{w}\mathcal{J}+ \bar{\mathcal{J}}w\right)
\end{align*}
$$

We now successfully diagonalized the exponent

$$
Z(\bar{J}, J)
= \prod_{k=1}^n \int 
\left[\frac{d\bar{w}_kdw_k}{2\pi i}\right] 
\exp \left(
    - \bar{w}_k \Lambda_k w_k
    + \bar{w}_k \mathcal{J}_k
    + \bar{\mathcal{J}}_k w_k
\right)
$$

Now we can apply our previous result about one-variable-pair integral

$$
\begin{align*}
    Z(\bar{J}, J)
    &= \prod_{k=1}^n  \frac{1}{\Lambda_k} \exp (
        \bar{\mathcal{J}}_k \Lambda_k^{-1} \mathcal{J}_k
    )
    = \frac{1}{\det A} \exp (
        \bar{\mathcal{J}}\Lambda^{-1}\mathcal{J}
    )
    \\
    &= \frac{1}{\det A}\exp (
        \bar{J} U \Lambda^{-1} U^{\dagger} J
    )
    = \frac{1}{\det A} \exp (\bar{J} A^{-1} J)
    \quad \blacksquare
\end{align*}
$$

## Wick's Theorem

With the generating function, we can take the $J$ (or $\bar{J}$) derivative to get various mean values and derive Wick's Theorem. The basic building blocks are

<div class="result">

**Two-point functions:**

$$
\langle z_a z_b\rangle =0, \quad
\langle \bar{z}_a \bar{z}_b\rangle =0, \quad
\langle \bar{z}_a z_b\rangle = \langle z_b\bar{z}_a\rangle
= (A^{-1})_{a b}
$$

They are also denoted by

$$
\langle a b\rangle ,
\langle \bar{a} \bar{b}\rangle ,
\langle \bar{a} b\rangle, 
\langle b \bar{a}\rangle
$$

A nonzero two-point function must include one variable and one "conjugate"
variable.

</div><br>

*Proof*: First take the derivative of $J_a$ of the normalized generating function

$$
\begin{align*}
    \frac{\partial}{\partial J_a}\mathcal{Z}(\bar{J}, J)
    &= \left(\sum_{i=1}^n \bar{J}_i(A^{-1})_{i a}\right)\exp(...)
    \\
    &\equiv \bar{B}_a(\bar{J}) \exp(...)
\end{align*}
$$

Since the structure $\bar{B}_a$ does not contain $J$, the two point
function $\langle a b\rangle$ must vanish. But

$$
\frac{\partial \bar{B}_a}{\partial \bar{J}_b}=(A^{-1})_{b a}
$$

Similarly, taking the derivative of $\bar{J}_a$ of the normalized generating function

$$
\begin{align*}
    \frac{\partial}{\partial \bar{J}_a}\mathcal{Z}(\bar{J}, J)
    &= \left(\sum_{i=1}^n (A^{-1})_{a i}J_i\right)\exp(...)
    \\
    &\equiv B_a(J)\exp(...)
\end{align*}
$$

The structure $B_a$ does not contain $\bar{J}$, and
$\langle \bar{a} \bar{b}\rangle$ vanishes. And

$$
\frac{\partial B_a}{\partial J_b}=(A^{-1})_{a b}
$$

Only the pairs with both kinds of variables survive:

$$
\begin{align*}
    \expect{\bar{z}_a z_b}
    &= \frac{\partial}{\partial J_b}
    \frac{\partial}{\partial \bar{J}_a} \exp(...)
    = \frac{\partial}{\partial J_b} B_a(J) \exp(...)
    \\
    &= (A^{-1})_{a b}\exp(...)+B_a(J)\bar{B}_b(\bar{J})
    \xrightarrow{J=0}
    (A^{-1})_{ab}
\end{align*}
$$

Now we know how to generalize the real integral Wick's Theorem. For
example, the 4-point function

$$
\expect{\bar{i} j \bar{k} l} 
= \expect{\bar{i} j} \expect{\bar{k} l} 
+ \expect{\bar{i} l} \expect{\bar{k} j}
$$

*Proof*:

$$
\begin{align*}
    \text{LHS}
    &= \frac{\partial}{\partial J_l}\frac{\partial}{\partial \bar{J}_k}\frac{\partial}{\partial J_j}\frac{\partial}{\partial \bar{J}_i}\exp
    ( ... )= \frac{\partial}{\partial J_l}\frac{\partial}{\partial \bar{J}_k}\frac{\partial}{\partial J_j}\left(B_i\exp(...)\right)
    \\
    &= \frac{\partial}{\partial J_l}\frac{\partial}{\partial \bar{J}_k}\left((A^{-1})_{i j}\exp(...)+B_i\bar{B}_j\exp(...)\right)
    \\
    &= \frac{\partial}{\partial J_l}\left((A^{-1})_{i j}B_k\exp(...)+B_i(A^{-1})_{k j}\exp(...)+B_i\bar{B}_jB_k\exp
    ( ... )\right)
    \\
    &=(A^{-1})_{i j}(A^{-1})_{k l}\exp(...)+(A^{-1})_{i j}B_k\bar{B}_l\exp(...)
    \\ &\qquad 
    +(A^{-1})_{i
    l}(A^{-1})_{k j}\exp(...)+ \left(\text{terms} \propto B,\bar{B}\right)
    \\
    &\xrightarrow{J=0}
    (A^{-1})_{i j}(A^{-1})_{k l}+(A^{-1})_{i l}(A^{-1})_{k j}
    = \expect{\bar{i} j} \expect{\bar{k} l} 
    + \expect{\bar{i} l} \expect{\bar{k} j}
\end{align*}
$$

## Fourier Transform of Integration Variables

