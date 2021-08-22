# Kubo Formula

Reference: [Wikipedia](https://en.wikipedia.org/wiki/Kubo_formula)

Consider a quantum system described by the (time independent) Hamiltonian $H_0$. Suppose now that an external perturbation $V(t)$ is applied very slowly, or suddenly turned on at some time $t_0$:

$$
H(t) = H_0 + V(t)
$$ 

Before turning on the perturbation, the ensemble average of a quantity $A$ is given by (working in the Heisenberg picture)

$$
\begin{align*}
    \expect{A}_0 &= \Tr \rho_0 A 
    \qquad \left(
        \rho_0 = \frac{1}{Z_0} e^{-\beta H_0}
    \right)
    \\
    &= \frac{1}{Z_0} \sum_n e^{-\beta E_n}
    \amp{n}{A}{n}
\end{align*}
$$

where $\ket{n}$ are eigenstates of $H_0$ with energies $E_n$. Here we have used $\amp{n}{A_H(t)}{n}$ as $\amp{n}{A}{n}$ when $H = H_0$, where $A$ is in Schrödinger picture. 

After turning on the perturbation, we assume that the system is weakly coupled to the heat bath (i.e. it will reach new equilibrium very slowly), so that the ensemble average is still performed with respect to the old distribution; but the values $\amp{n}{A}{n}$ will be replaced:

$$
\expect{A}(t) = \frac{1}{Z_0} 
\sum_n e^{-\beta E_n} \amp{n}{A_H(t)}{n}
$$

where $A_H(t)$ is the operator in the full Heisenberg picture. It can be related to the interaction picture $A_I(t)$ by (setting the reference time to $-\infty$, when there is still no perturbation)

$$
\begin{align*}
    A_H(t) &= U_I^\dagger(t,-\infty) A_I(t) U_I(t,-\infty)
    \\
    &\simeq \left[
        1 + i 
        \int_{-\infty}^t dt' \, V_I(t')
    \right] A_I(t) \left[
        1 - i 
        \int_{-\infty}^t dt' \, V_I(t')
    \right]
    \\
    &\simeq A_I(t) - i 
    \int_{-\infty}^t dt' \, [A_I(t), V_I(t')]
\end{align*}
$$

Here we keep terms up to first order in $V_I$. But we know that

$$
\amp{n}{A_I(t)}{n} = \amp{n}{A}{n}
$$

therefore

