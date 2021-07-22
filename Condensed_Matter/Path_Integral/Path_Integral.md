# Path Integral

## Real-Time Evolution Operator

### Decomposition of Evolution

Recall that the real-time evolution operator is given by the time-ordered exponential

$$
U(t,t_0) = T{\left[ \exp{
    \left(
        -i \int_{t_0}^t dt' \, H(t')
    \right)
} \right]}
$$

which can be decomposed into $N \to \infty$ pieces using the property $U(t_2,t_1) U(t_1,t_0) = U(t_2,t_0)$ :

$$
\begin{align*}
    U(t,t_0)
    &= U(t_N,t_{N-1}) \cdots U(t_1,t_0)
    \\ \text{with} \quad
    t_n &\equiv t_0 + n \epsilon, \quad
    \epsilon = \frac{t - t_0}{N}
\end{align*}
$$

For each small piece $U(t_{n+1},t_n)$, the Hamiltonian $H$ can be approximated by the value at $t_{n}$; then the time ordering can be omitted:

$$
U(t_{n+1},t_n) \approx e^{-iH(t_{n}) \epsilon}
$$

Then we can insert identities into the product of all the $U(t_{n+1},t_n)$ operators: 

- For *first-quantized* Hamiltonian, usually we use the resolution of identity in terms of position states or momentum states:

$$
\int dx \, \ket{x} \bra{x} = 1, \quad
\int \frac{dp}{2\pi} \ket{p} \bra{p} = 1
\quad \Big( \braket{x}{p} = e^{ipx} \Big)
$$

- For *second-quantized* Hamiltonian (in terms of creation/annihilation operators), we shall use resolution of identity in terms of **coherent states**, which will not be discussed now.

### Propagator

Let us evaluate the matrix element of the time evolution operator between two position states (called the **propagator**):

$$
U(x,t;x_0,t_0) \equiv \amp{x}{U(t,t_0)}{x_0}
$$

with the Hamiltonian in the classical (first-quantized and time independent) form

$$
H(p,x) = \frac{1}{2m}p^2 + V(x)
$$

With the decomposition of evolution operator, we obtain

$$
\begin{align*}
    &\amp{x}{U(t,t_0)}{x_0}
    \\
    &= \langle x|U(t_N,t_{N-1}) \cdots U(t_1,t_0)|x_0\rangle
    \\
    &= \int dx_{N-1} \cdots dx_1
    \langle x_N|e^{-iH\epsilon}|x_{N-1}\rangle
    \cdots 
    \langle x_1|e^{-iH\epsilon}|x_0\rangle 
    \\
    &=\int \prod_{n=1}^{N-1} dx_n \prod_{j=0}^{N-1} 
    \langle x_{j+1}|e^{-iH\epsilon}|x_j\rangle
\end{align*}
$$

Here we introduced $\ket{x_N} \equiv \ket{x}$. 

### Path Integral in Phase Space

The propagator in the $n$th ($n = 0,..,N-1$) time step is

$$
\begin{align*}
    &\langle x_{n+1}|e^{-iH\epsilon}|x_n\rangle 
    \\
    &\approx \langle x_{n+1}|1-iH(p,x)\epsilon|x_n\rangle 
    \\
    &= \int \frac{dp_n}{2\pi}
    \langle x_{n+1}|1-iH(p,x)\epsilon|p_n\rangle 
    \langle p_n|x_n \rangle 
    \\
    &= \int \frac{dp_n}{2\pi}
    [1-i H(p_n,x_n) \epsilon]
    \langle x_{n+1}|p_n \rangle \langle p_n|x_n \rangle 
    \\
    &= \int \frac{dp_n}{2\pi}
    [1-i H(p_n,x_n) \epsilon] 
    e^{i p_n(x_{n+1}-x_n)}
    \\
    &= \int \frac{dp_n}{2\pi}
    [1-i H(p_n,x_n) \epsilon] 
    e^{i p_n\dot{x}_n \epsilon}
    \\
    &\approx \int \frac{dp_n}{2\pi} 
    \exp \left[i \epsilon (
        p_n \dot{x}_n - H(p_n,x_n)
    ) \right]
\end{align*}
$$

