# The *S*-Matrix

## Cross Section

Consider a target of particles of type $A$ moving with velocity $v_A$, with density $\rho_A$ (particles per unit volume). We then shoot at it a bunch of particles of type $B$, with number density $\rho_B$ and velocity $v_B$ (parallel to $v_A$; this is always the case if we go to the center-of-mass frame).

<center>
<img src="images/scattering.png" width=400pt>
</center>

Particles $B$ will be scattered by particles $A$. Let: 

- $n$ be the number of incoming $B$ particles *per unit area* of the beam cross section that will go into the beam of $A$;
- $N$ be the *total* number of scattered $B$ particles.

The **cross section** of scattering is defined as

$$
\sigma = \frac{N}{n} = \frac{N}{\Phi_B T}
$$

- $\Phi_B = \rho_B|v_A - v_B|$ is the flux of $B$ *relative to $A$*; the volume density $\rho_B$ is assumed to be uniform everywhere in the $B$ beam;
- $T$ is the experiment time, which is assumed to be large but finite. 

We see that $\sigma$ has the dimension of area, hence its name. 

If we are only interested in the particles $B$ (with number $dN$) that falls in a differential region of parameters (say the phase space $d\Pi$), we also use the **differential cross section**

$$
d\sigma = \frac{dN}{n} 
= \frac{dN}{\rho_B|v_A - v_B| T}
$$

We can reexpress $d\sigma$ using the **scattering probability**. Let $dP$ be the probability that one particle $B$ will be scattered to the desired differential region of parameters from some given initial state. Then the (differential) number of scattered $B$ particles is just

$$
dN = \rho_B V \, dP
$$

For convenience, we assume that our scattering experiment is confined in a finite volume $V$. Then $\rho_B V$ is simply the *total* number of particles $B$ *all over the experiment space*. Therefore

$$
d\sigma = \frac{\rho_B V dP}{\rho_B|v_A - v_B| T}
= \frac{V}{|v_A - v_B| T} dP
$$

## *S*-Matrix and Scattering Probability

The scattering probability $dP$ can be related to the so-called ***S*-matrix**. 

Let $|\psi,t\rangle$ be the Schrödinger picture state at time $t$; its Heisenberg picture counterpart is simply denoted by $|\psi\rangle$.

The *free* states at $t = \pm \infty$ are called **asymptotic states**. The ***S*-matrix** describes the amplitude to go from $t = -\infty$ to $t = +\infty$:

$$
S_{fi} 
= \langle f|S|i \rangle
\equiv \langle f, + \infty | i,-\infty \rangle
$$

For free theory, $S = 1$. Thus for a general theory, we write

$$
S = 1 + i T
$$

where $T$ is the **transfer matrix**. Since $S$ should vanish unless the total 4-momentum is conserved, we normalize $T$ as

$$
i T = i \mathcal{M}
(2\pi)^4 \delta^4(\textstyle{\sum p_f - \sum p_i})
$$

where $\mathcal{M}$ is called the **invariant matrix element**, which is the one that actually encodes useful information. 

With *S*-matrix, the probability $dP$ that one particle $B$ will be scattered into $|f\rangle$ *and* fall in the momentum phase space $d\Pi$ (momentum states are uniformly distributed) is given by the product

$$
dP = \frac{|S_{fi}|^2}{
    \langle f|f \rangle
    \langle i|i \rangle
} d\Pi
$$

We now investigate each part of this $dP$:

