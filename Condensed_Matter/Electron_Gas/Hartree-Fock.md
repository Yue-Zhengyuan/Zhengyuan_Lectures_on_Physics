# Hartree-Fock Approximation

*Some constants:*

- Average occupied radius $r_s$

$$
\frac{1}{n}= \frac{V}{N}= \frac{4\pi  r_s^3}{3} \Longrightarrow  r_s= \left(\frac{3}{4\pi  n}\right)^{1/3}
$$

- Bohr radius

$$
a_0= \frac{\hbar ^2}{m e^2}
$$

- Fermi wave vector for degenerate electron gas (3D)

$$
k_F= \left(3\pi ^2n\right)^{1/3}= \left(\frac{9\pi}{4}\right)^{1/3}\frac{1}{r_s}
$$

## Derivation in First Quantization

For a system of interacting electrons in a lattice of positive ions, the
*many-body* Hamiltonian is

$$
H= \sum_{a=1}^N \left(\frac{1}{2m}p_a^2+ \sum_R \frac{-Z e^2}{\left| x_a-R\right|}\right)+ \frac{1}{2}\sum_{a\neq b} \frac{e^2}{|x_a-x_b|
}
$$

The Hartree-Fock approximation is a variational method, which relies on
the fact that for a time-independent Hamiltonian $H$:

$$
\expect{H}_{\Psi}
= \frac{\amp{\Psi}{H}{\Psi}}{\braket{\Psi}{\Psi}}
\overset{\left\{\psi_n\right\} \text{orthonormal}}{\longrightarrow
}\langle \Psi |H|\Psi \rangle
$$

is minimized by the ground-state wave function. To get an approximate solution of the ground-state energy, we construct $\Psi$ of a certain
form, and minimize over its parameters.

A general $N$ electron state that respect the exchange property should be written as the **Slater determinant**:

$$
\begin{align*}
    \Psi (q_1, ... ,q_N)
    &= \frac{1}{\sqrt{N!}}\det
    \begin{pmatrix}
        \psi_1(q_1) & \psi_1(q_2) & \cdots & \psi_1(q_N) \\
        \psi_2(q_1) & \psi_2(q_2) & \cdots & \psi_2(q_N) \\
        \vdots  & \vdots  & \cdots & \vdots  \\
        \psi_N(q_1) & \psi_N(q_2) & \cdots & \psi_N(q_N) 
    \end{pmatrix}
    \\
    &= \frac{1}{\sqrt{N!}}\sum_{\mathcal{P}} (-1)^{\text{sgn}(\mathcal{P})}\psi_1\left(q_{\mathcal{P}(1)}\right) ... \psi_N\left(q_{\mathcal{P}(N)}\right)
\end{align*}
$$

Here $q\equiv (x,s)$ represents both the coordinate and the spin of an electron. The subscript of $\psi_n$ refers to both the spin and other quantum numbers (e.g. the orbital angular momentum).

Then we can minimize $\langle H\rangle_{\Psi}$ with respect to the single-electron wave functions $\{\psi_n\}$. These trial wave functions are assumed to be *orthonormal* in the sense that

$$
\int d^3q \, \psi_m^*(q)\psi_n(q)
\equiv \sum_s \int d^3x \,\psi_m^*(x,s)\psi_n(x,s)
= \delta_{m n}
$$

The integration over $q$ should be understood as summation over spin $s$ and integration over coordinates $x$. In the following, we shall write $\psi_n\left(q_a\right)$ simply as $\psi_n(a)$.

### Mathematical Preparations

To evaluate $\langle \Psi |H|\Psi \rangle$, we first list some formulas that will be used later. For any *symmetric* operator $F$ (invariant under exchange of two particles) and two Slater determinants $\Psi ,\Psi'$, we can verify that

