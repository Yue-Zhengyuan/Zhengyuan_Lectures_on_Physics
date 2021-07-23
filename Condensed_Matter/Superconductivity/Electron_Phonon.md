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