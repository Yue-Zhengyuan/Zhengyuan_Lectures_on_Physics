# Fermion Coherent State

The discussion for fermions almost parallels that for bosons, except some minus signs from anti-commutativity.

## Coherent State and Grassmann Numbers

The eigenstates of the fermion annihilation operator are called 

<div class="result">

**Fermion coherent state:**

- One-fermion states: $c \ket{\psi} = \psi \ket{\psi}$

- $n$-fermion states: $c_1 \cdots c_n \ket{\psi_1 \cdots \psi_n} = \psi_1 \cdots \psi_n \ket{\psi_1 \cdots \psi_n}$

</div><br>

However, because the fermion operators *anti-commute*, we should have

$$
\cdots c_i \cdots c_j \cdots 
|\cdots \psi_i \cdots\psi_j \cdots\rangle 
= - \cdots\psi_j \cdots\psi_i \cdots 
| \cdots \psi_i \cdots \psi_j \cdots\rangle
$$

for any $i\neq j$. This means that $\psi_i$ are not ordinary numbers - they should *anti-commute with each other*. They are called **Grassmann numbers**. We also require that the Grassmann numbers *always anti-commute* with the annihilation / creation operators. 

## Building Coherent State from Vacuum

<div class="result">

**Building coherent state from vacuum:**

$$
\begin{align*}
    \ket{\psi}
    &= \ket{0} - \psi \ket{1}
    = (1-\psi c^\dagger)\ket{0}
    = \exp (-\psi c^\dagger)\ket{0}
    \\
    \bra{\bar{\psi}}
    &= \bra{0} - \bra{1} \bar{\psi}
    = \bra{0}(1 - c\bar{\psi})
    = \bra{0} \exp(-c\bar{\psi})
\end{align*}
$$

</div><br>

*Proof*:

We expand the coherent state using the only two Fock basis states $\ket{0}, \ket{1}$:

$$
\ket{\psi} =c_0\ket{0} +c_1\ket{1}
$$

The coefficients here are *Grassmann numbers*. Then

$$
\begin{align*}
    c\ket{\psi} 
    &= c c_0\ket{0} +c c_1\ket{1} 
    = -c_0c\ket{0} -c_1c\ket{1} =-c_1\ket{0}
    \\
    \psi \ket{\psi} 
    &=\psi \ket{0} +\psi c_1\ket{1}
\end{align*}
$$

Now we conclude that

$$
c_1 = -\psi
$$

Again, $c_0$ is just a normalization and we can set it to be 1. What about the $\psi c_1\ket{1}$ term? Recall that $\psi^n=0$ for any $n \ge 2$. Then $\psi c_1\ket{1} =-\psi^2\ket{1} =0$. Therefore 

$$
\ket{\psi} 
= \ket{0} -\psi \ket{1} 
= (1-\psi c^\dagger)\ket{0}
$$

The "Hermitian conjugate" of this state is

$$
\begin{align*}
    \bra{\bar{\psi}}
    &= \bra{0} (1-c \bar{\psi})
    = \bra{0} - \bra{1}\bar{\psi}
    \quad \blacksquare
\end{align*}
$$

<div class="remark">

*Remark*: 

- For systems containing multiple kinds of fermions,

$$
\begin{align*}
    \ket{\psi} 
    &= \prod_k (1-\psi_kc_k^\dagger)\ket{0} 
    = \prod_k \exp (- \psi_k c_k^\dagger)\ket{0}
\end{align*}
$$

- The number $\bar{\psi}$ is completely independent of $\psi$ (they are *not* "Hermitian conjugates" of each other). We might even call it as a new variable $\eta$, i.e. $\bra{\eta} = \bra{0} - \bra{1} \eta$. 

</div><br>

## Grassmann Calculus

Before we continue to write down the resolution of identity in the fermion case, we must first define differentiation and integration of Grassmann numbers.

Since $\psi^n=0$ for all $n\geq 2$, the analytical functions of Grassmann variables are limited to *multi-linear functions* of its variables. For example, the most general form of an analytical function of two variables $\psi ,\bar{\psi}$ is