$$
\amp{n}{A_H(t)}{n}
= \amp{n}{A}{n}
- i \int_{-\infty}^t dt' \, 
\amp{n}{[A_I(t), V_I(t')]}{n}
$$

Now we can obtain the new expectation value of $A$ at time $t$:

<div class="result">

**Kubo formula:**

$$
\begin{align*}
    \delta\expect{A(t)}
    &= \expect{A(t)} - \expect{A}_0 
    \\
    &= - i \int_{-\infty}^t dt' \, 
    \expect{[A_I(t), V_I(t')]}_0
\end{align*}
$$

</div><br>

## Response Function

We can rewrite Kubo formula as (note that the upper limit of $t'$ is changed to $+\infty$)

$$
\delta\expect{A(t)} 
= \int_{-\infty}^{\infty} dt' \, 
\chi^R_{AV}(t - t')
$$

with the following definition (for an arbitrary operator $B$):

<div class="result">

**Retarded response function (Green's function):**

$$
\chi^R_{AB}(t - t') \equiv
- i 
\expect{[A_I(t), B_I(t')]}_0 \theta(t - t')
$$

</div><br>

The time-independence of $H_0$ ensures that $\chi$ depends only on the difference between $t$ and $t'$.  The introduction of $\theta(t - t')$ in $\chi^R$ means that the response (change of $\expect{A}$) only depends on perturbation from the past. 

## In Frequency Domain

Usually, the perturbation $V$ takes the following form:

$$
V(t) = \int d^3x' B(\mathbf{x}') f(\mathbf{x}',t)
$$

and the operator $A$ is a function of space coordinate $A(\mathbf{x})$. Then

$$
\begin{align*}
    \delta\expect{A(\mathbf{x},t)}
    &= - i \int dt' \, d^3x' \,
    \expect{[A_I(\mathbf{x},t), B_I(\mathbf{x}',t')]}_0
    \theta(t - t') f(\mathbf{x}', t')
    \\
    &= \int dt' \, d^3x' \,
    \chi^R_{AB}(\mathbf{x}, \mathbf{x}', t - t')
    f(\mathbf{x}',t')
\end{align*}
$$

where we defined

$$
\chi^R_{AB}(\mathbf{x}, \mathbf{x}', t - t')
= - i \expect{[
    A_I(\mathbf{x},t), B_I(\mathbf{x}',t')
]}_0 \theta(t - t')
$$

Now we Fourier transform to find the response of one Fourier component of $A$:

$$
\begin{align*}
    \delta \expect{A(\mathbf{x},\omega)} 
    &= \int dt \, e^{i\omega t} 
    \int dt' \, d^3x' \,
    \chi^R_{AB}(\mathbf{x}, \mathbf{x}', t - t')
    f(\mathbf{x}',t')
    \\
    &= \int dt \, dt' \, d^3x' \, 
    \frac{d\omega_1}{2\pi} \frac{d\omega_2}{2\pi}
    \\ &\qquad \times 
    e^{i\omega t} e^{-i\omega_1(t - t')} 
    \chi^R_{AB}(\mathbf{x}, \mathbf{x}', \omega_1)
    e^{-i\omega_2 t'} f(\mathbf{x}',\omega_2)
\end{align*}
$$

Note that the integration over $t$ and $t'$ gives $(2\pi) \delta(\omega - \omega_1)$ and $(2\pi) \delta(\omega_1 - \omega_2)$, respectively. Thus we finally have

<div class="result">

**Kubo formula in frequency domain:**

$$
\begin{align*}
    \delta \expect{A(\mathbf{x},\omega)} 
    &= \int d^3x' \,
    \chi^R_{AB}(\mathbf{x},\mathbf{x}', \omega)
    f(\mathbf{x}',\omega)
\end{align*}
$$

</div><br>

## Translation Invariant Systems

For translation invariant systems, the response function $\chi^R_{AB}$ must only depends on $\mathbf{x} - \mathbf{x}'$. Mathematically, by Fourier transform both $A(\mathbf{x})$ and $B(\mathbf{x})$:

$$
\begin{align*}
    \chi^R_{AB}(\mathbf{x} - \mathbf{x}', t - t')
    &= - i \int \frac{d^3k}{(2\pi)^3}
    \frac{d^3k'}{(2\pi)^3} \, 
    e^{i\mathbf{k} \cdot \mathbf{x}}
    e^{i\mathbf{k}' \cdot \mathbf{x}'}
    \\ &\qquad \quad \times
    \expect{[
        A_I(\mathbf{k},t), B_I(\mathbf{k}',t')
    ]}_0 \theta(t - t')
\end{align*}
$$

we see that the only way to achieve translation invariance is requiring

$$
\expect{[
    A_I(\mathbf{k},t), B_I(\mathbf{k}',t')
]}_0
= \expect{[
    A_I(\mathbf{k},t), B_I(-\mathbf{k},t')
]}_0 (2\pi)^3 \delta^3(\mathbf{k} + \mathbf{k}')
$$

Then

$$
\begin{align*}
    \chi^R_{AB}(\mathbf{x} - \mathbf{x}', t - t')
    &= - i \int \frac{d^3k}{(2\pi)^3}
    e^{i\mathbf{k} \cdot (\mathbf{x} - \mathbf{x}')}
    \\ &\qquad \quad \times
    \expect{[
        A_I(\mathbf{k},t), B_I(-\mathbf{k},t')
    ]}_0 \theta(t - t')
\end{align*}
$$

from which we get the Fourier component of $\chi^R_{AB}$:

$$
\begin{align*}
    \chi^R_{AB}(\mathbf{k}, t - t')
    &= - i \expect{[
        A_I(\mathbf{k},t), B_I(-\mathbf{k},t')
    ]}_0 \theta(t - t')
\end{align*}
$$

<div class="remark">

*Remark*: Usually the operators $B$ is Hermitian. After Fourier transform, we obtain

$$
\begin{align*}
    B^\dagger(\mathbf{x}) 
    &= \int \frac{d^3k}{(2\pi)^3} 
    e^{i\mathbf{k} \cdot \mathbf{x}} 
    B^\dagger(\mathbf{k})
    = \int \frac{d^3k}{(2\pi)^3} 
    e^{-i\mathbf{k} \cdot \mathbf{x}} 
    B(\mathbf{k})
    \\ &\Downarrow \\
    B(-\mathbf{k}) &= B^\dagger(\mathbf{k})
    \\[0.5em]
    \chi^R_{AB}(\mathbf{k}, t - t')
    &= - i \expect{[
        A_I(\mathbf{k},t), B_I^\dagger(\mathbf{k},t')
    ]}_0 \theta(t - t')
\end{align*}
$$

</div><br>

One can then further transform the time to frequency:

$$
\begin{align*}
    \chi^R_{AB}(\mathbf{k}, \omega)
    &= - i \int_{-\infty}^\infty dt \,
    e^{i\omega t} \expect{[
        A_I(\mathbf{k},t), B_I(-\mathbf{k},0)
    ]}_0 \theta(t)
    \\
    &= - i \int_0^\infty dt \,
    e^{i\omega t} \expect{[
        A_I(\mathbf{k},t), B_I(-\mathbf{k},0)
    ]}_0
\end{align*}
$$