$$
\begin{align*}
    &\expect{\Psi |F|\Psi'} 
    \\
    &= \frac{1}{N!}\int d^{3N}q\, \det 
    \begin{pmatrix}
        \psi_1^*(1) & \cdots & \psi_1^*(N) \\
        \vdots  & \ddots & \vdots  \\
        \psi_N^*(1) & \cdots & \psi_N^*(N)
    \end{pmatrix}F \det 
    \begin{pmatrix}
        \psi_1^{\prime}(1) & \cdots & \psi_1^{\prime}(N) \\
        \vdots  & \ddots & \vdots  \\
        \psi_N^{\prime}(1) & \cdots & \psi_N^{\prime}(N)
    \end{pmatrix}
    \\
    &= \int d^{3N}q\, \psi_1^*(1) ... \psi_N^*(N)F \det 
    \begin{pmatrix}
        \psi_1^{\prime}(1) & \cdots & \psi_1^{\prime}(N) \\
        \vdots  & \ddots & \vdots  \\
        \psi_N^{\prime}(1) & \cdots & \psi_N^{\prime}(N)
    \end{pmatrix}
\end{align*}
$$

Applying this to one-body symmetric operators, we obtain

$$
\begin{align*}
    &\expect{\Psi \left|\sum_a f_a\right|\Psi} 
    \\
    &= \sum_a \int d^{3N}q\, \psi_1^*(1) ... \psi_N^*(N)f_a \sum_{\mathcal{P}} (-1)^{\text{sgn}(\mathcal{P})}\psi
    _1(\mathcal{P}(1)) ... \psi_N(\mathcal{P}(N))
\end{align*}
$$

Due to the orthonormality of the electron wave functions, the only $\mathcal{P}$ that results in nonzero integral is the *identity permutation*. Then

$$
\left\langle \Psi \left|\sum_a  f_a\right|\Psi \right\rangle = \sum_a \int d^3q \,_a\psi_a^*(a)f_a\psi_a(a)
= \sum_a \int d^3q \,_1 \psi_a^*(1)f_1\psi_a(1)
$$

Similarly, for two-body symmetric operators

$$
\left\langle \Psi \left|\sum_{a\neq b}  g_{a b}\right|\Psi \right\rangle = \sum_{a\neq b} \int d^3q \,_1d^3q_2\psi_a^*(1)\psi_b^*(2)g_{12}\left[\psi
_a(1)\psi_b(2)- \psi_a(2)\psi_b(1)\right]
$$

To make the spin variable explicit, the formula for two-body operators
can be written as

$$
\expect{\Psi \left|\sum_{a\neq b}  g_{a b}\right|\Psi} 
= \sum_{a\neq b} \int d^3x \,_1d^3x_2\psi_a^*(1)\psi_b^*(2)g_{12}\left[\psi
_a(1)\psi_b(2)- \delta \left(s_a,s_b\right)\psi_a(2)\psi_b(1)\right]
$$

The first term is called the **direct (Hartree) term**, and the second term is called the **exchange (Fock) term**. The $i\neq j$ constraint is not needed here, because the direct and the
exchange terms cancel out when $i=j$.

#### The Calculation

In the many-body Hamiltonian, we recognize

$$
\begin{align*}
    f_a &= \frac{1}{2m}p_a^2
    + \sum_R \frac{-Z e^2}{|x_a-R|}
    \\
    g_{a b} &= \frac{1}{2}\frac{e^2}{|x_a-x_b|}
\end{align*}
$$

Then

$$
\begin{align*}
    \expect{H}_\Psi
    &= \sum_a \int d^3x \, \psi_a^*(x)\left(- \frac{\hbar ^2}{2m}\nabla ^2+U^{\text{ion}}(x)\right)\psi_a(x)\\
    &\quad
    + \frac{1}{2}\sum_{a, b} \int d^3x \,d^3x'\psi_a^*(x)\psi_b^*\left(x'\right)\frac{e^2}{|x-x'|}\psi_a(x)\psi_b\left(x'\right)\\
    &\quad
    - \frac{1}{2}\sum_{a, b} \int d^3x \,d^3x'\psi_a^*(x)\psi_b^*\left(x'\right)\frac{e^2}{|x-x'|}\delta \left(s_a,s_b\right)\psi_a\left(x'\right)\psi
    _b(x)
\end{align*}
$$

### Hartree-Fock Equation

Minimizing $\langle H\rangle_{\Psi}$ with respect to $\psi_n^*$ under the normalization constraint

$$
\int d^3q \, \psi_n^*(q)\psi_n(q)=1
\quad (\text{with Lagrange multiplier} \ \epsilon_n)
$$

We obtain the **Hartree-Fock equation**:

$$
- \frac{\hbar ^2}{2m}\nabla ^2\psi_n(x)+U^{\text{ion}}(x)\psi_n(x)+U^{\text{el}}(x)\psi_n(x)- \underbrace{\sum_i \int d^3x' \,\frac{e^2}{\left|
x-x'\right|}\psi_i^*\left(x'\right)\psi_n\left(x'\right)\psi_i(x)\delta \left(s_n,s_i\right)}_{\text{exchange term}}= \epsilon_n\psi_n(x)
$$

where

$$
U^{\text{el}}(x)\equiv \sum_{\text{other} a} \frac{e^2}{|x-x_a|}\to e^2\int d^3x' \,\frac{\sum_{ i} \psi_i^*\left(x'\right)\psi_i\left(x'\right)}{\left|
x-x'\right|}
$$

In an actual solid, 

$$
U^{\text{ion}}+U^{\text{el}}=0
$$

then only the exchange term survives.

### Fourier Component of Energy

We use the plane waves as the basis functions:

$$
\psi_n(x)= \exp \left(i k_n\cdot x\right)
$$

Then (omitting the subscript of $k_n$; summation carried over $s_n=s_i$)

$$
\frac{\hbar ^2k^2}{2m}\exp (i k\cdot x)- \sum_i \int d^3x' \,\frac{e^2}{|x-x'|}\exp \left(i k \cdot x'\right)\exp \left(i k_i\cdot \left(x-x'\right)\right)= \epsilon
(k)\exp (i k\cdot x)
$$

Summation over occupied levels $i$ is just over $k'<k_F$. Thus, renaming $k_i\to k'$, we have

