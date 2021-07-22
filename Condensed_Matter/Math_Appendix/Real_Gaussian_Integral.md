# Real Gaussian Integral

To begin with, we review the standard result of one-variable Gaussian integral:

<div class="result">

**Real-variable Gaussian integral (multiple variable):**

- Generating function

    $$
    \begin{align*}
        Z(J)
        &= \int dx \exp \left(- \frac{1}{2}a x^2 + J x\right)
    \end{align*}
    $$

    - $a$ is a positive real number 
    - $J$ is a real number (called the **source**).

- Integration result of the generating function

    $$
    \begin{align*}
        Z(0) &= \bigg(\frac{2\pi}{a}\bigg)^{1/2}
        \\
        \frac{Z(J)}{Z(0)} &= \exp \left(
            \frac{J^2}{2a}
        \right)
        \equiv \mathcal{Z}(J)
    \end{align*}
    $$

</div><br>

Now we generalize Gaussian integral to many-variable case. 

<div class="result">

**Real-variable Gaussian integral (multiple variable):**

- Generating function

    $$
    \begin{align*}
        Z(J)
        &= \int dx_1 ... dx_n \exp \left(- \frac{1}{2}x_iA_{i j}x_j+J_ix_i\right)
        \\
        &= \int dx_1 ... dx_n \exp \left(- \frac{1}{2}x^{\mathsf{T}}A x+J^{\mathsf{T}}x\right)
    \end{align*}
    $$

    - $A$ is a real symmetric $n\times n$ matrix
    - $J$ is a real $n$-dimensional column vector (called the **source**).

- Integration result of the generating function

    $$
    \begin{align*}
        Z(0) &= \frac{(2\pi)^{n/2}}{(\det A)^{1/2}}
        \\
        \frac{Z(J)}{Z(0)} &= \exp \left(
            \frac{1}{2} J_i [A^{-1}]_{i j}J_j
        \right)
        \equiv \mathcal{Z}(J)
    \end{align*}
    $$

</div><br>

*Proof*: 

The standard method is to *diagonalize* the matrix $A$. Since it is real symmetric, diagonalization can be done by an *orthogonal matrix* $O$ (which has *unit determinant*). Let the matrix after diagonalization be $\Lambda$:

