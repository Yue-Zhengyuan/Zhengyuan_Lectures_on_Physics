# Finite-*T* Green's Function: <br>Free Boson and Fermion

The free Hamiltonian for both bosons and fermions is

$$
H = \sum_\rho \epsilon_\rho c_\rho^\dagger c_\rho, \quad
\epsilon_\rho = E_\rho - \mu
$$

## In Imaginary Time

By definition,

$$
\begin{align*}
    \mathcal{G}_{\rho \sigma}(\tau - \tau')
    &\equiv -\expect{T [c_\rho(\tau) c_\sigma^\dagger(\tau')]}
    \\
    &= -\Tr \left[
        e^{-\beta(H - F)}
        T[c_\rho(\tau) c_\sigma^\dagger(\tau')]
    \right]
    \\[1em]
    \text{with} &\quad
    Z = \Tr e^{-\beta H} 
    = e^{-\beta F}, \quad \tau = it
\end{align*}
$$

At equal time, one finds from statistical physics that 

$$
\expect{c^\dagger_\sigma c_\rho}
= \delta_{\rho \sigma} 
\frac{1}{e^{\beta \epsilon_\rho} \mp 1}
\quad \begin{cases}
    - : &\text{boson} \\
    + : &\text{fermion}
\end{cases}
$$

Then, using the commutation relation

$$
[c_\rho, c^\dagger_\sigma]_\mp
= c_\rho c^\dagger_\sigma \mp c^\dagger_\sigma c_\rho
= \delta_{\rho \sigma}
$$

one obtain (at equal time)

$$
\begin{align*}
    \expect{c_\rho c^\dagger_\sigma}
    &= \delta_{\rho \sigma} \pm 
    \expect{c^\dagger_\sigma c_\rho}
    \\
    &= \delta_{\rho \sigma} \left(
        1 \pm \frac{1}{e^{\beta \epsilon_\rho} \mp 1}
    \right)
    \\
    &= \delta_{\rho \sigma}
    \frac{e^{\beta \epsilon_\rho}}
    {e^{\beta \epsilon_\rho} \mp 1}
\end{align*}
$$

We use the Heisenberg picture to obtain the time dependence of the operators: in imaginary time

$$
\frac{\partial A}{\partial\tau} = [H, A]
$$

Then

$$
\begin{align*}
    \frac{\partial c_\rho}{\partial \tau}
    &= \epsilon_\rho [c_\rho^\dagger c_\rho, c_\rho]
    \\
    &= \epsilon_\rho [c_\rho^\dagger, c_\rho] c_\rho
    \\
    &= - \epsilon_\rho c_\rho
\end{align*} \qquad
\begin{align*}
    \frac{\partial c_\rho^\dagger}{\partial \tau}
    &= \epsilon_\rho [c_\rho^\dagger c_\rho, c_\rho^\dagger]
    \\
    &= \epsilon_\rho c_\rho^\dagger [c_\rho, c_\rho^\dagger]
    \\
    &= \epsilon_\rho c_\rho
\end{align*}
$$

Therefore

$$
c_\rho(\tau) = e^{-\epsilon_\rho \tau} c_\rho(0),\quad
c^\dagger_\rho(\tau) = e^{\epsilon_\rho \tau} c^\dagger_\rho(0)
$$

Then the Green's function has the explicit form

$$
\begin{align*}
    \mathcal{G}_{\rho \sigma}(\tau - \tau')
    &\equiv -\expect{T c_\rho(\tau) c_\sigma^\dagger(\tau')}
    \\
    &= - \left[
        \theta(\tau - \tau') 
        \expect{c_\rho(\tau) c_\sigma^\dagger(\tau')}
        \pm \theta(\tau' - \tau)
        \expect{c_\sigma^\dagger(\tau') c_\rho(\tau)}
    \right]
    \\
    &= - \left[
        \theta(\tau - \tau') 
        \expect{c_\rho c_\sigma^\dagger}
        \pm \theta(\tau' - \tau)
        \expect{c_\sigma^\dagger c_\rho}
    \right] e^{-\epsilon_\rho (\tau - \tau')}
    \\[0.6em]
    &= - \delta_{\rho \sigma} 
    e^{-\epsilon_\rho (\tau - \tau')} 
    \bigg[
        \theta(\tau - \tau') 
        \frac{e^{\beta \epsilon_\rho}}
        {e^{\beta \epsilon_\rho} \mp 1}
        \\ &\qquad \qquad \qquad \qquad 
        \pm \theta(\tau' - \tau)
        \frac{1}{e^{\beta \epsilon_\rho} \mp 1}
    \bigg] 
\end{align*}
$$

## In Matsubara Frequency

Now we Fourier transform this result to find

$$
\begin{align*}
    \mathcal{G}_{\rho \sigma}(i\omega_n)
    &= \int_0^\beta d\tau \, e^{+i\omega_n \tau} 
    \mathcal{G}_{\rho \sigma}(\tau)
    \\
    &= - \delta_{\rho \sigma} 
    \int_0^\beta d\tau \, 
    e^{(i\omega_n -\epsilon_\rho) \tau}
    \frac{e^{\beta \epsilon_\rho}}
    {e^{\beta \epsilon_\rho} \mp 1}
    \\
    &= - \frac{\delta_{\rho \sigma}}
    {i\omega_n - \epsilon_\rho}
    \frac{
        e^{(i\omega_n - \epsilon_\rho)\beta} - 1
    }{1 \mp e^{-\beta \epsilon_\rho}}
\end{align*}
$$

One can check explicitly that

$$
e^{i\omega_n \beta} = \pm e^{- \epsilon_\rho \beta}
$$

Therefore we get the same result for both bosons and fermions (except for the allowed values of $\omega_n$):

<div class="result">

**Matsubara Green's Function for Boson/Fermion:**

$$
\mathcal{G}_{\rho \sigma}(i\omega_n)
= \frac{\delta_{\rho \sigma}}
{i\omega_n - \epsilon_\rho}
$$

</div><br>
