# Electron-Phonon Interaction

## The Fröhlich Hamiltonian

The basic model of electron-phonon coupling effects in crystals is the **Fröhlich Hamiltonian:**

$$
H = H_e + H_{ph} + H_{e-ph}
$$

- The electrons are described by non-interacting <i>quasi-</i>particles with dispersion $\epsilon_k$:

    $$
    H_e = \sum_{k,\sigma,\nu} \epsilon_{k\nu}
    c_{k\sigma\nu}^{\dagger} c_{k\sigma\nu}
    $$

    where $\nu$ is the energy band label, $\sigma$ is the spin of the quasi-particle.

- The lattice vibration is described by the phonon Hamiltonian as independent harmonic oscillators:

    $$
    H_{ph} = \sum_{q,\lambda} \omega_{q\lambda} 
    (b_{q\lambda}^{\dagger} b_{q\lambda} + 1/2)
    $$

    where $\lambda$ is the phonon branch label (e.g. acoustic or optical, if the lattice unit cell contains more than one site). 

- The electron-phonon interaction is described by
    
    $$
    H_{e-ph} = \sum_{k,\nu,\nu',\sigma} \sum_{q,j}
    g_{k+q,\nu';k\nu}^{q\lambda} c_{k+q,\sigma\nu'}^\dagger 
    (b_{q\lambda} + b_{-q\lambda}^\dagger) c_{k\sigma\nu}
    $$

    where $g_{k+q,\nu;k\nu}^{q\lambda}$ is the amplitude for scattering a quasi-particle (which will be simply called "an electron") from state $(k,\nu)$ to $(k+q,\nu')$ by absorbing (emitting) a phonon with momentum $q$ ($-q$) and branch $\lambda$ (which does not change the spin of the electron).

## Phonon-Mediated Electron Interaction

For simplicity, assume that there is only one band and one phonon branch. Then the Fröhlich Hamiltonian takes a simpler form:

$$
H = \sum_k \epsilon_k c_k^\dagger c_k 
+ \sum_q \omega_q (b_q^\dagger b_q + 1/2)
+ \sum_{k,q} g_{k,q} c_{k+q}^\dagger c_k (b_q + b_{-q}^\dagger)
$$

where $g_{k,q} \equiv g_{k+q,k}^q$ (scattering of electron with momentum $k$ by phonon with momentum $q$). 

### Canonical Transformation Method

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

To determine the form of $S$, we first calculate its matrix elements among the eigenstates of $H_0$:

$$
H_0 \ket{m} = E_m \ket{m}
$$

Then from the requirement $H_1 + [H_0, S] = 0$, we obtain

$$
\begin{align*}
    H_1 &= - [H_0, S]
    \\ &\Downarrow \\
    \amp{m}{H_1}{n} &= \amp{m}{S H_0 - H_0 S}{n}
    \\ &= (E_n - E_m) \amp{m}{S}{n}
    \\ &\Downarrow \\
    \amp{m}{S}{n} &= \frac{\amp{m}{H_1}{n}}{E_n - E_m}
\end{align*}
$$

Since $H_0$ is just a sum of two 

### Path Integral Approach

One can also derive express the system as a coherent state path integral: replacing operators $c, b$ by Grassmann/complex numbers $\psi, z$, the partition function is

$$
\begin{align*}
    Z &= \int D\bar{\psi} \, D\psi \, D\bar{z} \, Dz \, e^{-S}
    \\
    S &=  
\end{align*}
$$
