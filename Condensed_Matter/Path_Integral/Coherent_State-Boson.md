# Boson Coherent State

## Coherent State: Eigenstate of Annihilation Operator

The eigenstate of the (boson) annihilation operator bears a special name:

<div class="result">

**Boson coherent state:**

$$
a \ket{z} =z \ket{z}, 
\quad
z \in \mathbb{C}
$$

</div><br>

A generalization is to introduce *multiple kinds* of bosons into the system. Let the annihilation operator of the $i$th kind of be $a_i$. Because the annihilation operators of different kinds of bosons *commute*, they have a common set of eigenstates labelled by $z_1, z_2, ... \in \mathbb{C}$:

$$
a_1 a_2 \cdots a_n 
|z_1z_2 \cdots z_n\rangle 
= z_1z_2 \cdots z_n
| z_1z_2 \cdots z_n\rangle
$$

Its Hermitian conjugate is

$$
\langle z_1z_2 \cdots z_n|
a_n^\dagger \cdots a_2^\dagger a_1^\dagger
=\langle z_1z_2 \cdots z_n|
\bar{z}_n \cdots \bar{z}_2 \bar{z}_1
$$

## Building Coherent State from Vacuum

We can obtain the coherent state from the vacuum state $\ket{0}$ using the following operation

<div class="result">

**Building coherent state from vacuum:**

$$
\begin{align*}
    \ket{z}
    &= \exp (z a^\dagger)\ket{0}
    = \sum_n \frac{(z a^\dagger)^n}{n!}\ket{0} 
    \\
    \bra{z}
    &= \bra{0} \exp (a \bar{z})
    = \sum_n  \bra{0}\frac{\left(a \bar{z}\right)^n}{n!}
\end{align*}
$$

</div><br>

*Proof*:

Expand the coherent state using the Fock space basis vectors :

$$
\begin{align*}
    \ket{z} 
    &= \sum_{n\geq 0}  c_n\ket{n} 
    \\
    \Rightarrow 
    a\ket{z} 
    &=\sum_{n\geq 0}  c_n(a\ket{n} )
    =\sum_{n\geq 1}  c_n\sqrt{n}|n-1\rangle 
    \\
    &=\sum_{n\geq 0}  c_{n+1}\sqrt{n+1}\ket{n}
\end{align*}
$$

Meanwhile

$$
a\ket{z} 
= z \ket{z} 
=\sum_{n\geq 0}  z c_n\ket{n}
$$

Therefore,

$$
z c_n = \sqrt{n+1}c_{n+1}
$$

By recursion, we find

$$
c_n = \frac{z}{\sqrt{n}}c_{n-1}
= \frac{z}{\sqrt{n}}\frac{z}{\sqrt{n-1}}c_{n-2}
= \cdots  
= \frac{z^n}{\sqrt{n!}}c_0
$$

Set $c_0 = 1$ (just a convenient choice of normalization). Using

$$
\ket{n} 
= \frac{a^\dagger}{\sqrt{n}}| n-1\rangle 
= \frac{a^\dagger}{\sqrt{n}}\frac{a^\dagger}{\sqrt{n-1}}| n-2\rangle 
= \cdots 
= \frac{(a^\dagger)^n}{\sqrt{n!}}\ket{0}
$$

we obtain

$$
\ket{z} 
= \sum_n  \frac{z^n}{\sqrt{n!}}\frac{(a^\dagger)^n}{\sqrt{n!}}\ket{0} 
= \sum_n  \frac{(z a^\dagger)^n}{n!}\ket{0} 
= \exp (z a^\dagger)\ket{0}
\quad \blacksquare
$$

<div class="remark">

*Remark*: If we have many kinds of bosons, the result is

$$
\ket{z} 
= \exp \bigg(\sum_k z_k a_k^\dagger \bigg)\ket{0}
$$

</div><br>

## Resolution of Identity

We now prove the central result to be used in the construction of coherent state path integral:

<div class="result">

**Over-completeness relation of boson coherent states:**

