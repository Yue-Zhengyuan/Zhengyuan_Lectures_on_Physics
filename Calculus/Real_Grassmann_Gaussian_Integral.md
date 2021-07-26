# Grassmann Gaussian Integral

For Grassmann numbers, *integration is the same as differentiation.* This leads to many different properties of Gaussian integrals for Grassmann variables.

## Integral of "Real" Variables

We first consider Gaussian integral of purely non-conjugate variables ($n$ must be an *even* integer in order that the integral does not vanish), motivated by the **Majorana (real) fermion**

$$
\begin{align*}
    Z(0)=\int d\eta_1 ... d\eta_n\exp \left(-\frac{1}{2}\sum_{i,j=1}^n \eta_iA_{i j}\eta_j\right)
\end{align*}
$$

Because $n$ is even, it makes no difference if we write the integral measure in reverse order. The matrix $A$ here, however, is assumed to be a real *anti-symmetric* matrix. The additional factor 1/2 is introduced to account for repeated counting:

$\frac{1}{2}\sum_{i,j=1}^n \eta_iA_{i j}\eta_j=\sum_{i<j}  \eta_iA_{i j}\eta_j\text{ }\Longrightarrow \text{ }Z(0)=\int d\eta_n ... d\eta
_1\exp \left(-\sum_{i<j}  \eta_iA_{i j}\eta_j\right)$

The corresponding generating function is

$Z(\xi )=\int d\eta_n ... d\eta_1\exp \left(-\sum_{i<j} \eta_iA_{i j}\eta_j+\sum_{i=1}^n  \xi_i\eta_i\right)\\
=\int d\eta_n ... d\eta_1\prod_{i<j} \left(1-\eta_iA_{i j}\eta_j\right)\prod_{i=1}^n  \left(1+\xi_i\eta_i\right)$

The result contains a new structure, called the **Pfaffian** (denoted $\operatorname{Pf} A$), whose square equals $\det A$:

$Z(0)=\operatorname{Pf} A,\text{      }\\
Z(\xi )=Z(0) \exp \left(\frac{1}{2}\sum_{i,j=1}^n  \xi_i\left(A^{-1}\right)_{i j}\xi_j\right)=Z(0) \exp \left(\sum_{i<j}  \xi_i\left(A^{-1}\right)_{i
j}\xi_j\right)$

What the "Pfaffian" is and why $n$ should be an even number will be made clear in the following proof.

*Proof*: Consider the source-free $n$-*variable* integral first. Similar to the $n$-*species* case, the nonzero contribution comes from the terms containing *one and only one* $\eta_i$ for *each* $i$. we obtain

$Z(0)=\int  d\eta_n ... d\eta_1\sum_{\sigma} \text{ }\left(-\eta_{\sigma (1)}A_{\sigma (1)\sigma (2)}\eta_{\sigma (2)}\right)\left(-\eta
_{\sigma (3)}A_{\sigma (3)\sigma (4)}\eta_{\sigma (4)}\right) ... \\
\left(-\eta_{\sigma (n-1)}A_{\sigma (n-1)\sigma (n)}\eta_{\sigma (n)}\right)\\
=\sum_{\sigma} (-1)^{p(\sigma )}\int  d\eta_n ... d\eta_1 \left(\eta_1 ... \eta_n\right)A_{\sigma (1)\sigma (2)} ... A_{\sigma
(n-1)\sigma (n)}=\\
\sum_{\sigma} (-1)^{p(\sigma )}A_{\sigma (1)\sigma (2)} ... A_{\sigma (n-1)\sigma (n)}$

Here we demand that the permutation $\sigma$ should satisfy:

1\. Because in the product expansion of the exponential function, we
have $i<j$, then

$\sigma (1)<\sigma (3)< ... <\sigma (n-1)$

2\. Because each $\eta_i$ can appear only once

$\sigma (1)<\sigma (2), \sigma (3)<\sigma (4),  ... , \sigma (n-1)<\sigma (n)$

Now we see that if $n$ is an odd number, the second requirement cannot
be satisfied, and the integral is zero.

The expression

$Z(0)=\sum_{\sigma} (-1)^{p(\sigma )}A_{\sigma (1)\sigma (2)} ... A_{\sigma (n-1)\sigma (n)}$

is *defined* as the Pfaffian of the anti-symmetric matrix $A$.

Now turn on the source term. We first rewrite the generating function in
a clearer form

$Z(\xi )=\int d\eta_n ... d\eta_1\prod_{i<j} \left(1-\eta_iA_{i j}\eta_j\right)\prod_{i=1}^n  \left(1+\xi_i\eta_i\right)\\
=\int d\eta_n ... d\eta_1$

### Wick's Theorem

Similar to the ordinary real case, we can find the $m$-point function from the generating function:

$\left\langle \eta_{a(1)} ... \eta_{a(m)}\right\rangle \equiv \frac{\int d\eta_n ... d\eta_1 \eta_{a(1)} ... \eta_{a(m)}\exp
\left(-\frac{1}{2}\eta_iA_{i j}\eta_j\right)}{\int d\eta_n ... d\eta_1 \exp \left(-\frac{1}{2}\eta_iA_{i j}\eta_j\right)}=\\
\left.\frac{\partial}{\partial \xi_{a(m)}} ... \frac{\partial}{\partial \xi_{a(1)}}\mathcal{Z}(\xi )\right]_{\xi =0}$

To fix the sign, we demand that the sequence $a(1), ... a(m)$
should be ordered from small to large:

$a(1)<a(2)< ... <a(m)$

If any two of them are *equal*, then the correlation function vanishes
because of the anti-commutativity of the Grassmann variables.

In the Grassmann case, *the differentiation order matters*, and Wick's
theorem will involve sign changes for some terms.

- Basic element: Two-point functions

    $$
    \left\langle \eta_a\eta_b\right\rangle 
    = [A^{-1}]_{a b}
    $$

    *Proof*:

    The first derivative we need to calculate is

    $\frac{\partial}{\partial \xi_a}\exp \left(\frac{1}{2}\sum_{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)$

    However, when differentiating on the second $\xi$, we need to bring it
    to the front (swapping position with the first $\xi$), producing a
    negative sign. we obtain

    $\frac{\partial}{\partial \xi_a}\exp \left(\frac{1}{2}\sum_{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)=\\
    \left(-\frac{1}{2}\sum_{i=1}^n  \xi_i [A^{-1}]_{i a}+\frac{1}{2}\sum_{j=1}^n  [A^{-1}]_{a j}\xi_j\right) \exp ( ... )$

    We still define it as the structure $B_a$ linear in $\xi$

    $B_a[\xi ]=-\frac{1}{2}\sum_{i=1}^n  \xi_i [A^{-1}]_{i a}+\frac{1}{2}\sum_{j=1}^n  [A^{-1}]_{a j}\xi_j\text{     
   }(a=1, ... ,n)$

    and

    $\frac{\partial}{\partial \xi_a}\exp \left(\frac{1}{2}\sum_{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)=B_a(\xi ) \exp \left(\frac{1}{2}\sum
  _{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)$

    Luckily, because of the *anti-symmetry* of $A$ (and $A^{-1}$),

    $\frac{\partial B_a}{\partial \xi_b}=-\frac{1}{2}[A^{-1}]_{b a}+\frac{1}{2}[A^{-1}]_{a b}=[A^{-1}]_{a b}$

    this result still holds.

The Wick's theorem for Grassmann Gaussian integrals then states that

- Mean values of an *even* number of variables can be obtained by finding *all pairings of the variables*, calculate the product of the two-point functions, and sum over all pairings. But the term should carry a *negative* sign if the permutation needed to pair the variables has
*odd* parity.

- Mean values of an *odd* number of variables are *zero* identically.

*Example*: 4-point function

$$
\langle i j k l\rangle =\langle i j\rangle \langle k l\rangle -\langle i k\rangle \langle j l\rangle +\langle i l\rangle \langle j k\rangle
$$

The four letters *must* represent different variables (without loss of generality, we assume that $i<j<k<l$).

*Proof:*

$$
\begin{align*}
    \langle i j k l\rangle 
    &=
    \frac{\partial}{\partial \xi_l}
    \frac{\partial}{\partial \xi_k}
    \frac{\partial}{\partial \xi_j}
    \frac{\partial}{\partial \xi_i}
    \exp ( ... )
    = 
    \frac{\partial}{\partial \xi_l}
    \frac{\partial}{\partial \xi_k}
    \frac{\partial}{\partial \xi_j}
    B_i \exp ( ... )
    \\
    &=
    \frac{\partial}{\partial \xi_l}
    \frac{\partial}{\partial \xi_k}
    (
        \langle i j\rangle \exp ( ... )
        - B_i B_j\exp ( ... )
    )
    \\
    &\text{(
        the minus sign is due to the exchange of
        $\partial /\partial \xi_j$ and $B_i$
    )}
    \\
    &= \frac{\partial}{\partial \xi_l}(
        \langle i j\rangle B_k\exp ( ... )-\langle i k\rangle B_j\exp ( ... )
        \\ &\qquad
        + B_i\langle j k\rangle \exp ( ... )
        - B_i B_j B_k\exp ( ... )
    )
    \\
    &= \langle i j\rangle \langle k l\rangle 
    -\langle i k\rangle \langle j l\rangle 
    +\langle i l\rangle \langle j k\rangle 
    +(\text{terms} \propto B)
    \\
    &\xrightarrow{\xi = 0}
    \langle i j\rangle \langle k l\rangle 
    - \langle i k\rangle \langle j l\rangle 
    + \langle i l\rangle \langle j k\rangle
    \end{align*}
$$
