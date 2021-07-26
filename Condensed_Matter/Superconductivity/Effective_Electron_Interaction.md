# Phonon-Mediated Electron Interaction

We start from the Fröhlich Hamiltonian with only one band and one phonon branch:

$$
H = \sum_k \epsilon_k c_k^\dagger c_k 
+ \sum_q \omega_q b_q^\dagger b_q
+ \sum_{k,q} g_{k,q} c_{k+q}^\dagger c_k (b_q + b_{-q}^\dagger)
$$

where $g_{k,q} \equiv g_{k+q,k}^q$ (scattering of electron with momentum $k$ by phonon with momentum $q$), and we omit the 1/2 constant in $H_{ph}$. 

## Canonical Transformation Approach

To derive the effective electron interaction mediated by phonons, we use the **canonical transformation** method. Consider the Hamiltonian

$$
H = H_0 + \eta H_1
$$

$H_1$ is treated as a perturbation, and $\eta$ is a small coefficient. The canonical transformation on $H$ is

$$
\begin{align*}
    H' &= e^{-\eta S} H e^{\eta S} \\
    &= H + [H,\eta S] + \frac{1}{2}[[H,\eta S], \eta S] + \cdots \\
    &= H_0 + \eta H_1 + \eta [H_0 + \eta H_1, S]
    + \frac{\eta^2}{2} [[H_0 +\eta H_1, S], S] + \cdots \\
    &= H_0 + \eta(H_1 + [H_0, S]) 
    + \eta^2 \bigg([H_1, S] + \frac{1}{2}[[H_0,S],S] \bigg)
    + O(\eta^3)
\end{align*}
$$

The operator $S$ is chosen such that the first order term vanishes:

$$
H_1 + [H_0, S] = 0
$$

Then the transformed $H$ up to second order in $\eta$ is

$$
H' = H_0 + \frac{\eta^2}{2}[H_1, S] + O(\eta^2)
$$

In the Fröhlich Hamiltonian, we choose 

$$
H_0 = H_e + H_{ph}, \quad \eta H_1 = H_{e-ph}
$$

To determine the form of $S$, we first calculate its matrix elements among the eigenstates of $H_0$, which is just the direct product of electron eigenstate and phonon eigenstate. In momentum representation, we simply obtain

$$
\left. \begin{align*}
    H_e \ket{k}_e &= \epsilon_k \ket{k}_e \\
    H_{ph} \ket{q}_{ph} &= \omega_q \ket{q}_{ph}