$$
\int \frac{d\bar{z}\,dz}{2\pi i}
\exp (-\bar{z} z) \ket{z} \bra{z} = 1
$$

</div><br>

<div class="remark">

*Remark*: The complex integration is just a fancy way of writing

$$
\begin{gathered}
    \int \frac{dx dy}{\pi}e^{-(x^2+y^2)}
    \ket{z} \bra{z}
    = 1
    \\
    \text{with} \quad
    z = x + i y, \quad 
    \bar{z} = x - i y \quad (x,y\in \mathbb{R})
\end{gathered}
$$

</div><br>

*Proof*:

We verify that for any two Fock space basis states $\ket{m}, \ket{n}$

$$
\amp{m}{
    \int \frac{dx \, dy}{\pi} e^{-(x^2 + y^2)}
}{z} \braket{z}{n}
=\delta_{m n}
$$

Recall that

$$
\ket{z} 
= \sum_{n\geq 0}  \frac{z^n}{\sqrt{n!}} \ket{n} ,
$$

Then

$$
\begin{align*}
    \text{LHS} 
    &=\int \frac{dx dy}{\pi} e^{-(x^2 + y^2)}
    \braket{m}{z} 
    \braket{z}{n} 
    \\
    &= \int \frac{dx dy}{\pi} e^{-(x^2 + y^2)}
    \frac{z^m}{\sqrt{m!}}
    \frac{\bar{z}^m}{\sqrt{n!}}
\end{align*}
$$

To evaluate this integral, we use the polar coordinates:

$$
z =r e^{i \theta}, \quad 
\bar{z}=r e^{-i \theta}
$$

Then

$$
\begin{align*}
    \text{LHS} 
    &= \int \frac{r \, dr \, d\theta}{\pi \sqrt{m!n!}}
    e^{-r^2 + i(m-n)\theta} r^{m+n}
    \\
    &=\frac{1}{\pi \sqrt{m!n!}}
    \int_0^{\infty} dr \, r^{m+n+1} e^{-r^2}
    \underbrace{
        \int_0^{2\pi} d\theta \, e^{i(m-n)\theta}
    }_{2\pi \delta_{mn}}
    \\
    &= \delta_{m n} \frac{2}{n!}
    \int_0^{\infty} dr \, r^{2n+1}e^{-r^2}
    \\
    &=\delta_{m n}\frac{2}{n!}\frac{\Gamma (n+1)}{2}
    =\delta_{m n}
    \quad \blacksquare
\end{align*}
$$

## Operators in Coherent State Representation

Since coherent states are eigenstates of the boson operator, finding the amplitudes of any second-quantized operators between two coherent states is easy.

<div class="result">

**Amplitudes between coherent states:**

For any normal ordered operator $\normord{A(a^\dagger, a)}$ and two coherent states $\ket{z}, \ket{w}$, 

$$
\amp{w}{\normord{A(a^\dagger,a)}}{z}
= e^{\bar{w}z} \normord{A(\bar{w},z)}
$$

In particular, when $A$ is the identity operator, we find the overlap between two coherent states

$$
\braket{w}{z} = e^{\bar{w}z}
$$

</div><br>

*Proof*:

$$
\braket{w}{z} 
= \amp{0}{e^{\bar{w} a} e^{z a^\dagger}}{0}
$$

Using the theorem (when $[A,B]$ is a $c$-number)

$$
e^A e^B = e^{[A,B]} e^B e^A
$$

We have

$$
\begin{align*}
    e^{\bar{w} a}e^{z a^\dagger}
    &= e^{\bar{w}z [a,a^\dagger]} e^{z a^\dagger} e^{\bar{w} a}
    = e^{\bar{w}z} e^{z a^\dagger} e^{\bar{w} a}
    \\
    \Rightarrow \quad
    \braket{w}{z} &= e^{\bar{w}z} 
    \amp{0}{e^{z a^\dagger} e^{\bar{w} a}}{0}
\end{align*}
$$

