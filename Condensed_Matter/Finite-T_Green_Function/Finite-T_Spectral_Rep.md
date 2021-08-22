# Spectral Representation at Finite-*T*

The zero-temperature Green's function can be generalized to finite temperature by replacing the ground state expectation value with the grand-canonical ensemble average:

<div class="result">

**(Time-ordered) Green's function at finite temperature:**

$$
\begin{align*}
    i \bar{G}_{\alpha \beta}(t - t')
    &= \expect{T[a_\alpha(t) c^\dagger_\beta(t')]} \\
    &= e^{\beta F} \Tr \left\{
        e^{-\beta H} T[a_\alpha(t) c^\dagger_\beta(t')]
    \right \}
\end{align*}
$$

</div><br>

## Lehmann Representation at Finite-*T*

Now we Fourier transform $\bar{G}$. As usual, we first separate the time dependence from the $c$ operators: expressing the trace as a summation over energy eigenstates $\ket{m}$ (this label implicitly includes the number of particles), we have

$$
\begin{align*}
    &\Tr \left\{
        e^{-\beta H} T[a_\alpha(t) c^\dagger_\beta(t')]
    \right \}
    = \sum_m \amp{m}{
        e^{-\beta H} T[a_\alpha(t) c^\dagger_\beta(t')]
    }{m}
    \\
    &= \sum_m e^{-\beta E_m}
    \amp{m}{
        a_{\alpha} e^{-iH(t - t')} 
        a^\dagger_{\beta}
    }{m} e^{i E_m (t - t')} \theta(t - t')
    \\ &\quad
    \pm \sum_m e^{-\beta E_m} \amp{m}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
        a_{\alpha}
    }{m} e^{i E_m (t' - t)} \theta(t' - t)
\end{align*}
$$

As in the zero-*T* case, we insert identities to deal with $e^{\pm iH(t-t')}$: 

$$
\begin{align*}
    &\amp{m}{
        a_{\alpha} e^{-iH(t - t')} 
        a^\dagger_{\beta}
    }{m}
    \\
    &= \sum_n \amp{m}{
        a_{\alpha} e^{-iH(t - t')} 
    }{n} \amp{n}{
        a^\dagger_{\beta}
    }{m}
    \\
    &= \sum_n e^{-iE_n(t - t')} \amp{m}{
        a_{\alpha}
    }{n} \amp{n}{
        a^\dagger_{\beta}
    }{m}

    \\[2em]

    &\amp{m}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
        a_{\alpha}
    }{m}
    \\
    &= \sum_n \amp{m}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
    }{n} \amp{n}{
        a_{\alpha}
    }{m}
    \\
    &= \sum_n e^{-iE_n(t' - t)} \amp{m}{
        a^\dagger_{\beta}
    }{n} \amp{n}{
        a_{\alpha}
    }{m}
\end{align*}
$$

Collecting these results, we obtain (setting $t - t' \to t$)

$$
\begin{align*}
    &i \bar{G}_{\alpha\beta}(t)
    \\
    &= e^{\beta F} \sum_{m,n} \bigg[
        e^{-\beta E_m} 
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        e^{- i(E_n - E_m)t} \theta(t)
        \\ &\qquad \qquad \quad
        \mp e^{-\beta E_n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        \amp{m}{a_{\alpha}}{n} 
        e^{-i(E_n - E_m)t} \theta(-t)
    \bigg]
\end{align*}
$$

Here we have secretly swapped the label $m,n$ for the second term in the summand. We note that the summand in both summations is nonzero when $\ket{n}$ has one more particle than $\ket{m}$ (i.e. $N_n = N_m + 1$). 

We can now Fourier transform: through a calculation parallel to the zero-*T* case

<div class="result">

**Green's function at finite temperature <br>(Lehmann representation):**

$$
\begin{align*}
    \bar{G}_{\alpha\beta}(E)
    &= e^{\beta F} \sum_{m,n} 
    \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\quad \times \bigg[
        \frac{e^{-\beta E_m}}
        {E - (E_n - E_m) + i\eta} 
        \mp \frac{e^{-\beta E_n}}
        {E - (E_n - E_m) - i\eta}
    \bigg]
\end{align*}
$$

</div><br>

<div class="remark">

*Remark*: If the basis $\alpha, \beta$ etc. are obtained from a conserved operator $A$ (i.e. $[H,A] = 0$), we can choose the states $\ket{n}$ as the common eigenstates of $H, A$. Then we may simply write

$$
\amp{m}{a_{\alpha}}{n} \amp{n}{a^\dagger_{\beta}}{m} 
= \delta_{\alpha \beta} |\amp{m}{a_\alpha}{n}|^2
$$

</div><br>

## Retarded and Advanced Green's Functions

In addition to the time-ordered Green's function, we also introduce two other kinds of Green's functions, which will appear in response theory:

<div class="result">

**Retarded and Advanced Green's functions:**

$$
\begin{align*}
    i \bar{G}^R_{\alpha \beta}(t - t')
    &= \theta(t - t') \expect{
        [a_\alpha(t), a^\dagger_\beta(t')]_{\mp}
    } \\
    i \bar{G}^A_{\alpha \beta}(t - t')
    &= - \theta(t' - t) \expect{
        [a_\alpha(t), a^\dagger_\beta(t')]_{\mp}
    } 
\end{align*}
$$

</div><br>

By similar calculations, one obtains

$$
\begin{align*}
    &i \bar{G}^R_{\alpha\beta}(t)
    \\
    &= e^{\beta F} \sum_{m,n} \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\qquad \qquad \qquad \times
    (e^{-\beta E_m} \mp e^{-\beta E_n})
    e^{-i(E_n - E_m)t} \theta(t)
    \\
    &i \bar{G}^A_{\alpha\beta}(t)
    \\
    &= e^{\beta F} \sum_{m,n} 
    \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\qquad \qquad \qquad \times
    (- e^{-\beta E_m} \pm e^{-\beta E_n})
    e^{-i(E_n - E_m)t} \theta(-t)
\end{align*}
$$

Their Fourier transforms are

<div class="result">

**Retarded/Advanced Green's function at finite temperature <br>(Lehmann representation):**

$$
\begin{align*}
    \bar{G}^R_{\alpha\beta}(E)
    &= e^{\beta F} \sum_{m,n} 
    e^{-\beta E_m} \frac{
        [1 \mp e^{-\beta (E_n - E_m)}]
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
    }{
        E - (E_n - E_m) + i\eta
    } \\
    \bar{G}^A_{\alpha\beta}(E)
    &= e^{\beta F} \sum_{m,n} 
    e^{-\beta E_m} \frac{
        [1 \mp e^{-\beta (E_n - E_m)}]
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
    }{
        E - (E_n - E_m) - i\eta
    }
\end{align*}
$$

</div><br>

## Relation between Green's Functions

From the structure of $\bar{G}^{R/A}$, we define 

<div class="result">

**The spectral function:**

$$
S_{\alpha \beta}(E) 
= -2 \operatorname{Im} \bar{G}^R_{\alpha \beta}(E)
$$

or equivalently

$$
S_{\alpha \beta}(E) 
= +2 \operatorname{Im} \bar{G}^A_{\alpha \beta}(E)
$$

</div><br>

Using the Sokhotski–Plemelj theorem:

$$
\frac{1}{z \pm i\eta}
= \mathcal{P}\frac{1}{z} \mp i\pi \delta(z)
$$

we get the explicit expression for $S_{\alpha \beta}$:

$$
\begin{align*}
    S_{\alpha \beta}(E)
    &= e^{\beta F} (1 \mp e^{-\beta E})
    \sum_{m,n} e^{-\beta E_m} 
    \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\qquad \qquad \times
    (2\pi) \delta[E - (E_n - E_m)]
\end{align*}
$$

Let us now express the three kinds of Green's function in terms of $S$. 

- **Retarded/Advanced Green's function**

    The energy delta function in $S$ allows us to rewrite $\bar{G}^{R/A}$ as an integral over energy:

    $$
    \begin{align*}
        \bar{G}^R_{\alpha \beta}(E)
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        \frac{S_{\alpha \beta}(E')}
        {E - E' + i\eta}
        \\
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        S_{\alpha \beta}(E') \bigg[
            \mathcal{P} \frac{1}{E - E'}
            - i \pi \delta(E - E')
        \bigg]
        
        \\[1.5em]
        
        \bar{G}^A_{\alpha \beta}(E)
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        \frac{S_{\alpha \beta}(E')}
        {E - E' - i\eta}
        \\
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        S_{\alpha \beta}(E') \bigg[
            \mathcal{P} \frac{1}{E - E'}
            + i \pi \delta(E - E')
        \bigg]
    \end{align*}
    $$

- **Time-ordered Green's function**

    $$
    \begin{align*}
        \bar{G}_{\alpha\beta}(E)
        &= e^{\beta F} \sum_{m,n} 
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        \\ &\quad \times \bigg[
            e^{-\beta E_m} \left(
                \mathcal{P} \frac{1}{E - (E_n - E_m)} 
                - i\pi \delta[E - (E_n - E_m)]
            \right)
            \\ &\quad \quad
            \mp e^{-\beta E_n} \left(
                \mathcal{P} \frac{1}{E - (E_n - E_m)}
                + i\pi \delta[E - (E_n - E_m)]
            \right)
        \bigg]
        \\
        &= e^{\beta F} \sum_{m,n} 
        e^{-\beta E_m} \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        \\ &\qquad \times \bigg[
            \mathcal{P} \frac{1}{E - (E_n - E_m)} 
            [1 \mp e^{-\beta(E_n - E_m)}]
            \\ &\qquad \quad
            - i\pi \delta[E - (E_n - E_m)]
            [1 \pm e^{-\beta(E_n - E_m)}]
        \bigg]
    \end{align*}
    $$

    The first term in the square bracket can be converted using the delta function in $S$, yielding

    $$
    \begin{align*}
        \bar{G}_{\alpha \beta}(E)
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi} 
        S_{\alpha \beta}(E') 
        \\ &\qquad \times \bigg[
            \mathcal{P} \frac{1}{E - E'}
            - i\pi \delta(E - E') 
            \frac{1 \pm e^{-\beta E}}
            {1 \mp e^{-\beta E}}
        \bigg]
    \end{align*}
    $$

Comparing this with the retarded and advanced Green's functions, we obtain an identity between the three kinds of Green's functions:

$$
\begin{align*}
    &(1 \mp e^{-\beta E})^{-1} \bar{G}^R_{\alpha \beta}(E)
    + (1 \mp e^{\beta E})^{-1} \bar{G}^A_{\alpha \beta}(E)
    \\
    &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
    S_{\alpha \beta}(E') 
    \\ &\qquad \times 
    \bigg\{
        \mathcal{P} \frac{
            (1 \mp e^{-\beta E})^{-1}
            + (1 \mp e^{\beta E})^{-1}
        }{E - E'}
        \\ &\qquad \qquad
        - i \pi \delta(E - E') \left[
            (1 \mp e^{-\beta E})^{-1}
            - (1 \mp e^{\beta E})^{-1}
        \right]
    \bigg\}
    \\
    &= \bar{G}_{\alpha \beta}(E)
\end{align*}
$$

## The Sum Rule

<div class="result">

**The sum rule of the spectral function:**

$$
\int_{-\infty}^\infty \frac{dE}{2\pi} \, S_{\alpha \alpha}(E)
= 1
$$

</div><br>

*Proof*: Due to the energy delta function in $S_{\alpha \alpha}$, the integration is converted to a summation

$$
\begin{align*}
    \int \frac{dE}{2\pi} \, S_{\alpha \alpha}(E)
    &= e^{\beta F} \sum_{m,n} 
    (e^{-\beta E_m} \mp e^{-\beta E_n}) 
    \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\alpha}}{m} 
\end{align*}
$$

Now we "undo" the insertion of identities:

$$
\begin{align*}
    \int \frac{dE}{2\pi} \, S_{\alpha \alpha}(E)
    &= e^{\beta F} \sum_{m,n} 
    \bigg[
        e^{-\beta E_m}
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\alpha}}{m} 
        \\ &\qquad \qquad \quad \mp
        e^{-\beta E_n}
        \amp{n}{a^\dagger_{\alpha}}{m} 
        \amp{m}{a_{\alpha}}{n} 
    \bigg]
    \\
    &= e^{\beta F} \bigg[
        \sum_{m} \amp{m}{e^{-\beta H} a_{\alpha} a^\dagger_\alpha}{m} 
        \\ &\qquad \quad \mp
        \sum_{n} \amp{n}{e^{-\beta H} a^\dagger_{\alpha} a_\alpha}{n} 
    \bigg]
    \\
    &= \Tr (e^{-\beta(H - F)} 
    [a_{\alpha} a^\dagger_\alpha]_\mp)
    \\
    &= \Tr e^{-\beta(H - F)} = 1 
    \qquad \blacksquare
\end{align*}
$$
