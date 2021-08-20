# Elementary Processes of Scalar QED

<font size=5>

**Part 2: Particle-Photon Interaction**

</font>

## Compton Scattering

The **compton scattering** refers to the scattering of an incoming photon $\gamma$ by an "electron" $\phi$ at rest (in the lab frame). For a moment, we go into an arbitrary frame, and call the momenta of the incoming $\phi, \gamma$ as $p, k$, and the momenta of the outgoing $\phi, \gamma$ as $p', k'$. The scattering process is described as

$$
\phi(p) + \gamma(k) \to \phi(p') + \gamma(k')
$$

In the following calculation, the charge of a $\phi$ particle $(Q)$ will be made explicit. 

### Invariant Amplitude $\mathcal{M}$

In scalar QED, Compton scattering involves the following 3 diagrams at the lowest order:

- The seagull diagram
    
    <center>
    <img src="images/compton-seagull.png" height="180px">
    </center>

    $$
    i \mathcal{M}_4 = 2i (eQ)^2 g^{\mu \nu} \epsilon_\mu(k) \epsilon'^*_\nu(k')
    $$

- The s-channel diagram
    
    <center>
    <img src="images/compton-s.png" height="180px">
    </center>

    $$
    \begin{align*}
        i \mathcal{M}_s 
        &= \color{green} \epsilon_\mu(k) \cdot
        ieQ[p + (p+k)]^\mu 
        \\ & \quad \times
        \color{darkcyan}
        \frac{i}{(p+k)^2 - m^2}
        \\ & \quad \times
        \color{red}
        ieQ [(p'+k') + p']^\nu \epsilon'^*_\nu(k')
    \end{align*}
    $$

    We can simplify a little bit using the on-shell conditions of the incoming $\phi, \gamma$:

    $$
    p^2 = m^2 \qquad
    k^2 = 0
    $$

    Then

    $$
    \begin{align*}
        (p+k)^2 - m^2 
        &= p^2 + k^2 + 2p\cdot k - m^2
        \\
        &= 2p \cdot k
    \end{align*}
    $$

    Therefore

    $$
    \begin{align*}
        i \mathcal{M}_s 
        &= -i(eQ)^2 
        \epsilon_\mu(k) \epsilon'^*_\nu(k')
        \frac{(2p+k)^\mu (2p'+k')^\nu}{2p\cdot k}
    \end{align*}
    $$

- The u-channel diagram

    <center>
    <img src="images/compton-u.png" height="200px">
    </center>

    Then

    $$
    \begin{align*}
        i \mathcal{M}_u 
        &= \color{green} \epsilon_\mu(k) \cdot
        ieQ[(p'-k) + p']^\mu 
        \\ & \quad \times
        \color{darkcyan}
        \frac{i}{(p-k')^2 - m^2}
        \\ & \quad \times
        \color{red}
        ieQ [p + (p-k')]^\nu \epsilon'^*_\nu(k')
    \end{align*}
    $$

    Again, using the on-shell conditions of the incoming/outgoing $\phi, \gamma$, we have

    $$
    \begin{align*}
        (p-k')^2 - m^2 
        &= p^2 + k'^2 - 2p\cdot k' - m^2
        \\
        &= -2p \cdot k'
    \end{align*}
    $$

    Therefore

    $$
    \begin{align*}
        i \mathcal{M}_u 
        &= i(eQ)^2 
        \epsilon_\mu(k) \epsilon'^*_\nu(k')
        \frac{(2p'-k)^\mu (2p-k')^\nu}{2p\cdot k'}
    \end{align*}
    $$

The total amplitude $\mathcal{M}$ is the sum of these 3 terms:

$$
\begin{align*}
    i \mathcal{M}
    &= i (\mathcal{M}_4 + \mathcal{M}_s + \mathcal{M}_u)
    \\
    &= i(eQ)^2 
    \epsilon_\mu(k) \epsilon'^*_\nu(k') T^{\mu \nu}    
\end{align*}
$$

where

$$
\begin{align*}
    T^{\mu \nu} 
    &= 2 g^{\mu \nu} - A^{\mu \nu} + B^{\mu \nu}
    \\
    A^{\mu \nu} 
    &= \frac{(2p+k)^\mu (2p'+k')^\nu}{2p\cdot k}
    \\
    B^{\mu \nu}
    &= \frac{(2p'-k)^\mu (2p-k')^\nu}{2p\cdot k'}
\end{align*}
$$

### Side Note: Verifying Ward Identity

Let us now again only focus on the outgoing $\gamma$:

<center>
<img src="images/ward2.png" height="160px">
</center>

The amplitude $\mathcal{M}$ of Compton scattering can be expressed as

$$
i\mathcal{M} = i \mathcal{M}^\nu(k')\epsilon'^*_\nu(k')
$$

where

$$
\mathcal{M}^\nu = i(eQ)^2 
\epsilon_\mu(k) T^{\mu \nu}
$$

The Ward identity then states that

$$
k'_\nu \mathcal{M}^\nu = 0
$$

Let us check it is true: replace $\epsilon'^*_\nu(k')$ by $k'_\nu$ in $\mathcal{M}$ (omitting the overall constant $i(eQ)^2$), we obtain

$$
\begin{align*}
    &\epsilon_\mu k'_\nu T^{\mu \nu}
    = \epsilon_\mu k'_\nu 
    (2g^{\mu \nu} - A^{\mu \nu} + B^{\mu \nu})
    \\[0.5em]
    &= \epsilon_\mu \left(
        2 k'^\mu 
        - \frac{(2p+k)^\mu (2p'+k')\cdot k'}{2p\cdot k}
        + \frac{(2p'-k)^\mu (2p-k')\cdot k'}{2p\cdot k'}
    \right)
\end{align*}
$$

Apply the on-shell conditions:

$$
\begin{align*}
    \epsilon_\mu k'_\nu T^{\mu \nu}
    &= \epsilon_\mu \left(
        2 k'^\mu 
        - \frac{(2p+k)^\mu 2p'\cdot k'}{2p\cdot k}
        + \frac{(2p'-k)^\mu 2p\cdot k'}{2p\cdot k'}
    \right)
    \\
    &= \epsilon_\mu \left(
        2 k'^\mu - (2p+k)^\mu + (2p'-k)^\mu
    \right)
\end{align*}
$$

Here we used momentum conservation to obtain

$$
\left. \begin{align*}
    p + k &= p' + k'
    \\
    (p+k)^2 - m^2 &= 2p\cdot k
    \\
    (p'+k')^2 - m^2 &= 2p'\cdot k'
\end{align*} \right\}
\, \Rightarrow \, 
p\cdot k = p' \cdot k'
$$

<div class="remark">

*Remark*: In the same way, we can derive 

$$
\left. \begin{align*}
    p - k' &= p' - k
    \\
    (p-k')^2 - m^2 &= - 2p\cdot k'
    \\
    (p'-k)^2 - m^2 &= - 2p'\cdot k
\end{align*} \right\}
\, \Rightarrow \, 
p' \cdot k = p \cdot k'
$$

We will use these two relations below. 

</div><br>

Finally

$$
\epsilon_\mu k'_\nu T^{\mu \nu}
= 2 \epsilon_\mu (p'+k' - p - k)^\mu
= 0
$$

Thus the Ward identity is satisfied. 

### Polarization Sum

What goes into the differential cross section is the *sum* of the squared norm $|\mathcal{M}|^2$ for *each* configuration of polarization $\epsilon, \epsilon'$, but *averaged* over the *incoming* polarization $\epsilon$ (*two* linearly independent choices). Mathematically, this refers to (note that $T^{\mu \nu}$ is real)

$$
\begin{align*}
    \frac{1}{2} \sum_{\text{pol.}} 
    |\mathcal{M}|^2
    &= \frac{(eQ)^4}{2} \sum_{\epsilon, \epsilon'} 
    (\epsilon_\mu \epsilon'^*_\nu T^{\mu \nu})
    (\epsilon^*_\rho \epsilon'_\sigma T^{\rho \sigma})
    \\
    &= \frac{(eQ)^4}{2} 
    \sum_{\epsilon} \epsilon_\mu \epsilon^*_\rho
    \sum_{\epsilon'} \epsilon'_\sigma \epsilon'^*_\nu \,
    T^{\mu \nu} T^{\rho \sigma}
\end{align*}
$$

Using the substitution

$$
\sum_{\epsilon} \epsilon_\mu \epsilon^*_\nu
\to -g_{\mu \nu}, \quad
\sum_{\epsilon'} \epsilon'_\mu \epsilon'^*_\nu
\to -g_{\mu \nu}
$$

Then

$$
\begin{align*}
    \frac{1}{2} \sum_{\text{pol.}} 
    |\mathcal{M}|^2
    &= \frac{(eQ)^4}{2} 
    g_{\mu \rho} g_{\sigma \nu}
    T^{\mu \nu} T^{\rho \sigma}
    \\
    &= \frac{(eQ)^4}{2} T^{\mu \nu} T_{\mu \nu}
\end{align*}
$$

Let us evaluate the scalar $T^{\mu \nu} T_{\mu \nu}$:

$$
\begin{align*}
    T^{\mu \nu} T_{\mu \nu}
    &= (2 g^{\mu \nu} - A^{\mu \nu} + B^{\mu \nu})
    (2 g_{\mu \nu} - A_{\mu \nu} + B_{\mu \nu})
    \\
    &= A^{\mu \nu} A_{\mu \nu} + B^{\mu \nu} B_{\mu \nu}
    - 2 A^{\mu \nu} B_{\mu \nu}
    \\ &\quad
    - 4{A^\mu}_\mu + 4{B^\mu}_\mu 
    + 4 \delta^\mu_\mu
\end{align*}
$$

These terms can all be simplified by the following replacements: 

- on-shell conditions

    $$
    p^2 = p'^2 = m^2, \quad
    k^2 = k'^2 = 0
    $$

- inner product replacement (we shall express all inner products using $p\cdot k$ and $p\cdot k'$)

    $$
    \begin{align*}
        p'\cdot k' &= p \cdot k
        \\[0.5em]
        p' \cdot k &= p \cdot k' 
        \\[0.5em]
        p \cdot p' &= p \cdot (p+k-k')
        \\ &= m^2 + p\cdot k - p\cdot k'
        \\[0.5em]
        k \cdot k' 
        &= \frac{1}{2}[k \cdot k' + k \cdot k']
        \\ &= \frac{1}{2}[k\cdot(p+k-p') + (p'+k'-p)\cdot k']
        \\ &= \frac{1}{2}(p\cdot k - p'\cdot k + p'\cdot k' - p\cdot k')
        \\ &= p\cdot k - p\cdot k'
    \end{align*}
    $$

Let us now tackle the terms one by one :

$$
\begin{align*}
    A^{\mu \nu} A_{\mu \nu}
    &= \frac{(2p+k)^2 (2p'+k')^2}{(2p\cdot k)^2}
    \\ &= \frac{(4p^2 + 4p\cdot k)(4p'^2 + 4p'\cdot k')}{4(p\cdot k)^2}
    \\ &= \frac{4(m^2 + p\cdot k)^2}{(p\cdot k)^2}

    \\[2em]

    B^{\mu \nu} B_{\mu \nu}
    &= \frac{(2p'-k)^2 (2p-k')^2}{(2p\cdot k')^2}
    \\ &= \frac{(4p'^2 - 4p'\cdot k)(4p^2 - 4p\cdot k')}{4(p\cdot k')^2}
    \\ &= \frac{4(m^2 - p\cdot k')^2}{(p\cdot k')^2}

    \\[2em]

    A^{\mu \nu} B_{\mu \nu}
    &= \frac{(2p+k)^\mu (2p'-k)_\mu (2p'+k')^\nu (2p-k')_\nu}{(2p\cdot k)(2p\cdot k')}
    \\ &= \frac{
        (4p\cdot p' - 2p\cdot k + 2p'\cdot k)
        (4p\cdot p' - 2p'\cdot k' + 2p\cdot k')
    }{(2p\cdot k)(2p\cdot k')} 
    \\ &= \frac{
        (2m^2 + p\cdot k - p\cdot k')^2
    }{(p\cdot k)(p\cdot k')}

    \\[2em]

    {A^\mu}_\mu
    &= \frac{(2p+k)^\mu (2p'+k')_\mu}{2p\cdot k}
    \\ &= \frac{4p\cdot p' + 2p\cdot k' + 2p'\cdot k + k\cdot k'}{2p\cdot k}
    \\ &= \frac{4m^2 + 5p\cdot k - p\cdot k'}{2p\cdot k}

    \\[2em]

    {B^\mu}_\mu
    &= \frac{(2p'-k)^\mu (2p-k')_\mu}{2p\cdot k'}
    \\ &= \frac{4p\cdot p' - 2p'\cdot k' - 2p\cdot k + k\cdot k'}{2p\cdot k'}
    \\ &= \frac{4m^2 - 5p\cdot k' + p\cdot k}{2p\cdot k'}

    \\[2em]

    \delta^\mu_\mu &= 4
\end{align*}
$$

Putting everything together, finally we obtain

$$
\begin{align*}
    \frac{1}{2} \sum_{\text{pol.}} 
    |\mathcal{M}|^2
    &= 2(eQ)^4 \bigg[
        2 + 2m^2 \left(
            \frac{1}{p\cdot k} - \frac{1}{p\cdot k'}
        \right)
        \\ & \qquad \qquad \quad
        + m^4 \left(
            \frac{1}{p\cdot k} - \frac{1}{p\cdot k'}
        \right)^2
    \bigg]
\end{align*}
$$

### Lorentz Invariant Phase Space

To find the differential cross section, we shall return to the lab frame. Let the scattering angle of the photon be $\theta$, and choose the coordinate system as shown below.

<center>
<img src="images/compton-lab.png" height="150px">
</center>

$$
\def \arraystretch{1.5}
\begin{array}{l|l}
    \text{Initial Momentum} & \text{Final Momentum} \\
    \hline
    k^\mu = \omega(1,0,0,1) & k'^\mu = \omega'(1,\sin \theta,0,\cos \theta)
    \\
    p^\mu = (m,0,0,0) & 
    p'^\mu = (m+\omega-\omega', -\omega' \sin \theta, 0, \omega - \omega' \cos \theta)
\end{array}
$$

Here $\omega, \omega'$ are the frequencies (energies) of the incoming and scattered photon. To find $\omega'$, we use

$$
p'^2 = m^2 
\, \Rightarrow \, 
\omega' = \frac{\omega}{1 + (\omega/m)(1 - \cos \theta)}
$$

Now let us evaluate $d\Pi_2$. By definition

$$
\begin{align*}
    \int d\Pi_2 
    &= \int \frac{d^3 p'}{(2\pi)^3} \frac{1}{2E'_\phi}
    \frac{d^3 k'}{(2\pi)^3} \frac{1}{2E'_\gamma}
    (2\pi)^4 \delta^4(p'+k'-p-k)
    \\
    &= \int \frac{d^3 k'}{(2\pi)^3} 
    \frac{1}{4 E'_\gamma E'_\phi}
    (2\pi) \delta(
        E'_\phi + E'_\gamma - E_\phi - E_\gamma
    )
    \\
    &= \int \frac{\omega'^2 d\omega' d\Omega}{(2\pi)^3} 
    \frac{1}{4 \omega' E'_\phi}
    (2\pi) \delta(
        E'_\phi + E'_\gamma - m - \omega
    )
\end{align*}
$$

Here we changed to spherical polar coordinates, using the fact that momentum $\mathbf{k}'$ has magnitude $\omega'$. To deal with the delta function, let us express $E'_\phi, E'_\gamma$ as functions of $\omega'$ (*without* using energy conservation, since the corresponding delta function has not been removed; but for the same reason, momentum conservation is fine):

$$
\begin{align*}
    E'_\gamma &= \omega'
    \\[0.5em]
    E'_\phi &= \sqrt{|\mathbf{p}'|^2 + m^2}
    \\
    &= \sqrt{(-\omega' \sin \theta)^2 + (\omega - \omega' \cos \theta)^2 + m^2}
    \\
    &= \sqrt{m^2 + \omega^2 + \omega'^2 - 2\omega \omega' \cos \theta}
\end{align*}
$$

Then 

$$
\begin{align*}
    &\int d\omega' \delta(E'_\phi + E'_\gamma - m - \omega)
    \\
    &\to \left|
        \frac{\partial}{\partial \omega'}
        (E'_\phi + E'_\gamma - m - \omega)
    \right|^{-1}
    \\
    &= \left[
        \frac{\omega' - \omega \cos \theta}{E'_\phi}
        + 1
    \right]^{-1}
    \\
    &= \frac{E'_\phi}{\omega' - \omega \cos \theta + E'_\phi}
    \quad (E'_\phi = m + \omega - \omega')
\end{align*}
$$

Now we remove the last delta function and impose energy conservation:

$$
\begin{align*}
    \int d\Pi_2 
    &= \int d\Omega \frac{\omega'^2 }{(2\pi)^3} 
    \frac{1}{4 \omega' E'_\phi}
    (2\pi) \frac{E'_\phi}{\omega' - \omega \cos \theta + E'_\phi}
    \bigg|_{E'_\phi = m + \omega - \omega'}
    \\
    &= \frac{1}{16 \pi^2} \int d\Omega \,
    \frac{\omega'}{m + \omega(1-\cos \theta)}
    \\
    &= \frac{1}{16 \pi^2} \int d\Omega \,
    \frac{\omega'^2}{m \omega}
\end{align*}
$$

### Differential Cross Section

In the lab frame, using

$$
p\cdot k = m \omega \qquad
p\cdot k' = m \omega'
$$

the polarization averaged amplitude becomes

$$
\begin{align*}
    \frac{1}{2} \sum_{\text{pol.}} 
    |\mathcal{M}|^2
    &= 2(eQ)^4 (1 + \cos^2 \theta)
\end{align*}
$$

The differential cross section (in lab frame) to the lowest order is

$$
d\sigma = \frac{1}{2E_\phi 2E_\gamma |v_\phi - v_\gamma|}
\frac{1}{2} \sum_{\text{pol.}} |\mathcal{M}|^2 d\Pi_2
$$

Plugging in

$$
\begin{align*}
    E_\phi = m, \quad E_\gamma = \omega, \quad
    |v_\phi - v_\gamma| = |0 - 1| = 1
    \\[0.5em]
    \alpha = \frac{e^2}{4\pi} \quad \text{(Fine structure constant)}
\end{align*}
$$

Finally

<div class="result">

**Compton Scattering Cross Section in Scalar QED (up to $O(\alpha^2)$):**

$$
\begin{align*}
    \left(\frac{d\sigma}{d\Omega}\right)_\text{lab}
    &= \frac{1}{4m \omega} 2(eQ)^4 (1 + \cos^2 \theta)
    \frac{1}{16 \pi^2} \frac{\omega'^2}{m \omega}
    \\
    &= \frac{\alpha^2 Q^4}{2m^2} 
    \left(\frac{\omega'}{\omega}\right)^2
    (1 + \cos^2 \theta)
\end{align*}
$$

</div><br>

### Low Energy Limit: Thompson Scattering

## Pair Annihilation

The **pair annihilation** refers to the production of two photons $\gamma$ by the annihilation of the "electron"-"positron" pair $\phi$ and $\bar{\phi}$. Let the momenta of the incoming $\phi, \bar{\phi}$ as $p, p'$, and the momenta of the outgoing photons $\gamma$ as $k, k'$. The annihilation process is described as

$$
\phi(p) + \bar{\phi}(p') \to \gamma(k) + \gamma(k')
$$

### Invariant Amplitude $\mathcal{M}$

Pair annihilation involves the following 3 diagrams (to the lowest order):

<center>
<img src="images/pairanni.png" height="200px">
</center>

The amplitudes for each diagram are found to be (used on-shell conditions to simplify the denominator)

$$
\begin{align*}
    i\mathcal{M}_4
    &= i (eQ)^2 \epsilon^*_\mu(k) \epsilon'^*_\nu(k') 2g_{\mu \nu}
    \\[1em]
    i \mathcal{M}_t
    &= \color{green}\epsilon^*_\mu(k)
    ieQ[p + (p-k)]^\mu
    \\ &\quad \color{darkcyan} \times \frac{i}{(p-k)^2 - m^2}
    \color{red} \times ieQ[(k'-p') - p']^\nu \epsilon'^*_\nu(k')
    \\ &= -i (eQ)^2 \epsilon^*_\mu(k) \epsilon'^*_\nu(k')
    \frac{(2p-k)^\mu (2p'-k')^\nu}{2p\cdot k}
    \\[1em]
    i \mathcal{M}_u
    &= \color{green}\epsilon^*_\mu(k)
    ieQ[(k-p')-p']^\mu
    \\ &\quad \color{darkcyan} \times \frac{i}{(p-k')^2 - m^2}
    \color{red} \times ieQ[p + (p-k')]^\nu \epsilon'^*_\nu(k')
    \\ &= -i (eQ)^2 \epsilon^*_\mu(k) \epsilon'^*_\nu(k')
    \frac{(2p'-k)^\mu (2p-k')^\nu}{2p\cdot k'}
\end{align*}
$$

### Side Note: Crossing Symmetry

We discover that the polarization averaged amplitude can be obtained from that of Compton scattering by the replacement

$$
p \to p, \quad p' \to -p', \quad
k \to -k, \quad k' \to k'
$$

Therefore

$$
\begin{align*}
    \frac{1}{2}\sum_{\text{pol.}} |\mathcal{M}|^2
    &= 2(eQ)^4 \bigg[
        2 - 2m^2 \left(
            \frac{1}{p\cdot k} + \frac{1}{p\cdot k'}
        \right)
        \\ & \qquad \qquad \quad
        + m^4 \left(
            \frac{1}{p\cdot k} + \frac{1}{p\cdot k'}
        \right)^2
    \bigg]
\end{align*}
$$

The relation between these two scattering processes $\phi(p) \gamma(k) \to \phi(p') \gamma(k')$ and $\phi(p) \bar{\phi}(p') \to \gamma(k) \gamma(k')$ is called **crossing symmetry**. In general, the *S*-matrix for any process involving a particle with momentum $p$ in the initial state is equal to the *S*-matrix for an otherwise identical process but with an *antiparticle* of momentum $-p$ in the final state:

$$
\mathcal{M}(\phi(p) \cdots \to \cdots)
= \mathcal{M}(\cdots \to \cdots \bar{\phi}(-p))
$$

### Kinetics and Cross Section

To find the differential cross section, we go to the CM frame. Let the scattering angle of the photons be $\theta$, and choose the coordinate system as shown below. 

<center>
<img src="images/pairanni-cm.png" height="150px">
</center>

$$
\def \arraystretch{1.5}
\begin{array}{l|l}
    \text{Initial Momentum} & \text{Final Momentum} \\
    \hline
    p^\mu = (E,0,0,p) & 
    k^\mu = E(1, \sin\theta, 0, \cos\theta)
    \\
    p'^\mu = (E,0,0,-p) & 
    k'^\mu = E(1, - \sin\theta, 0, - \cos\theta)
\end{array}
$$

Here $E$ is the energy of the incoming $\phi, \bar{\phi}$. By conservation of energy, we know that it should also be the energy of the photons. The momentum magnitude $p$ is determined by

$$
E^2 - p^2 = m^2 \, \Rightarrow \,
p \equiv |\mathbf{p}| = \sqrt{E^2 - m^2}
$$

From known results of $2\to 2$ scattering in CM frame, we obtain

$$
\begin{align*}
    \left(\frac{d\sigma}{d\Omega}\right)_\text{CM}
    &= \frac{1}{64\pi^2 E_{\text{CM}}^2} \frac{p_f}{p_i}
    \times \frac{1}{2}\sum_{\text{pol.}}|\mathcal{M}|^2
    \\
    &= \frac{1}{64\pi^2 (2E)^2} \frac{E}{p}
    \times \frac{1}{2}\sum_{\text{pol.}}|\mathcal{M}|^2
    \\
    &= \frac{1}{256\pi^2} \frac{1}{E p} \times
    \frac{1}{2}\sum_{\text{pol.}}|\mathcal{M}|^2
\end{align*}
$$

The polarization averaged amplitude is found by plugging in

$$
\begin{align*}
    p\cdot k &= E (E - p\cos \theta) \\[0.3em]
    p\cdot k'&= E (E + p\cos \theta)
\end{align*} \qquad
(p = \sqrt{E^2 - m^2})
$$

$$
\begin{align*}
    \Rightarrow
    & \, \frac{1}{2}\sum_{\text{pol.}}|\mathcal{M}|^2
    \\
    &= 4(eQ)^4 \bigg[
        1
        - \frac{2 m^2 p \cos^2 \theta}{E (E^2 - p^2 \cos^2 \theta)}
        + \frac{2 m^4 p^2 \cos^2 \theta}{E^2 (E^2 - p^2 \cos^2 \theta)^2}
    \bigg]
\end{align*}
$$

## Pair Creation

The **pair creation** refers to the production of electron-position pair $\phi$ and $\bar{\phi}$ by a high-energy photon pair $\gamma\gamma$. Let the momenta of the incoming photon pair as $k, k'$, and the momenta of the produced $\phi, \bar{\phi}$ pair as $p, p'$. The creation process is described as

$$
\gamma(k) + \gamma(k') \to \phi(p) + \bar{\phi}(p')
$$

### Invariant Amplitude $\mathcal{M}$

Pair creation involves the following 3 diagrams (to the lowest order):

<center>
<img src="images/paircreate.png" height="200px">
</center>

The polarization averaged amplitude can be obtained by the same replacement as in the pair annihilation case. 

### Kinetics and Cross Section

To find the differential cross section, we go to the CM frame. Let the scattering angle of the electron be $\theta$, and choose the coordinate system as shown below. Then

<center>
<img src="images/paircreate-cm.png" height="160px">
</center>

$$
\def \arraystretch{1.5}
\begin{array}{l|l}
    \text{Initial Momentum} & \text{Final Momentum} \\
    \hline
    k^\mu = \omega(1,0,0,1) & 
    p^\mu = (E, p\sin\theta, 0, p\cos\theta)
    \\
    k'^\mu = \omega(1,0,0,-1) & 
    \begin{align*}
        p'^\mu &= (p + p' -k)^\mu
        \\ &= (E, -p\sin\theta, 0, -p\cos\theta)
    \end{align*}
\end{array}
$$

The momentum magnitude $p$ is again determined as usual by $E^2 - p^2 = m^2$. By energy conservation we know that $E = \omega$.

From known results of $2\to 2$ scattering in CM frame, we obtain

$$
\begin{align*}
    \left(\frac{d\sigma}{d\Omega}\right)_\text{CM}
    &= \frac{1}{64\pi^2 E_{\text{CM}}^2} \frac{p_f}{p_i}
    \times \frac{1}{2}\sum_{\text{pol.}}|\mathcal{M}|^2
    \\
    &= \frac{1}{64\pi^2 (2\omega)^2} \frac{p}{\omega}
    \times \frac{1}{2}\sum_{\text{pol.}}|\mathcal{M}|^2
    \\
    &= \frac{1}{256\pi^2} \frac{p}{\omega^3} \times
    \frac{1}{2}\sum_{\text{pol.}}|\mathcal{M}|^2
\end{align*}
$$