$$
\Lambda =O^{\mathsf{T}}A O \Rightarrow \left\{ \begin{align*}
    A &= O \Lambda  O^{\mathsf{T}}
    \\ 
    A^{-1} &=
    (O^{\mathsf{T}})^{-1} \frac{1}{\Lambda} O^{-1}
    = O \frac{1}{\Lambda} O^{\mathsf{T}}
\end{align*} \right. 
$$

Here $1/\Lambda$ is the inverse of $\Lambda$. Introduce the new
variables $y=O^{\mathsf{T}}x$. The corresponding Jacobian is 1 (since we choose $\det O=1$). Then

$$
\begin{align*}
    Z(0)
    &= \int dx_1 ... dx_n \exp \left(- \frac{1}{2}x^{\mathsf{T}}O \Lambda  O^{\mathsf{T}}x\right)
    \\
    &= \int dy_1 ... dy_n \exp \left(- \frac{1}{2}y^{\mathsf{T}}\Lambda  y\right)
    \\
    &= \int
    dy_1 ... dy_n \prod_{k=1}^n  \exp \left(- \frac{1}{2}\Lambda_k y_k^2\right)
    \\
    &= \prod_{k=1}^n \int dy_k \exp \left(- \frac{1}{2}\Lambda_k y_k^2\right)
    \\
    &= \prod_{k=1}^n \left(\frac{2\pi}{\Lambda_k}\right)^{1/2}
    = \frac{(2\pi
    )^{n/2}}{(\det \Lambda)^{1/2}}= \frac{(2\pi)^{n/2}}{(\det A)^{1/2}}
\end{align*}
$$

The general $Z(J)$ can be found similarly:

$$
\begin{align*}
    Z(J)
    &= \int dx_1 ... dx_n \exp \left(
        - \frac{1}{2}x^{\mathsf{T}}O \Lambda O^{\mathsf{T}}x
        + J^{\mathsf{T}} x
    \right)
    \\
    &= \int dy_1 ... dy_n \exp \left(- \frac{1}{2}y^{\mathsf{T}}\Lambda  y+J^{\mathsf{T}}Oy\right)
\end{align*}
$$

Define the new parameters $\mathcal{J}=O^{\mathsf{T}}J$:

$$
\begin{align*}
    Z(J)
    &= \int dy_1 ... dy_n \exp \left(- \frac{1}{2}y^{\mathsf{T}}\Lambda  y+ \mathcal{J}^{\mathsf{T}} y\right)
    \\
    &= \int dy_1 ... dy_n \prod_{k=1}^n  \exp \left(- \frac{1}{2}\Lambda_k y_k^2+ \mathcal{J}_k y_k\right)
    \\
    &= \prod_{k=1}^n \int dy_k \exp \left(
        - \frac{1}{2}\Lambda_k y_k^2
        + \mathcal{J}_k y_k
    \right)
    \\
    &= \prod_{k=1}^n \left(\frac{2\pi}{\Lambda_k}\right)^{1/2}\exp \left(\frac{1}{2}\mathcal{J}_k\frac{1}{\Lambda_k}\mathcal{J}_k\right)
    = \frac{(2\pi)^{n/2}}{(\det A)^{1/2}}\exp \left(\frac{1}{2}\mathcal{J}^{\mathsf{T}} \frac{1}{\Lambda}\mathcal{J}\right)
    \\
    &= Z(0) \exp \left(\frac{1}{2}J O\frac{1}{\Lambda}O^{\mathsf{T}}J\right)
    = Z(0) \exp \left(\frac{1}{2}J_i
    [A^{-1}]_{i j}J_j\right)

    \qquad \blacksquare
\end{align*} 
$$

## Wick's Theorem

By differentiating the normalized generating function with respect to the sources $J$, we can obtain the **$n$-point function** (this name comes from quantum field theory and statistical physics):

$$
\begin{align*}
    \left\langle x_{a(1)} ... x_{a(m)}\right\rangle 
    &\equiv \frac{
        \int dx_1 ... dx_n x_{a(1)} ... x_{a(m)}
        \exp \left(
            - \frac{1}{2} x_i A_{ij} x_j
        \right)
    }{
        \int dx_1 ... dx_n \exp \left(
            - \frac{1}{2} x_i A_{ij} x_j
        \right)
    }
    \\
    &= \left[
        \frac{\partial}{\partial J_{a(m)}} ... 
        \frac{\partial}{\partial J_{a(1)}}
        \mathcal{Z}(J)
    \right]_{J=0}
\end{align*}
$$

Sometimes we simply write $\langle a(1) ... a(m)\rangle$. 

<div class="result">

**Two-point functions:**

$$
\left\langle x_ax_b\right\rangle =[A^{-1}]_{a b}
$$

</div><br>

*Proof*: 

To save writing in the proofs in the following, we define a
structure linear in the $J$'s

$B_a[J]= \frac{1}{2}\sum_{i=1}^n  J_i [A^{-1}]_{i a}+ \frac{1}{2}\sum_{j=1}^n  [A^{-1}]_{a j}J_j\text{     }(a=1, ... ,n)$

Obviously $B_a(0)=0$. Then

$\frac{\partial}{\partial J_a}\exp \left(\frac{1}{2}J_i [A^{-1}]_{i j}J_j\right)=B_a(J)\exp \left(\frac{1}{2}J_i[A^{-1}]_{i
j}J_j\right)$

Because of the symmetry of $A$ (and $A^{-1}$), its derivative with
respect to $J$ is

$\frac{\partial B_a}{\partial J_k}= \frac{1}{2}[A^{-1}]_{k a}+ \frac{1}{2}[A^{-1}]_{a k}=[A^{-1}]_{a k}$

Then

$$
\langle a b\rangle = \frac{\partial}{\partial J_b}\frac{\partial}{\partial J_a}\exp(...)= \frac{\partial}{\partial J_b}\left(B_a\exp(...)\right)=[A^{-1}]_{a
b}\exp(...)+B_aB_b\exp(...)\overset{J=0}{\rightarrow}[A^{-1}]_{a b}
$$

<div class="result">

**Wick's theorem:**

Mean values of an *even* number of variables can be obtained by finding
*all pairings of the variables*, calculate the product of the two-point
functions, and sum over all pairings.

Mean values of an *odd* number of variables are *zero* identically.

</div><br>

*Example*: 4-point function

$$
\langle i j k l\rangle = \langle i j\rangle \langle k l\rangle + \langle i k\rangle \langle j l\rangle + \langle i l\rangle \langle j k\rangle
$$

The four letters $i,j,k,l$ need *not* represent different variables.

*Proof*:

$$
\begin{align*}
    \langle i j k l\rangle 
    &= \frac{\partial}{\partial J_l}
    \frac{\partial}{\partial J_k}
    \frac{\partial}{\partial J_j}
    \frac{\partial}{\partial J_i} 
    \exp( ... )
    \\
    &= \frac{\partial}{\partial J_l}
    \frac{\partial}{\partial J_k}
    \frac{\partial}{\partial J_j}
    \left[
        B_i \exp(...)
    \right]
    \\
    &= \frac{\partial}{\partial J_l}
    \frac{\partial}{\partial J_k}
    \left[
        \langle i j\rangle \exp(...)
        + B_i B_j \exp(...)
    \right]
    \\
    &= \frac{\partial}{\partial J_l}
    \big[
        \langle i j\rangle B_k \exp(...)
        + \langle i k\rangle B_j \exp(...)
        \\ &\qquad \qquad
        + B_i\langle j k\rangle \exp(...)
        + B_i B_j B_k \exp( ... )
    \big]
\end{align*}
$$

If we stop differentiation here, we are evaluating
$\langle i j k\rangle$, containing 3 variables; it is obviously zero
because of the $B$'s in each term.

Now we continue:

$\langle i j k l\rangle = \langle i j\rangle \langle k l\rangle \exp(...)+ \langle i k\rangle \langle j l\rangle \exp(...)+ \langle
i l\rangle \langle j k\rangle \exp(...)+(\text{terms} \text{proportional} \text{to} B)$

Setting $J=0$, and we are left with the desired result:

$\langle i j k l\rangle = \langle i j\rangle \langle k l\rangle + \langle i k\rangle \langle j l\rangle + \langle i l\rangle \langle j k\rangle$