$$
f(\psi ,\bar{\psi})
= a_0 + a_1 \psi + a_1^{\prime} \bar{\psi} 
+ a_{12} \psi \bar{\psi}
\quad a_0,a_1,a_1^{\prime},a_{12}\in \mathbb{C}
$$

### Differentiation

The differentiation is almost the same as ordinary differentiation. However, the *order* is important: we must differentiate the *innermost* variable first, then going outside one after another. For example,

$$
\frac{\partial}{\partial \theta}
\frac{\partial}{\partial \psi} (\theta \psi)
= \frac{\partial}{\partial \theta}
\frac{\partial}{\partial \psi} (-\psi \theta)
= \frac{\partial}{\partial \theta}(-\theta)
= -1
$$

### Integration

Integration over Grassmann variables is *defined to be the same* as differentiation.

## Resolution of Identity

<div class="result">

**Over-completeness relation of boson coherent states:**

$$
\int d\bar{\psi} \, d\psi \exp (- \bar{\psi} \psi) 
\ket{\psi} \bra{\bar{\psi}} =\mathbf{1}
$$

</div><br>

*Proof*: 

Since differentiation and integration are equivalent for Grassmann numbers, the proof is much simpler than the bosonic case. 

$$
\begin{align*}
    \text{LHS}
    &= \int d\bar{\psi} \, d\psi 
    (1-\bar{\psi} \psi) \ket{\psi} \bra{\bar{\psi}}
    \\
    &= \int d\bar{\psi} \, d\psi (1-\bar{\psi} \psi) 
    (\ket{0} - \psi \ket{1})
    (\bra{0} - \bra{1} \bar{\psi})
    \\
    &= \int d\bar{\psi} \, d\psi (1-\bar{\psi} \psi) (
        \ket{0} \bra{0}
        - \bar{\psi} \ket{0} \bra{1}
        - \psi \ket{1} \bra{0}
        + \psi \bar{\psi} \ket{1} \bra{1}
    )
    \\
    &= \int d\bar{\psi} \, d\psi (
        - \bar{\psi} \psi \ket{0} \bra{0}
        + \psi \bar{\psi} \ket{1} \bra{1}
    )
    \\
    &= \ket{0} \bra{0}+\ket{1} \bra{1}
    =\mathbf{1}
    \qquad \blacksquare
\end{align*}
$$

## Operators in Coherent State Representation

<div class="result">

**Amplitudes between coherent states:**

For any normal ordered operator $\normord{A(c^\dagger, c)}$ and two coherent states $\bra{\bar{\xi}}, \ket{\psi}$, 

$$
\amp{\bar{\xi}}{\normord{A(c^\dagger,c)}}{\psi}
= e^{\bar{\xi} \psi} \normord{A(\bar{\xi},\psi)}
$$

In particular, when $A$ is the identity operator, we find the overlap between two coherent states

$$
\braket{\bar{\xi}}{\psi} = e^{\bar{\xi} \psi}
$$

</div><br>

*Proof*:

$$
\begin{align*}
    \langle \xi |\psi \rangle 
    &= \langle 0 |\exp ( \bar{\xi} c)\exp (-\psi c^\dagger)|0\rangle 
    \\
    &= \bra{0}(1+\bar{\xi} c)(1-\psi c^\dagger)|0\rangle
    \\
    &= \bra{0}1-\psi c^\dagger +\bar{\xi} c-\bar{\xi} c \psi c^\dagger |0\rangle
    \\
    &= \braket{0}{0} 
    - \amp{0}{\bar{\xi} c \psi c^\dagger}{0}
    \\
    &= 1+\bar{\xi} \psi = e^{\bar{\xi} \psi}
    \quad \blacksquare
\end{align*}
$$

## Trace

The trace of a bosonic operator $O$ (made of product of an even number of fermion operators) can be expressed as the integral

<div class="result">

**Trace of bosonic operators:**

$$
\operatorname{Tr} O
= \int d\bar{\psi}\,d\psi
\exp (-\bar{\psi} \psi) \amp{-\bar{\psi}}{O}{\psi}
$$

</div><br>

Notice the *additional minus sign* compared to the boson case. 

*Proof*: 