where we introduced $\dot{x}_n = (x_{n+1} - x_n)/\epsilon$. Then

$$
\begin{align*}
    &\amp{x}{U(t,t_0)}{x_0}
    \\
    &= \int \underbrace{\bigg[
        \prod_{n=1}^{N-1} dx_n
        \prod_{n=0}^{N-1} \frac{dp_n}{2\pi}
    \bigg]}_{\equiv Dx \, Dp}
    \prod_{j=0}^{N-1} \exp [
        i \epsilon  (p_j \dot{x}_j - H(p_j,x_j))
    ]
\end{align*}
$$

In the $\epsilon \to 0$ limit, we obtain

<div class="result">

**Phase space path integral of $U(t,t_0)$:**

$$
\begin{align*}
    \amp{x}{U(t,t_0)}{x_0}
    &= \int Dx \, Dp \, e^{iS}
    \\
    \text{Action:} \quad
    S &= \int_{t_0}^t 
    dt' \, \Big[
        p \dot{x} - H(p,x)
    \Big]
\end{align*}
$$

</div><br>

### Path Integral in Position Space

It turns out that when $H$ has the classical kinetic + potential energy form, the integration over momentum can be evaluated

$$
\begin{align*}
    &\langle x_{n+1}|e^{-iH\epsilon}|x_n\rangle 
    \\
    &\approx \int \frac{dp_n}{2\pi} 
    \exp \left[i \epsilon (
        p_n \dot{x}_n - H(p_n,x_n)
    ) \right]
    \\
    &= \exp[- i\epsilon V(x_n)] \times
    \int \frac{dp_n}{2\pi} 
    \exp \left[i \epsilon \left(
        - \frac{p_n^2}{2m} + p_n \dot{x}_n 
    \right) \right]
\end{align*}
$$

This is a Gaussian integral. To ensure convergence, we have to assume that $\epsilon$ has a very small negative imaginary part ($\epsilon \to \epsilon + i0^-$). Then

$$
\begin{align*}
    \int \frac{dp_n}{2\pi} 
    \exp \left[i \epsilon \left(
        - \frac{p_n^2}{2m} + p_n \dot{x}_n 
    \right) \right]
    = \sqrt{\frac{m}{2\pi i\epsilon}} \exp \bigg[
        \frac{1}{2} m\dot{x}_n^2 \times i \epsilon
    \bigg]
\end{align*}
$$

Therefore

$$
\begin{align*}
    &\amp{x}{U(t,t_0)}{x_0}
    \\&=\int \prod_{n=1}^{N-1} dx_n \prod_{j=0}^{N-1} 
    \sqrt{\frac{m}{2\pi i\epsilon}} \exp \bigg[
        i \epsilon \bigg(
            \underbrace{
                \frac{1}{2} m\dot{x}_n^2 - V(x_n)
            }_{\text{Lagrangian} \ L[x,\dot{x}]}
        \bigg) 
    \bigg]
\end{align*}
$$

Define the integration measure

$$
Dx \equiv \lim_{N \to \infty} \bigg(
    \frac{m}{2\pi i \epsilon}
\bigg)^{N/2} \int \prod_{n=1}^{N-1} dx_n
$$

In the continuum limit, we obtain

<div class="result">

**Position space path integral of $U(t,t_0)$:**

