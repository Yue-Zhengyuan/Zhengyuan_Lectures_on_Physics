# Imaginary Time

## Motivation: Grand-Canonical Ensemble

In grand-canonical ensemble, the density matrix is (the Hamiltonian is in fact $H - \mu N$)

$$
\rho = e^{-\beta H}
$$

From this we define the **grand-canonical partition function** $Z$ and the **grand-canonical potential** $F$ (also often denoted by $\Omega$, but we use the same notation as the canonical ensemble):

$$
Z = \Tr e^{-\beta H} = e^{-\beta F}
$$

The imaginary time formulation is motivated by the similarity between the density matrix and the time evolution operator (starting from $t_0 = 0$)

$$
U(t) = e^{-iHt}
$$

The density matrix can be then regarded as evolution in imaginary time:

$$
\rho = e^{-i H (-i\beta)} = U(-i\beta)
$$

At zero temperature, one is interested in the ground state expectation values ($O = O_1(t_1) \cdots O_n(t_n)$ in interaction picture)

$$
\expect{O}
= \lim_{T \to \infty(1-i\epsilon)}
\frac{
    \amp{0}{T[S(T, -T) O]}{0}
}{
    \amp{0}{S(T, -T)}{0}
}
$$

But at finite temperature, the quantity is replaced by the *ensemble average*

$$
\expect{O} = \frac{\Tr(\rho O)}
{\Tr(\rho)}
$$

Thus we see the replacement

<div class="result">

**Expectation values from zero to finite temperature:**

$$
\amp{0}{S(+\infty,-\infty) O}{0} \to \Tr(\rho O)
$$

</div><br>

Notably, the time evolution is now restricted to a finite period (from 0 to $-i\beta$), and with the full Hamiltonian $H$ instead of using the interaction $V$ only. 

## Evolution Pictures in Imaginary Time

Motivated by the similarity $\rho = U(-i\beta H)$, one get the imaginary time evolution by setting

$$
t = -i \tau \quad (\text{or} \ \  \tau = it)
$$

### Schrödinger Picture

- State evolution (Schrödinger equation)

    $$
    \frac{\partial}{\partial t} \ket{\psi_S(t)}
    = -i H \ket{\psi_S(t)}
    \  \Rightarrow \ 
    \frac{\partial}{\partial \tau} \ket{\psi_S(\tau)}
    = -H \ket{\psi_S(\tau)}
    $$

- Time evolution operator 
    
    $$
    \begin{align*}
        &U(t,t_0) = T{\left[ \exp{
            \left(
                -i \int_{t_0}^t dt' \, H(t')
            \right)
        } \right]}
        \\[1em]
        &\Rightarrow \quad
        U(\tau,\tau_0) = T{\left[ \exp{
            \left(
                - \int_{\tau_0}^\tau d\tau' \, H(\tau')
            \right)
        } \right]}
    \end{align*}
    $$

    On the RHS $T$ means time-ordering in $\tau$. For time-independent $H$, the formulas simplify to

    $$
    \begin{align*}
        U(t,t_0) = e^{-iH(t - t_0)} 
        \ &\Rightarrow \ 
        U(\tau,\tau_0) = e^{-H(\tau - \tau_0)}
    \end{align*}
    $$

    <div class="remark">

    *Remark*: We now see that the density matrix corresponds to imaginary time evolution from $\tau = 0$ to $\beta$

    $$
    \rho = e^{-\beta H} = U(\beta,0)
    $$

    </div><br>

### Heisenberg Picture

For time-independent $H$:

- Operator evolution (for convenience, set $t_0, \tau_0 = 0$)
    
    $$
    \begin{align*}
        O_H(t) &= e^{iHt} O_S e^{-iHt}
        \\[0.5em]
        \frac{\partial O_H}{\partial t} &= i [H, O_H]
    \end{align*}
    \ \Rightarrow \ 
    \begin{align*}
        O_H(\tau) &= e^{H\tau} O_S e^{-H\tau}
        \\[0.5em]
        \frac{\partial O_H}{\partial \tau} &= [H, O_H]
    \end{align*}
    $$

### Interaction Picture

As usual, we separate the full $H$ into $H_0 + V$. The chemical potential term $-\mu N$ is absorbed by $H_0$. 

- State evolution
  
    $$
    \ket{\psi_I(t)} = e^{iH_0 t} \ket{\psi_S(t)}
    \ \Rightarrow \ 
    \ket{\psi_I(\tau)} = e^{H_0 \tau} \ket{\psi_S(\tau)}
    $$

- Operator evolution (by $H_0$)
    
    $$
    \begin{align*}
        O_I(t) &= e^{iH_0 t} O_S e^{-iH_0 t}
        \\[0.5em]
        \frac{\partial O_I}{\partial t} &= i [H_0, O_I]
    \end{align*}
    \ \Rightarrow \ 
    \begin{align*}
        O_I(\tau) &= e^{H_0 \tau} O_S e^{-H_0 \tau}
        \\[0.5em]
        \frac{\partial O_I}{\partial \tau} &= [H_0, O_I]
    \end{align*}
    $$

- State evolution operator
    
    $$
    \begin{align*}
        \begin{align*}
            &S(t,t_0) = e^{iH_0 (t-t_0)} U(t, t_0)
            \\
            &= T{\left[ \exp{
                \left(
                    -i \int_{t_0}^t dt' \, V_I(t')
                \right)
            } \right]} 
        \end{align*}
        \ \Rightarrow \ 
        \begin{align*}
            &S(\tau,\tau_0) 
            = e^{H_0 (\tau-\tau_0)} U(t, t_0)
            \\
            &= T{\left[ \exp{
                \left(
                    - \int_{\tau_0}^\tau d\tau' \, V_I(\tau')
                \right)
            } \right]} 
        \end{align*}
    \end{align*}
    $$