- The normalization of the states $\langle f|f \rangle, \langle i|i \rangle$ should be treated carefully. Usually, the initial and final states will be chosen as the momentum eigenstates. For example, we write for $2 \to n$ scattering
    
    $$
    \begin{align*}
        |i\rangle &= |\mathbf{p}_A, \mathbf{p}_B\rangle
        = |\mathbf{p}_A\rangle \otimes |\mathbf{p}_B\rangle
        \\
        |f\rangle &= |\mathbf{p}_1, ..., \mathbf{p}_n \rangle
        = |\mathbf{p}_1\rangle \otimes \cdots \otimes |\mathbf{p}_n\rangle
    \end{align*}
    $$

    Recall that in relativistic field theory, the momentum eigenstates are defined as

    $$
    |\mathbf{p}\rangle = \sqrt{2E_\mathbf{p}} a_\mathbf{p}^\dagger |0\rangle
    $$

    Therefore, its norm is

    $$
    \begin{align*}
        \langle \mathbf{p} | \mathbf{p} \rangle
        &= 2E_\mathbf{p} 
        \langle 0| a_\mathbf{p} a_\mathbf{p}^\dagger |0\rangle
        \\
        &= 2E_\mathbf{p} 
        \langle 0| [a_\mathbf{p} a_\mathbf{p}^\dagger] + a_\mathbf{p}^\dagger a_\mathbf{p} |0\rangle
        \\
        &= 2E_\mathbf{p} (2\pi)^3 \delta^3(0)
    \end{align*}
    $$

    which seems to be unphysical. However, with the finite volume (and the experiment time $T$), using

    $$
    \int \frac{d^3p}{(2\pi)^3} f(\mathbf{p})
    \to \frac{1}{V} \sum_\mathbf{p} f(\mathbf{p})
    $$

    the space delta functions can be regulated to

    $$
    \delta^3(\mathbf{p} - \mathbf{p}') 
    \to \frac{V}{(2\pi)^3} \delta_{\mathbf{p} \mathbf{p}'}
    $$

    We now can write

    $$
    \begin{align*}
        \langle i | i \rangle
        &= (2E_A V) (2E_B V) 
        \\
        \langle f | f \rangle
        &= (2E_1 V) \cdots (2E_n V)
    \end{align*}
    $$

    We shall see that the $V$ factors will eventually cancel each other

- The norm $|S_{fi}|^2$ can be expressed using the invariant amplitude $\mathcal{M}$:
    
    $$
    |S_{fi}|^2
    = |1_{fi} + iT_{fi}|^2
    $$

    Since we are usually not interested in the trivial case $|i\rangle = |f\rangle$ (no scattering at all), the identity part plays no role:

    $$
    \begin{align*}
        |S_{fi}|^2
        &= |T_{fi}|^2
        \\
        &= |\mathcal{M}_{fi}|^2 [
            (2\pi)^4 \delta^4(\textstyle{\sum p_f - \sum p_i})
        ]^2
    \end{align*}
    $$

    The square of delta function is interpreted as follows:

    - The first one is maintained to ensure momentum conservation, so the other is constrained to $(2\pi)^4 \delta^4(0)$
    
    - The finite volume regulation of it is
        $$
        \delta^4(0) = \frac{TV}{(2\pi)^4}
        $$
    
    Therefore

    $$
    |S_{fi}|^2 
    = T V |\mathcal{M}_{fi}|^2 (2\pi)^4 
    \delta^4(\textstyle{\sum p_f - \sum p_i})
    $$

- The final (outcome) phase space element is integrated all over the experimental space:

    $$
    d\Pi = \int_V
    \prod_{f=1}^n \frac{d^3x_f \, d^3p_f}{(2\pi)^3}
    = \prod_{f=1}^n \left[
        \frac{V}{(2\pi)^3} d^3 p_f
    \right]
    $$

    where $V$ is the volume of the experiment space.

Combine all these together, we obtain

$$
\begin{align*}
    dP &= \frac{
        T V (2\pi)^4 \delta^4(\textstyle{\sum p_f - \sum p_i})
    }{
        (2E_A V) (2E_B V) \prod_f (2E_f V)
    }
    |\mathcal{M}_{fi}|^2
    \prod_{f=1}^n \left[
        \frac{V}{(2\pi)^3} d^3 p_f
    \right]
    \\
    &= \frac{T}{V} \frac{1}{2E_A 2E_B}
    |\mathcal{M}_{fi}|^2 d\Pi_n
\end{align*}
$$

where we introduced the structure

$$
d\Pi_n 
\equiv
\left[
    \prod_{f=1}^n \frac{d^3 p_f}{(2\pi)^3} \frac{1}{2E_f}
\right] 
(2\pi)^4 \delta^4(\textstyle{\sum p_i - \sum p_f}) 
$$

It is called the **Lorentz invariant $n$-body phase space element**. 

Finally, plugging it into $d\sigma$, the factors $T,V$ cancel out, and we arrive at

<div class="result">

**$2\to n$ Scattering Differential Cross Section (Any Frame):**

$$
d\sigma 
= \frac{|\mathcal{M}_{fi}|^2}{2E_A 2E_B|v_A - v_B|}
d\Pi_n
$$

</div><br>

### Effect of Identical Particles



## Special Cases of Cross Section

### $2\to 2$ Scattering in CM Frame

We consider the special case of $2 \to 2$ scattering (of massive particles) in the center-of-mass reference frame, in which

$$
\begin{align*}
    \mathbf{p}_A + \mathbf{p}_B 
    &= \mathbf{p}_1 + \mathbf{p}_2 = 0
    \\
    E_A + E_B 
    &= E_1 + E_2 = E_\text{CM}
\end{align*}
$$

Thus we can set the final and the initial momenta as

$$
p_f \equiv |\mathbf{p}_1| = |\mathbf{p}_2|
\qquad
p_i \equiv |\mathbf{p}_A| = |\mathbf{p}_B|
$$

Now we calculate the final 2-body phase space

$$
\int d\Pi_2
= \int \frac{d^3 p_1}{(2\pi)^3}
\frac{d^3 p_2}{(2\pi)^3} 
\frac{1}{2E_1 2E_2}
(2\pi)^4 \delta^4(\textstyle{\sum p_i - \sum p_f}) 
$$

- First, we eliminate the integration over $\mathbf{p}_2 = -\mathbf{p}_1$ using the 3D part of the delta function:
    
    $$
    \int d\Pi_2
    = \int \frac{d^3 p_f}{(2\pi)^3} \left[
        \frac{1}{2E_1 2E_2} 
        (2\pi) \delta(E_\text{CM} - E_1 - E_2)
    \right]
    $$

- The rest of the integral is evaluated using the spherical polar coordinate:
    
    $$
    \int d\Pi_2
    = \int \frac{d\Omega \, dp_f}{(2\pi)^3}
    \frac{p_f^2}{2E_1 2E_2} 
    (2\pi) \delta(E_1 + E_2 - E_\text{CM})
    $$

    Express $E_1, E_2$ as functions of $p_f$:

    $$
    E_1 = \sqrt{m_1 + p_f^2}, \quad E_2 = \sqrt{m_2 + p_f^2}
    $$

    Then

    $$
    \begin{align*}
        &\int dp_f \delta(E_1 + E_2 - E_\text{CM})
        \\ &\to \left|
            \frac{\partial}{\partial p_f}
            (E_1 + E_2 - E_\text{CM})
        \right|^{-1}_{E_1+E_2=E_\text{CM}}
        \\ &= \left(
            \frac{p_f}{E_1} + \frac{p_f}{E_2}
        \right)^{-1}_{E_1+E_2=E_\text{CM}}
    \end{align*}
    $$

Putting these together:

<div class="result">

**2-Particle Phase Space $d\Pi_2$ in CM Frame:**

$$
\begin{align*}
    \int d\Pi_2
    &= \int \frac{d\Omega}{(2\pi)^2} \left[
        \frac{p_f^2}{2E_1 2E_2} 
        \left(
            \frac{p_f}{E_1} + \frac{p_f}{E_2}
        \right)^{-1}
    \right]_{E_1+E_2=E_\text{CM}}
    \\
    &= \int d\Omega \, 
    \frac{p_f}{16\pi^2 E_\text{CM}}
\end{align*}
$$

</div><br>

Besides, the relative velocity factor can also be simplified to

$$
\begin{align*}
    |v_A - v_B| &= \left|
        \frac{|\mathbf{p}_A|}{E_A}
        + \frac{|\mathbf{p}_B|}{E_B}
    \right|
    \\
    &= \frac{p_i}{E_A} + \frac{p_i}{E_B}
    = \frac{p_i (E_A + E_B)}{E_A E_B}
    \\
    &= \frac{p_i E_\text{CM}}{E_A E_B}
\end{align*}
$$

Finally, the cross section is

<div class="result">

**Two Massive Particles to Another Two in CM Frame:**

$$
\left( \frac{d\sigma}{d\Omega} \right)_\text{CM}
= \frac{1}{64 \pi^2 E_\text{CM}^2} 
\frac{p_f}{p_i}
|\mathcal{M}_{fi}|^2
$$

</div><br>

### Identical Particle $2\to 2$ Scattering

If all the four particles are *identical*, in the CM frame

$$
|\mathbf{p}_A| = |\mathbf{p}_B|
= |\mathbf{p}_1| = |\mathbf{p}_2|
$$

The formula then further simplifies to

$$
\left( \frac{d\sigma}{d\Omega} \right)_\text{CM}
= \frac{|\mathcal{M}|^2}{64 \pi^2 E_\text{CM}^2}
$$

## The Decay Rate

The **decay rate** $\Gamma$ of an unstable particle $A$ (assumed to be *at rest*) is defined as

$$
\Gamma = \frac{
    \text{Number of decays per unit time}
}{
    \text{Number of remaining $A$ particles}
}
$$

The decay process can be formally regarded as $1 \to n$ scattering:

$$
|i\rangle = |\mathbf{p}_A = 0 \rangle
$$

We shall solve this problem in the CM frame. In this frame, the particle $A$ is at rest, and $E_A = m_A$. Similar to the derivation above, the probability that a particle $A$ will decay into $n$ particles within some differential region of parameters is

$$
\begin{align*}
    dP &= \frac{
        T V (2\pi)^4 \delta^4(\textstyle{\sum p_f - \sum p_i})
    }{
        (2E_A V) \prod_f (2E_f V)
    }
    |\mathcal{M}_{fi}|^2
    \prod_{f=1}^n \left[
        \frac{V}{(2\pi)^3} d^3 p_f
    \right]
    \\
    &= \frac{T}{2m_A}
    |\mathcal{M}_{fi}|^2 d\Pi_n
\end{align*}
$$

The differential decay rate is then

<div class="result">

**Differential Decay Rate in CM Frame:**

$$
d\Gamma = \frac{dP}{T}
= \frac{1}{2m_A}
|\mathcal{M}_{fi}|^2 d\Pi_n
$$

</div><br>

### Special Case: $1 \to 2$ Decay