\end{align*} \right\} \Rightarrow 
H_0 \ket{kq} = E_{kq} \ket{kq} 
\left\{ \begin{align*}
    E_{kq} &= \epsilon_k + \omega_q \\
    \ket{kq} &= \ket{k}_e \otimes \ket{q}_{ph}
\end{align*} \right.
$$

Then from the requirement $H_1 = -[H_0, S]$, we obtain

$$
\begin{align*}
    \amp{k'q'}{H_1}{kq} &= \amp{k'q'}{S H_0 - H_0 S}{kq}
    \\ &= (E_{kq} - E_{k'q'}) \amp{k'q'}{S}{kq}
    \\ &\Downarrow \\
    \amp{k'q'}{S}{kq} &= \frac{\amp{k'q'}{H_1}{kq}}{E_{kq} - E_{k'q'}}
\end{align*}
$$

To express the denominator as an operator, we examine the only nonbero matrix elements of

$$
\begin{align*}
    \eta H_1 &= \sum_{k,q} \Big[
        g_{k,q} c_{k+q}^\dagger b_q c_k
        + g_{k,q} c_{k+q}^\dagger b_{-q}^\dagger c_k
    \Big] \\
    &= \sum_{k,q} \Big[
        g_{k,q} c_{k+q}^\dagger b_q c_k
        + g_{k,-q} c_{k-q}^\dagger b_{q}^\dagger c_k
    \Big]
\end{align*}
$$

- First term: $\amp{k+q,0}{H_1}{k,q} \Rightarrow E_{kq} - E_{k+q,0} = \epsilon_k + \omega_q - \epsilon_{k+q}$
- Second term: $\amp{k-q,q}{H_1}{k,0} \Rightarrow E_{k0} - E_{k-q,q} = \epsilon_k - \epsilon_{k-q} - \omega_q$

Then we can write (using $\omega_q = \omega_{-q}$)

$$
\begin{align*}
    \eta S &= \sum_{k,q} \bigg[
        \frac{g_{k,q}}{\epsilon_k + \omega_q - \epsilon_{k+q}}
        c_{k+q}^\dagger b_q c_k
        + \frac{g_{k,-q}}{\epsilon_k - \epsilon_{k-q} - \omega_q}
        c_{k-q}^\dagger b_{q}^\dagger c_k
    \bigg] \\
    &= \sum_{k,q} \bigg[
        \frac{g_{k,q}}{\epsilon_k - \epsilon_{k+q} + \omega_q}
        c_{k+q}^\dagger b_q c_k
        + \frac{g_{k,q}}{\epsilon_k - \epsilon_{k+q} - \omega_q}
        c_{k+q}^\dagger b_{-q}^\dagger c_k
    \bigg] \\
    &\equiv \sum_{k,q} c_{k+q}^\dagger c_k \Big(
        A_{k,q} b_q + B_{k,q} b_{-q}^\dagger
    \Big)
\end{align*}
$$

Now we are ready to calculate the effective electron interaction: 

$$
\begin{align*}
    H_\text{eff} &= \frac{1}{2}[\eta H_1, \eta S] \\
    &= \frac{1}{2} \sum_{k,q} \sum_{k',q'} \Big[
        c_{k+q}^\dagger c_k g_{k,q} (b_q + b_{-q}^\dagger),
        c_{k'+q'}^\dagger c_{k'} (
            A_{k',q'} b_{q'} + B_{k',q'} b_{-q'}^\dagger
        )
    \Big]
\end{align*}
$$

From the relations (note that Fourier transform (with symmetric convention) preserves boson/fermion commutation relations)

$$
\begin{align*}
    &[Aa,Bb] = AB[a,b] + [A,B]ab - [A,B][a,b]
    \quad ([A/B,a/b] = 0)
    \\
    &[b_q, b_{q'}] = 0, \quad [b_q, b_{q'}] = \delta_{q,q'}, \quad
    \{c_k, c_{k'}\} = 0, \quad \{c_k, c_{k'}\} = \delta_{k,k'}
\end{align*}
$$

define

$$
\begin{align*}
    A &= c_{k+q}^\dagger c_k, & 
    a &= g_{k,q} (b_q + b_{-q}^\dagger) \\
    B &= c_{k'+q'}^\dagger c_{k'}, &
    b &= A_{k',q'} b_{q'} + B_{k',q'} b_{-q'}^\dagger
\end{align*}
$$

Then

$$
\begin{align*}
    [a,b] &= [
        g_{k,q} (b_q + b_{-q}^\dagger), 
        A_{k',q'} b_{q'} + B_{k',q'} b_{-q'}^\dagger
    ] \\ 
    &= g_{k,q} \Big\{
        B_{k',q'} [b_q, b^\dagger_{-q'}]
        + A_{k',q'} [b^\dagger_{-q}, b_{q'}] 
    \Big\} \\
    &= g_{k,q} (B_{k',q'} - A_{k',q'}) \delta_{q+q'}
    \\
    [A,B] &= [c_{k+q}^\dagger c_k, c_{k'+q'}^\dagger c_{k'}] \\
    &= c_{k+q}^\dagger c_k c_{k'+q'}^\dagger c_{k'}
    - c_{k'+q'}^\dagger c_{k'} c_{k+q}^\dagger c_k \\
    &= c_{k+q}^\dagger (\delta_{k'+q'-k} - c_{k'+q'}^\dagger c_k) c_{k'}
    - c_{k'+q'}^\dagger (\delta_{k+q-k'} - c_{k+q}^\dagger c_{k'}) c_k
    \\
    &= c_{k+q}^\dagger c_{k'} \delta_{k'+q'-k}
    - c_{k'+q'}^\dagger c_k \delta_{k+q-k'}
\end{align*}
$$

We then see that

$$
\begin{align*}
    [A,B][a,b]
    &= [
        c_{k+q}^\dagger c_{k'} \delta_{k'+q'-k}
        - c_{k'+q'}^\dagger c_k \delta_{k+q-k'}
    ] \\ &\quad \times
    g_{k,q} (B_{k',q'} - A_{k',q'}) \delta_{q+q'} \\
    &= [
        c_{k+q}^\dagger c_{k'} - c_{k'-q}^\dagger c_k 
    ] \\ &\quad \times
    g_{k,q} (B_{k',-q} - A_{k',-q}) \delta_{q+q'} \delta_{k+q-k'}
\end{align*}
$$

The terms corresponding to electron interaction ($c^\dagger c c^\dagger c$) is therefore $AB[a,b]$: omitting the rest terms, we have

$$
\begin{align*}
    H_\text{eff} &= \frac{1}{2} \sum_{k,q} \sum_{k',q'}
    g_{k,q} (B_{k',q'} - A_{k',q'}) \delta_{q+q'}
    c_{k+q}^\dagger c_k c_{k'+q'}^\dagger c_{k'}
    + \cancel{\text{others}} \\
    &= \frac{1}{2} \sum_{k,k',q}
    g_{k,q} (B_{k',-q} - A_{k',-q})
    c_{k+q}^\dagger c_k c_{k'-q}^\dagger c_{k'}
    \\
    &\equiv \sum_{k,k',q} V_{kk'q}
    c_{k+q}^\dagger c_k c_{k'-q}^\dagger c_{k'}
\end{align*}
$$

where we defined the effective interaction potential

$$
\begin{align*}
    V_{kk'q} &\equiv \frac{1}{2} g_{k,q} (B_{k',-q} - A_{k',-q}) \\
    &= \frac{1}{2} g_{k,q} \bigg(
        \frac{g_{k',-q}}{\epsilon_{k'} - \epsilon_{k'-q} - \omega_q}
        - \frac{g_{k',-q}}{\epsilon_{k'} - \epsilon_{k'-q} + \omega_q}
    \bigg) \\
    &= \frac{
        g_{k,q} g_{k',-q} \omega_q
    }{
        (\epsilon_{k'} - \epsilon_{k'-q})^2 - \omega_q^2
    }
\end{align*}
$$

### Electron Pairing in Superconductors

For superconductors, the major contribution comes from the terms with $k' = -k$. Then using $\epsilon_{-k} = \epsilon_k, g_{-k,-q} = g_{k,q}^*$, we obtain

$$
\begin{align*}
    H_\text{eff} &= \sum_{k,q} V_{k,-k,q}
    c_{k+q}^\dagger c_k c_{-k-q}^\dagger c_{-k} \\
    &= \sum_{k,q} V_{k,-k,q}
    c_{k+q}^\dagger c_{-k-q}^\dagger c_{-k} c_k
    + \cancel{\text{non-interaction term}}
\end{align*}
$$

The interaction potential is

$$
V_{k,-k,q} = \frac{
    |g_{k,q}|^2 \omega_q
}{
    (\epsilon_{k} - \epsilon_{k+q})^2 - \omega_q^2
}
$$

For small phonon momentum $q$, the potential is *negative* ($|\epsilon_k - \epsilon_{k+q}| < \omega_q$), providing *attraction* between the electrons. 

## Path Integral Approach

One can also derive the effective electron Hamiltonian using the coherent state path integral: replacing operators $(c, b)$ by Grassmann/complex numbers, the partition function is

$$
\begin{align*}
    Z &= \int D\bar{c} \, Dc \, D\bar{b} \, Db \, e^{-S}
    \\
    S &= S_e + S_{ph} + S_{e-ph}
    \\
    &= \int_0^\beta d\tau \, \bigg\{ 
        \sum_k \Big[
            \bar{c}_k \partial_\tau c_k
            + \epsilon_k \bar{c}_k c_k 
        \Big] 
        + \sum_q \Big[
            \bar{b}_q \partial_\tau b_q
            + \omega_q \bar{b}_q b_q 
        \Big] \\ &\quad
        + \sum_{k,q} \Big[
            g_{k,q} \bar{c}_{k+q} c_k b_q 
            + g_{k,-q} \bar{c}_{k-q} c_k \bar{b}_q)
        \Big]
    \bigg\}
\end{align*}
$$

To derive the effective electron action $S_\text{eff}$, we only need to integrate out $\bar{b},b$: 

$$
\begin{align*}
    Z &= \int D\bar{c} \, Dc \, e^{-S_\text{eff}} \\
    e^{-S_\text{eff}} &\equiv 
    e^{-S_e} \int D\bar{b} \, Db \, e^{-(S_{ph}+S_{e-ph})}
\end{align*}
$$

It helps to also Fourier transform to frequency representation:

$$
\begin{align*}
    c_k(\tau) &= \frac{1}{\sqrt{\beta}} \sum_{\nu}
    c_{k\nu} e^{i\nu\tau}, & 
    \nu &\in \left\{
        \frac{(2n+1)\pi}{\beta} \bigg| n \in \mathbb{Z}
    \right\} \\
    b_q(\tau) &= \frac{1}{\sqrt{\beta}} \sum_{\chi}
    b_{q\chi} e^{i\chi\tau}, & 
    \chi &\in \left\{
        \frac{2n\pi}{\beta}  \bigg| n \in \mathbb{Z}
    \right\}
\end{align*}
$$

We focus on the terms involved in the integration of $\bar{b},b$:

- Pure phonon term

    $$
    \begin{align*}
        S_{ph} &= \frac{1}{\beta} \int_0^\beta d\tau 
        \sum_q \sum_{\chi,\chi'} e^{i(-\chi'+\chi)\tau} 
        \bar{b}_{q\chi'} (i\chi + \omega_q) b_{q\chi}
        \\
        &= \sum_{q,\chi} (i\chi + \omega_q) \bar{b}_{q\chi} b_{q\chi}
    \end{align*}
    $$

- Electron-phonon interaction

    $$
    \begin{align*}
        S_{e-ph} &= \frac{1}{\beta^{3/2}} \int_0^\beta d\tau 
        \sum_{k,q} \sum_{\nu,\nu',\chi} 
        \\ &\quad \times \Big[
            g_{k,q} \bar{c}_{k+q,\nu} c_{k\nu'} b_{q\chi}
            e^{i(-\nu+\nu'+\chi)}
            + g_{k,-q} \bar{c}_{k-q,\nu} c_{k\nu'} \bar{b}_{q\chi}
            e^{i(-\nu+\nu'-\chi)}
        \Big]
        \\
        &= \frac{1}{\sqrt{\beta}} \sum_{q,\chi} \sum_{k,\nu} \Big[
            g_{k,q} \bar{c}_{k+q,\nu} c_{k,\nu-\chi} b_{q\chi}
            + g_{k,-q} \bar{c}_{k-q,\nu} c_{k,\nu+\chi} \bar{b}_{q\chi}
        \Big]
    \end{align*}
    $$

Then

$$
\begin{align*}
    S &= S_e + \sum_{q,\chi} \bigg\{
        (i\chi + \omega_q) \bar{b}_{q\chi} b_{q\chi}
        \\ &\quad
        + \frac{1}{\sqrt{\beta}} \sum_{k,\nu} \Big[
            g_{k,q} \bar{c}_{k+q,\nu} c_{k,\nu-\chi} b_{q\chi}
            + g_{k,-q} \bar{c}_{k-q,\nu} c_{k,\nu+\chi} \bar{b}_{q\chi}
        \Big]
    \bigg\}
\end{align*}
$$

The integration over $\bar{b},b$ is therefore Gaussian. The result is

$$
\begin{align*}
    & \int D\bar{b} \, Db \, e^{-(S_{ph}+S_{e-ph})}
    \\
    &\propto \prod_{q,\chi} \int d\bar{b}_{q\chi} \, db_{q\chi}
    \exp \bigg\{
        - (i\chi + \omega_q) \bar{b}_{q\chi} b_{q\chi}
        \\ &\quad
        - \bigg[
            \frac{1}{\sqrt{\beta}} \sum_{k,\nu}
            g_{k,q} \bar{c}_{k+q,\nu} c_{k,\nu-\chi}
        \bigg] b_{q\chi}
        - \bigg[
            \frac{1}{\sqrt{\beta}} \sum_{k,\nu}
            g_{k,-q} \bar{c}_{k-q,\nu} c_{k,\nu+\chi}
        \bigg] \bar{b}_{q\chi}
    \bigg\}
    \\
    &\propto \exp \bigg\{
        \sum_{q,\chi} \frac{1}{\beta(i\chi + \omega_q)}
        \\ &\quad \times \bigg[
            \sum_{k,\nu}
            g_{k,q} \bar{c}_{k+q,\nu} c_{k,\nu-\chi}
        \bigg] \bigg[
            \sum_{k',\nu'}
            g_{k',-q} \bar{c}_{k'-q,\nu'} c_{k',\nu'+\chi}
        \bigg]
    \bigg\}
    \\
    \Rightarrow
    S_\text{eff} &= S_e 
    - \sum_{q,\chi} \frac{1}{\beta(i\chi + \omega_q)}
    \sum_{k,k',\nu,\nu'}
    g_{k,q} g_{k',-q} \bar{c}_{k+q,\nu} c_{k,\nu-\chi}
    \bar{c}_{k'-q,\nu'} c_{k',\nu'+\chi}
\end{align*}
$$

We then take the approximation