$$
\begin{align*}
    \epsilon (k)
    &= \frac{\hbar ^2k^2}{2m}- \sum_{k'<k_F} \int d^3x' \,\frac{e^2}{|x-x'|}
    e^{-i(k-k')\cdot (x-x')}\\
    &\to \frac{\hbar ^2k^2}{2m}- \int_{k'<k_F}\frac{d^3k'}{(2\pi)^3}\underbrace{
        \int d^3x' \,\frac{e^2}{|x-x'|}
        e^{-i(k-k')\cdot(x-x')}
   }_{\text{Fourier transform}}
\end{align*}
$$

Using the Fourier transform of the Coulomb potential

$$
V(r)= \frac{e^2}{r}\leftrightarrow V(k)= \frac{4\pi  e^2}{k^2}
$$

i.e.

$$
\frac{4\pi  e^2}{k^2}= \int d^3x \, \frac{e^2}{r}e^{-i k\cdot x}
$$

We obtain

$$
\epsilon (k)= \frac{\hbar ^2k^2}{2m}- \int_{k'<k_F}\frac{d^3k'}{(2\pi)^3}\frac{4\pi  e^2}{\left| k-k'\right| ^2}
$$

Setting

$$
F(x)\equiv 1+ \frac{1-x^2}{2x}\ln \left| \frac{1+x}{1-x}\right|
$$

we finally have

$$
\epsilon (k)= \frac{\hbar ^2k^2}{2m}
- \frac{k_Fe^2}{\pi}F\left(\frac{k}{k_F}\right)
$$

#### Appendix: Evaluation of the Integral

To do the integration easily, we use spherical polar coordinates, and
choose $z$ axis to be in the same direction of $k$:

$$
\begin{align*}
    I &\equiv 
    \int_{k'<k_F}\frac{d^3k'}{(2\pi)^3}\frac{4\pi  e^2}{\left| k-k'\right| ^2}
    \\
    &= \int_{k'<k_F}
    \frac{k'^2 \sin \theta  dk'd\theta d\varphi}{(2\pi)^3}\frac{4\pi  e^2}{\left(k'\sin \theta \right)^2+ \left(k'\cos
    \theta -k\right)^2}
    \\
    &= \frac{e^2}{\pi}\int_0^{k_F}dk'\int_0^{\pi} d\theta  
    \frac{k'^2 \sin \theta}{k'^2 -2k k'\cos \theta +k^2}
    \\
    &= \frac{e^2}{\pi}\int_0^{k_F}dk'\int_0^{\pi} d\theta  
    \frac{k'^2 \sin \theta}{k'^2-2k k'\cos \theta +k^2}
\end{align*}
$$

Setting $u= \cos \theta$, then

$$
\begin{align*}
    I &= \frac{e^2}{\pi}\int_0^{k_F}dk'
    k'^2 \int_{-1}^1 du 
    \frac{1}{k'^2-2k k'u+k^2}\\
    &= \frac{e^2}{k \pi}\int_0^{k_F}dk'\, k'\ln \abs{\frac{k'+k}{k'-k}}
\end{align*}
$$

Integrate by parts:

$$
\begin{align*}
    &\int_0^{k_F} dk'\, k'
    \ln \abs{\frac{k'+k}{k'-k}}
    \\
    &= \frac{1}{2}\int_0^{k_F}d\left(k'^2\right)
    \ln \abs{\frac{k'+k}{k'-k}}
    \\
    &= \left[
        \frac{k'^2}{2}
        \ln \abs{\frac{k'+k}{k'-k}} 
    \right]_{k'=0}^{k'=k_F}
    - \frac{1}{2}\int_0^{k_F} k'^2 \, d\left[
        \ln \abs{\frac{k'+k}{k'-k}} 
    \right]
    \\
    &= \frac{k_F^2}{2} \ln \abs{\frac{k_F+k}{k_F-k}} 
    + k\int_0^{k_F}dk'\frac{k'^2}{k'^2-k^2} 
    \\
    &= \frac{k_F^2}{2}\ln \abs{\frac{k_F+k}{k_F-k}} 
    + k \left(
        k_F- \frac{k}{2}
        \ln \abs{\frac{k_F+k}{k_F-k}} 
    \right)
    \\
    &= k k_F + \frac{k_F^2-k^2}{2}
    \ln \abs{\frac{k_F+k}{k_F-k}}
\end{align*}
$$

Then, setting 

$$
x\equiv k\left/k_F\right.
$$

we obtain

$$
\begin{align*}
    I &= \frac{e^2}{\pi} \left[
        k_F + \frac{1}{2} \left(\frac{k_F^2}{k}-k\right)
        \ln \abs{\frac{k_F+k}{k_F-k}} 
    \right]
    \\
    &= \frac{k_Fe^2}{\pi} \left[
        1+ \frac{1}{2} \left(\frac{k_F}{k}- \frac{k}{k_F}\right)
        \ln \abs{\frac{1+k/k_F}{1-k/k_F}}
    \right]
    \\
    &= \frac{k_Fe^2}{\pi} \left[
        1+ \frac{1}{2} \left(\frac{1}{x}-x\right)
        \abs{\frac{1+x}{1-x}}
    \right]
\end{align*}
$$

### 2. Single-Electron Energy Levels