$$
\begin{align*}
    \amp{x}{U(t,t_0)}{x_0}
    &= \int Dx \, Dp \, e^{iS}
    \\
    \text{Action:} \quad
    S &= \int_{t_0}^t 
    dt' \, L[x(t'), \dot{x}(t')]
    \\
    \text{Lagrangian:} \quad
    L &= \frac{1}{2} m\dot{x}^2 - V(x)
\end{align*}
$$

</div><br>

## Euclidean Path Integral in Imaginary Time

<div class="remark">
<center>

*In this section $H$ is assumed to be time-independent,<br>as is the case for equilibrium statistical physics.*

</center>
</div><br>

The density matrix $\rho$ in statistical physics can be interpreted as *imaginary* time evolution operator:

$$
\rho = e^{-\beta H} = e^{-i H (-i\beta)} = U(-i\beta,0)
$$

We then define the imaginary time $\tau$ as

$$
\tau \equiv it = e^{i\pi/2} t
\qquad (t = -i\tau)
$$

which can be regarded as rotating $t$ counter-clockwise by $\pi/2$ in the complex plane (called a **Wick rotation**). The imaginary time evolution operator is then

$$
U(\tau,\tau_0) \quad \Rightarrow \quad
\rho = U(\beta,0)
$$

The time derivative will be replaced by $\tau$-derivative:

$$
\frac{\partial}{\partial t} = \frac{\partial}{-i \, \partial \tau}
= i \frac{\partial}{\partial \tau}
$$

Let us also divide $\beta$ into $N \to \infty$ pieces:

$$
\epsilon \equiv \frac{\beta}{N}, \quad 
\tau_n \equiv n \epsilon \ (n = 0,1,...,N)
$$

Then, in analogy with the real time case, we obtain

$$
\begin{align*}
    &\amp{x}{\rho}{x_0} = \amp{x}{U(\beta,0)}{x_0}
    \\
    &= \langle x|U(\tau_N,\tau_{N-1}) \cdots U(\tau_1,\tau_0)|x_0\rangle
    \\
    &=\int \prod_{n=1}^{N-1} dx_n \prod_{j=0}^{N-1} 
    \langle x_{j+1}|e^{-\epsilon H}|x_j\rangle

    \\~\\

    &\langle x_{n+1}|e^{-\epsilon H}|x_n\rangle 
    \\
    &\approx \int \frac{dp_n}{2\pi}
    [1 - \epsilon H(p_n,x_n)] 
    e^{i p_n\dot{x}_n \epsilon}
    \\
    &\approx \int \frac{dp_n}{2\pi} 
    \exp \left[
        -\epsilon H(p_n,x_n)
        + i \epsilon p_n\dot{x}_n
    \right]

\end{align*}
$$

Note that $\dot{x}_n$ now refers to $\tau$-derivative. Then we obtain in the phase space

<div class="result">

**Phase space path integral of $\rho = U(\beta,0)$:**

$$
\begin{align*}
    \amp{x}{\rho}{x_0}
    &= \int Dx \, Dp \, e^{-S_E}
    \\
    \text{(Euclidean) Action:} \quad
    S_E &= \int_0^\beta d\tau \, \Big[
        -i p \, \partial_\tau x + H(p,x)
    \Big]
\end{align*}
$$

</div><br>

Alternatively, we can evaluate the integration over $p$:

$$
\begin{align*}
    &\langle x_{n+1}|e^{-\epsilon H}|x_n\rangle 
    \\
    &\approx \int \frac{dp_n}{2\pi} 
    \exp \left[
        -\epsilon H(p_n,x_n)
        + i \epsilon p_n\dot{x}_n
    \right]
    \\
    &= \exp[-\epsilon V(x_n)]
    \int \frac{dp_n}{2\pi} 
    \exp \left[
        -\epsilon \left(\frac{p_n^2}{2m}\right)
        + i \epsilon p_n\dot{x}_n
    \right]
    \\
    &= \sqrt{\frac{m}{2\pi \epsilon}} \exp \left[
        -\epsilon \left(
            \frac{1}{2} m \dot{x}_n^2 + V(x_n)
        \right)
    \right]
\end{align*}
$$

Contrary to the real-time case, this Gaussian integration is well-defined. Define the integration measure

$$
Dx \equiv \lim_{N \to \infty} \bigg(
    \frac{m}{2\pi \epsilon}
\bigg)^{N/2} \int \prod_{n=1}^{N-1} dx_n
$$

In the continuum limit, we obtain

<div class="result">

**Position space path integral of $\rho = U(\beta,0)$:**

$$
\begin{align*}
    \amp{x}{\rho}{x_0}
    &= \int Dx \, Dp \, e^{-S_E}
    \\
    \text{(Euclidean) Action:} \quad
    S_E &= \int_0^\beta d\tau \, L_E[x(\tau), \partial_\tau{x}(\tau)]
    \\
    \text{(Euclidean) Lagrangian:} \quad
    L_E &= \frac{1}{2} m (\partial_\tau x)^2 + V(x)
\end{align*}
$$

</div><br>