$$
\begin{align*}
    \text{RHS} &= \int d\bar{\psi}\,d\psi \,
    (1 - \bar{\psi} \psi) \Big[
        (\bra{0} + \bra{1} \bar{\psi}) O
        (\ket{0} - \psi \ket{1})
    \Big]
    \\
    &= \int d\bar{\psi}\,d\psi \,
    (1 - \bar{\psi} \psi) \Big[
        \amp{0}{O}{0} - \psi \amp{0}{O}{1}
        + \bar{\psi} \amp{1}{O}{0}
        - \bar{\psi} \psi \amp{1}{O}{1}
    \Big]
    \\
    &= \int d\bar{\psi}\,d\psi \,
    \Big[
        1 \times (- \bar{\psi} \psi \amp{1}{O}{1})
        + (-\bar{\psi} \psi) \times \amp{0}{O}{0} 
    \Big]
    \\
    &= \amp{1}{O}{1} + \amp{0}{O}{0} = \operatorname{Tr} O = \text{LHS}
    \quad \blacksquare
\end{align*}
$$

## Coherent State Path Integral for Fermions

Similar to the boson case, the partition function for a fermion system can be split into the product of many pieces, and identities are inserted to obtain the path integral representation:

$$
\begin{align*}
    Z &= \prod_{n=1}^N \int 
    d\bar{\psi}_n \, d\psi_n
    \exp (-\bar{\psi}_n \psi_n) 
    \amp{\bar{\psi}_{n}}{1 - \epsilon H(c^\dagger, c)}{\psi_{n-1}}
    \\
    &= \int D\bar{\psi} \, D\psi
    \prod_{n=1}^N \bigg[
        \exp (-\bar{\psi}_n \psi_n) 
        \exp (\bar{\psi}_n \psi_{n-1}) 
        \underbrace{
            [1 - \epsilon H(\bar{\psi}_n, \psi_{n-1})]
        }_{\approx \exp[-\epsilon H(\bar{\psi}_n, \psi_n)]}
    \bigg]
    \\
    &= \int D\bar{\psi}\, D\psi \exp \bigg\{
        \sum_{n=1}^N \bigg[
            - \bar{\psi}_n (\psi_n - \psi_{n-1})
            - \epsilon H(\bar{\psi}_n, \psi_n)
        \bigg]
    \bigg\}
\end{align*}
$$

Notice that for fermions the additional minus sign in the trace operation requires *anti-PBC* along the $\tau$-direction: 

$$
\psi_0, \bar{\psi}_0 = -\psi_N, -\bar{\psi}_N
\ \Rightarrow \ 
\psi(\tau) = -\psi(\tau + \beta)
$$ 

and we defined the integration measure

$$
D\bar{\psi} \, D\psi = \prod_{n=1}^N d\bar{\psi}_n d\psi_n
$$

Note that the eigenvalues $\psi_n$ can be interpreted as an (imaginary-)time dependent variable $\psi(\tau)$ at $\tau_n = n \beta/N$. Then

$$
\begin{align*}
    Z &\approx \int D\bar{\psi}\, D\psi \exp \bigg\{
        - \epsilon \sum_{n=1}^N \Big[
            \bar{\psi}_n \partial_\tau \psi_n
            + H(\bar{\psi}_n, \psi_n)
        \Big]
    \bigg\}
\end{align*}
$$

In the $N\to \infty$ limit, the summation becomes an integration of $\tau$ from 0 to $\beta$. We finally arrive at

<div class="result">

**Fermion partition function in path integral form:**

$$
\begin{align*}
    Z &= \int D\bar{\psi} \,D\psi \exp \bigg[
        - \int_0^\beta d\tau \, L[\bar{\psi}, \psi]
    \bigg]
    \\[1em]
    \text{with} \quad 
    L[\bar{\psi}, \psi]
    &= \bar{\psi}(\tau) \partial_\tau \psi(\tau) + H(\bar{\psi}(\tau), \psi(\tau))
\end{align*}
$$

</div><br>

<div class="remark">

*Remark*: If there are $n > 1$ types of bosons, simply treat $\psi$ as an $n$-dimensional column vector, and $\bar{\psi}$ as an $n$-dimensional row vector. 

</div><br>
