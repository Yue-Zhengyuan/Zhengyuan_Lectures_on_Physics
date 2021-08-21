# Compactified Boson

Recall that a free boson field $\phi(z,\bar{z})$ compactified on a circle of radius $R$ is identified in the following way:

$$
\phi(z,\bar{z}) = \phi(z,\bar{z}) + 2\pi n R, \quad
n \in \Z
$$

i.e. $\phi$ is treated as an angular variable. 

*Remark*: We emphasize that the circle has no direct relation with the manifold described by the variables $z,\bar{z}$. The latter is the space the theory is defined on, which in our case is the Riemann sphere respectively a torus.

## Partition Function

The currents have the mode expansion

$$
\begin{align*}
    j(z) &\equiv i \partial \phi 
    = \sum_{n \in \Z} j_n z^{-n-1}
    \\
    \bar{j}(\bar{z}) &\equiv i \bar{\partial} \phi 
    = \sum_{n \in \Z} \bar{j}_n \bar{z}^{-n-1}
\end{align*}
$$

After integration over $z, \bar{z}$, we obtain (here we take the $g = 1/4\pi$ normalization)

$$
\phi(z,\bar{z}) 
= x_0 - i (j_0 \ln z + \bar{j}_0 \ln \bar{z})
+ i \sum_{n \ne 0} \frac{1}{n} (
    j_n z^{-n} + \bar{j}_n \bar{z}^{-n}
)
$$

Now we require that the field is invariant under the $2\pi$ rotation $z \to e^{2\pi i} z$, but now up to the angular identification:

$$
\phi(e^{2\pi i} z, e^{-2\pi i} \bar{z})
= \phi(z, \bar{z}) + 2\pi n R,
\quad z \in \Z
$$

Using the expression of $\phi$ obtained above, we find

$$
j_0 - \bar{j}_0 = n R,
\quad z \in \Z
$$

Then we infer that

$$
j_0 | Q,n\rangle = Q |Q,n\rangle, \quad
\bar{j}_0 |Q, n \rangle = (Q - nR) |Q, n \rangle
$$

where $Q$ is the $j_0$ charge to be determined later. 

The partition function of the compactified boson (cb) is related to the free boson (fb) by

$$
\begin{align*}
    Z_{\text{cb}} (\tau,\bar{\tau})
    &= Z_{\text{fb}}(\tau, \bar{\tau}) 
    \sum_{Q, n} \langle Q,n | q^{j_0^2/2} \bar{q}^{\bar{j}_0^2/2} | Q,n \rangle
    \\
    &= \frac{1}{|\eta(\tau)|^2}
    \sum_{Q,n} q^{Q^2/2} \bar{q}^{(Q-nR)^2/2}
\end{align*}
$$

The partition function should be invariant under modular transformations. We can use the *T*-transformation ($\tau \to \tau + 1$) only to determine the form of $Q$: recall that $q \equiv e^{2\pi i \tau}$, then

$$
Z_{\text{cb}} (\tau+1, \bar{\tau}+1)
= \frac{1}{|\eta(\tau)|^2}
\sum_{Q, n} q^{Q^2/2} \bar{q}^{(Q-nR)^2/2}
e^{2\pi i n (QR - nR^2/2)}
$$

Thus we require

$$
QR - \frac{n R^2}{2} = m 
\, \Rightarrow \,
Q =  \frac{m}{R} + \frac{nR}{2},
\quad
m \in \Z
$$

Using this new notation, we write

$$
\begin{align*}
    j_0 |m,n \rangle &= \left(
        \frac{m}{R} + \frac{nR}{2}
    \right) |m,n \rangle
    \\
    \bar{j}_0 |m,n \rangle &= \left(
        \frac{m}{R} - \frac{nR}{2}
    \right) |m,n \rangle
\end{align*}
$$

and

$$
Z_{\text{cb}}(\tau, \bar{\tau}) 
= \frac{1}{|\eta(\tau)|^2}
\sum_{m, n} q^{(m/R + nR/2)^2/2} 
\bar{q}^{(m/R - nR/2)^2/2}
$$

## Operators in Mode Expansion

With the expression of $j_0, \bar{j}_0$ above, the mode expansions of $\phi$ and its derivatives are

$$
\begin{align*}
    \phi(z,\bar{z})
    &= \phi_0
    - i \left(
        \frac{m}{R} + \frac{nR}{2}
    \right) \ln z
    + i \sum_{n \ne 0}
    \frac{1}{n} a_n z^{-n}
    \\ &\qquad
    - i \left(
        \frac{m}{R} - \frac{nR}{2}
    \right) \ln \bar{z}
    + \frac{i}{\sqrt{4\pi g}} \sum_{n \ne 0}
    \frac{1}{n} \bar{a}_n \bar{z}^{-n}
    \\
    i \partial \phi(z)
    &= \left(
        \frac{m}{R} + \frac{nR}{2}
    \right) \frac{1}{z}
    + \sum_{n \ne 0} a_n z^{-n-1}
    \\
    i \bar{\partial} \phi(\bar{z})
    &= \left(
        \frac{m}{R} - \frac{nR}{2}
    \right) \frac{1}{\bar{z}}
    + \sum_{n \ne 0} \bar{a}_n \bar{z}^{-n-1}
\end{align*}
$$

Here we see that $a_0, \bar{a}_0$ should be redefined to

$$
\begin{align*}
    a_0 
    &= \frac{m}{R} + \frac{nR}{2}
    \\
    \bar{a}_0 
    &= \frac{m}{R} - \frac{nR}{2}
\end{align*}
$$

Then the generators $L_0, \bar{L}_0$ are found to be

$$
\begin{align*}
    L_0 
    &= \sum_{n>0} a_{-n} a_n 
    + \frac{1}{2} \left(
        \frac{m}{R} + \frac{nR}{2}
    \right)^2
    \\
    \bar{L}_0 
    &= \sum_{n>0} \bar{a}_{-n} {a}_n 
    + \frac{1}{2} \left(
        \frac{m}{R} - \frac{nR}{2}
    \right)^2
\end{align*}
$$

## Invariance of $Z_\text{cb}$ under *S*-Transformations

To show the invariance of the partition function under the *S*-transformation ($\tau \to -1/\tau$)

$$
Z_\text{cb} \left(
    -\frac{1}{\tau}, -\frac{1}{\bar{\tau}}
\right) = Z_{\text{cb}}(\tau, \bar{\tau}) 
$$

we need to use the **Poisson Resummation Formula**

$$
\sum_{n \in \Z} \exp(-\pi a n^2 + b n)
= \frac{1}{\sqrt{a}} \sum_{k \in \Z}
\exp \left[
    -\frac{\pi}{a} \left(
        k + \frac{b}{2\pi i}
    \right)^2
\right]
$$

## Appendix A: <br>Proof of Poisson Resummation Formula

balabala

## Appendix B: <br>Compactification Radius from Partition Function

*Reference: Physical Review B **99**, 115105 (2019)*