But $\bra{0}e^{z a^\dagger}=\bra{0}$ and $e^{\bar{w} a}\ket{0} =\ket{0}$, thus

$$
\braket{w}{z} =e^{\bar{w}z}
\quad \blacksquare
$$

## Trace

The trace of a bosonic operator $O$ can be expressed as the integral

<div class="result">

**Trace of bosonic operators:**

$$
\operatorname{Tr} O
= \int \frac{d\bar{z}\,dz}{2\pi i}
\exp (-\bar{z} z) \amp{z}{O}{z}
$$

</div><br>

which is the same as inserting an identity into a closed "spacetime loop".

## Coherent State Path Integral for Bosons

The partition function of a statistical model is given by

$$
Z = \operatorname{Tr} e^{-\beta H}
$$

The Hamiltonian $H(a^\dagger,a)$ is assumed to be normal-ordered. 

To obtain a path integral representation of $Z$, we divide $e^{-\beta H}$ into product of many small pieces:

$$
e^{-\beta H} = \prod_{n=1}^N e^{-\epsilon H}
\approx \prod_{n=1}^N (1 - \epsilon H), \quad 
\epsilon \equiv \frac{\beta}{N} \quad 
(N \to \infty)
$$

Between these small pieces, we insert identities in coherent state representation 

$$
\begin{align*}
    Z &= \prod_{n=1}^N \int 
    \frac{d\bar{z}_n \, dz_n}{2\pi i}
    \exp (-\bar{z}_n z_n) 
    \amp{z_{n}}{1 - \epsilon H(a^\dagger, a)}{z_{n-1}}
    \\
    &= \int D\bar{z} \, Dz
    \prod_{n=1}^N \bigg[
        \exp (-\bar{z}_n z_n) 
        \exp (\bar{z}_n z_{n-1}) 
        \underbrace{
            [1 - \epsilon H(\bar{z}_n, z_{n-1})]
        }_{\approx \exp[-\epsilon H(\bar{z}_n, z_n)]}
    \bigg]
    \\
    &= \int D\bar{z}\, Dz \exp \bigg\{
        \sum_{n=1}^N \bigg[
            - \bar{z}_n (z_n - z_{n-1})
            - \epsilon H(\bar{z}_n, z_n)
        \bigg]
    \bigg\}
\end{align*}
$$

Here $z_0, \bar{z}_0 = z_N, \bar{z}_N$, meaning periodicity in the $\tau$-direction 

$$
z(\tau) = z(\tau + \beta)
$$

and we defined the integration measure

$$
D\bar{z} \, Dz = \prod_{n=1}^N \frac{d\bar{z}_n dz_n}{2\pi i}
$$

Note that the eigenvalues $z_n$ can be interpreted as an (imaginary-)time dependent variable $z(\tau)$ at $\tau_n = n \beta/N$. Then

$$
\begin{align*}
    Z &\approx \int D\bar{z}\, Dz \exp \bigg\{
        - \epsilon \sum_{n=1}^N \Big[
            \bar{z}_n \partial_\tau z_n
            + H(\bar{z}_n, z_n)
        \Big]
    \bigg\}
\end{align*}
$$

In the $N\to \infty$ limit, the summation becomes an integration of $\tau$ from 0 to $\beta$. We finally arrive at

<div class="result">

**Boson partition function in path integral form:**

$$
\begin{align*}
    Z &= \int D\bar{z} \,Dz \exp \bigg[
        - \int_0^\beta d\tau \, L[\bar{z}, z]
    \bigg]
    \\[1em]
    \text{with} \quad 
    L[\bar{z}, z]
    &= \bar{z}(\tau) \partial_\tau z(\tau) + H(\bar{z}(\tau), z(\tau))
\end{align*}
$$

</div><br>

<div class="remark">

*Remark*: If there are $n > 1$ types of bosons, simply treat $z$ as an $n$-dimensional column vector, and $\bar{z}$ as an $n$-dimensional row vector. 

</div><br>
