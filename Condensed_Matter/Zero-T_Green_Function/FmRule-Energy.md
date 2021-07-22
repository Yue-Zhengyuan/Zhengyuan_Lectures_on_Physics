# Perturbative Expansion of <br>Green's Function

<font size=5>

**Part 2: Energy (Frequency) Version**

</font>

*In this section $\hbar = 1$.*

## Fourier Transform of Time

In this part we Fourier transform the time to obtain the diagram rules in energy formulation

$$
G^{(n)}_{\alpha \beta}(E)
= \int dt \, e^{iEt} G^{(n)}_{\alpha \beta}(t) \quad n = 0,1,2,...
$$

where we need to transform each $G^{(0)}$ appearing in the perturbation expansion of $G^{(n)}$ by

$$
G^{(0)}_{\alpha \beta}(t)
= \int \frac{dE}{2\pi} e^{-iEt} G^{(0)}_{\alpha \beta}(E)
$$

For example, consider the first order direct term:

<div class="imgtext">
<img src="images/2BodyV_1st-3E-mid.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1D})}_{\alpha \beta}(t)
    \\
    &=
    - i \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\theta \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\epsilon \beta}(t_1)
    \\ &\Downarrow \\
    &G^{(\text{1D})}_{\alpha \beta}(E)
    \\
    &= - i \int dt \, e^{iEt} 
    \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    \int \frac{dE_1}{2\pi} e^{-iE_1(t - t_1)}
    G^{(0)}_{\alpha \gamma}(E_1)
    \\ &\quad \times
    \int \frac{dE'}{2\pi} e^{-iE' 0^-}
    G^{(0)}_{\theta \delta}(E')
    \\ &\quad \times
    \int \frac{dE_2}{2\pi} e^{-iE_2 t_1}
    G^{(0)}_{\epsilon \beta}(E_2)
\end{align*}
$$

</div>

<div class="remark">

*Remark*: In general, for each arrowed lines with two ends connected by interaction (including closed loops), we will get an $e^{-iE' 0^-}$ factor (in the following we denote it as $e^{iE'\eta} \, (\eta \to 0^+)$). The limit can be achieved by extending the integral to a contour integral (going to the upper half plane):

$$
\begin{align*}
    \int \frac{dE'}{2\pi} e^{iE'\eta}
    G^{(0)}_{\theta \delta}(E')
    = \oint_{C\uparrow} \frac{dE'}{2\pi} 
    G^{(0)}_{\theta \delta}(E')
\end{align*}
$$

</div><br>

Here we introduced three energies for each Green's function (arrowed lines). First, the integration over $t$ and the intermediate time $t_1$ gives the constraints

$$
E = E_1 = E_2
$$

Then only the integration over the energy $E'$ remains:

<div class="imgtext">
<img src="images/2BodyV_1st-3E.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1D})}_{\alpha \beta}(E)
    = \int dt \, e^{iEt} 
    G^{(\text{1D})}_{\alpha \beta}(t)
    \\
    &= - i 
    \sum_{\gamma \delta \epsilon \theta} 
    \amp{\gamma \delta}{V}{\epsilon \theta}
    G^{(0)}_{\alpha \gamma}(E)
    \\ &\quad \times
    \int \frac{dE'}{2\pi} e^{iE'\eta}
    G^{(0)}_{\theta \delta}(E') \,
    G^{(0)}_{\epsilon \beta}(E)
\end{align*}
$$

</div><br>

For the exchange term, we obtain in a similar fashion:

<div class="imgtext">
<img src="images/2BodyV_1st-4E.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1E})}_{\alpha \beta}(E)
    = \int dt \, e^{iEt} 
    G^{(\text{1E})}_{\alpha \beta}(t)
    \\
    &= - i 
    \sum_{\gamma \delta \epsilon \theta} 
    \amp{\gamma \delta}{V}{\epsilon \theta}
    G^{(0)}_{\alpha \gamma}(E)
    \\ &\quad \times
    \int \frac{dE'}{2\pi} e^{iE'\eta}
    G^{(0)}_{\epsilon \delta}(E') \,
    G^{(0)}_{\theta \beta}(E)
\end{align*}
$$

</div><br>

We notice two properties in the energy version of diagrams: 

- The interaction *conserves energy*:

    <div class="result">

    **Energy conservation in interaction:**

    <div class="imgtext">
    <img src="images/2BodyV_energy.png" width="180pt">

    $$
    \quad \begin{align*}
        E_1 + E_2 &= E_3 + E_4 \\
        E_\text{out} &= E_\text{in}
    \end{align*}
    $$

    </div>
    </div><br>

    <div class="remark">

    *Remark*: 

    - One can *imagine* that energy is *locally conserved at each vertex*, i.e. some energy is transferred from the right to (or from) the left.
    
    - Some terminology on the interaction line

        - If $E_1 = E_3$ and $E_2 = E_4$, then it is called a **direct interaction**;
        - If $E_1 = E_4$ and $E_2 = E_3$, then it is called an **exchange interaction**.

    </div><br>

    ----

    *Proof*: When Fourier transforming each propagators connecting to the interaction line (say at time $t$), the incoming ones will contribute an $e^{-iEt}$, while outgoing ones will contribute an $e^{+iEt}$. Thus we get the expression

    $$
    \begin{align*}
        \int dt \, e^{i(E_1 + E_2 - E_3 - E_4)t}
        &= 2\pi \delta(E_1 + E_2 - E_3 - E_4 )\\
        &= 2\pi \delta(E_\text{out} - E_\text{in})
        \qquad \blacksquare
    \end{align*}
    $$

    ----

    The energy conservation can be better demonstrated in *second order* diagrams. For example, the following second order diagram is expressed as

    <div class="imgtext">
    <img src="images/2BodyV_2nd-9E.png" width="150pt">

    $$
    \quad \begin{align*}
        &G^{(\text{2i})}_{\alpha \beta}(E)
        \\
        &= - i \sum_{\gamma \delta \epsilon \theta} 
        \amp{\gamma \delta}{V}{\epsilon \theta}
        \amp{\zeta \xi}{V}{\lambda \mu}
        G^{(0)}_{\alpha \gamma}(E)
        \\ &\quad \times
        \int \frac{dE_1}{2\pi} \frac{dE_2}{2\pi}
        G^{(0)}_{\epsilon \zeta}(E_1)
        G^{(0)}_{\theta \xi}(E_2)
        G^{(0)}_{\mu \delta}(E_3)
        \\ &\quad \times
        G^{(0)}_{\lambda \beta}(E)
        \\ \\
        &\text{with} \quad E_3 \equiv E_1 + E_2 - E
    \end{align*}
    $$

    </div><br>

- The diagram always starts with a $G^{(0)}(E)$ and ends with another $G^{(0)}(E)$, i.e. the incoming and outgoing propagator has the same energy $E$ specified by the full propagator $G(E)$. 

### Summary: Feynman Rules in Energy (General Basis)

## In Momentum-Energy Space

When using the energy formulation, one usually use the momentum states as the basis states (when translational symmetry exists). We first state the general rules for conversion. For convenience spin indices are omitted in the following; they can always be added back at the final stage if there is no spin interaction. 

- **Conversion of Green's function**

    Since the momentum is now a conserved quantity for each Green's function (as the spin), the orthogonality of different momentum states can be separated out from the propagator: for example

    $$
    G^{(0)}_{\alpha \gamma}(E) \to 
    (2\pi)^3 \delta^3(\mathbf{p}_\alpha - \mathbf{p}_\gamma)
    G^{(0)}(\mathbf{p}_\alpha, E)
    $$

    This delta function will fix the momentum at the two ends of the propagator (arrowed line) to be the same.

- **Conversion of $V$ matrix elements**

    It is trickier to obtain the form of $V$ elements in momentum space, since the translational symmetry of $V$ is best revealed in the *position* space. Let us first find the general form of $V$ in position space (using Schrödinger picture):
    
    $$
    \begin{align*}
        V &= \frac{1}{2} \sum_{\gamma \delta \epsilon \theta}
        a_\gamma^\dagger a_\delta^\dagger
        \amp{\gamma \delta}{V}{\epsilon \theta}
        a_\theta a_\epsilon
        \\
        &\to \frac{1}{2} \int d^3x_1 \, d^3x_2 \,
        d^3x_3 \, d^3x_4 \, \\ &\qquad \qquad
        \phi^\dagger(\mathbf{x}_1) 
        \phi^\dagger(\mathbf{x}_2)
        \amp{\mathbf{x}_1 \mathbf{x}_2}{V}
        {\mathbf{x}_3 \mathbf{x}_4}
        \phi(\mathbf{x}_4) \phi(\mathbf{x}_3)
    \end{align*}
    $$

    Here the translational symmetric matrix element of $V$ is given by

    $$
    \amp{\mathbf{x}_1 \mathbf{x}_2}{V}
    {\mathbf{x}_3 \mathbf{x}_4}
    = \delta^3(\mathbf{x}_1 - \mathbf{x}_3)
    \delta^3(\mathbf{x}_2 - \mathbf{x}_4)
    V(\mathbf{x}_1 - \mathbf{x}_2)
    $$

    Each item can be Fourier transformed (using $\braket{\mathbf{x}}{\mathbf{p}} = e^{i\mathbf{p}\cdot \mathbf{x}}$):

    $$
    \begin{align*}
        \phi^{(\dagger)} (\mathbf{x})
        &= \int \frac{d^3p}{(2\pi)^3} \,
        \braket{\mathbf{x}}{\mathbf{p}}^{(*)} 
        \phi^{(\dagger)} (\mathbf{p})
        = \int \frac{d^3p}{(2\pi)^3} \,
        e^{(-) i\mathbf{p}\cdot \mathbf{x}} 
        \phi^{(\dagger)} (\mathbf{p})
        \\
        \delta^3(\mathbf{x} - \mathbf{x}') 
        &= \int \frac{d^3p}{(2\pi)^3} 
        \braket{\mathbf{x}}{\mathbf{p}}
        \braket{\mathbf{p}}{\mathbf{x}'}
        = \int \frac{d^3p}{(2\pi)^3} 
        e^{i\mathbf{p}\cdot (\mathbf{x} - \mathbf{x}')}
    \end{align*}
    $$

    We also introduce the Fourier component of the function $V(\mathbf{x})$:

    $$
    V(\mathbf{x}) = \int \frac{d^3p}{(2\pi)^3} 
    e^{i\mathbf{p}\cdot \mathbf{x}} V(\mathbf{p})
    $$

    <div class="remark">

    *Remark*: Due to the symmetry $V(\mathbf{x}_1 - \mathbf{x}_2) = V(\mathbf{x}_2 - \mathbf{x}_1)$ (i.e. $V(\mathbf{x})$ is an even function), the Fourier component is also an even function.

    $$
    V(\mathbf{p}) = V(-\mathbf{p})
    $$

    </div><br>

    Collecting these, we obtain
    
    $$
    \begin{align*}
        V &= \frac{1}{2} \int d^3x_1 \, d^3x_2 \,
        d^3x_3 \, d^3x_4 \, 
        \\ &\qquad
        \int \frac{d^3p_1}{(2\pi)^3} \frac{d^3p_2}{(2\pi)^3} \,
        e^{- i\mathbf{p}_1\cdot \mathbf{x}_1} 
        e^{- i\mathbf{p}_2\cdot \mathbf{x}_2} 
        \phi^\dagger (\mathbf{p}_1)
        \phi^\dagger(\mathbf{p}_2)
        \\ &\qquad
        \int \frac{d^3q_1}{(2\pi)^3} \frac{d^3q_2}{(2\pi)^3}
        \frac{d^3q}{(2\pi)^3}
        e^{i\mathbf{q}_1\cdot (\mathbf{x}_1 - \mathbf{x}_3)}
        e^{i\mathbf{q}_2\cdot (\mathbf{x}_2 - \mathbf{x}_4)}
        e^{i\mathbf{q}\cdot (\mathbf{x}_1 - \mathbf{x}_2)} V(\mathbf{q})
        \\ &\qquad
        \int \frac{d^3p_3}{(2\pi)^3} \frac{d^3p_4}{(2\pi)^3} \,
        e^{i\mathbf{p}_3\cdot \mathbf{x}_3} 
        e^{i\mathbf{p}_4\cdot \mathbf{x}_4} 
        \phi(\mathbf{p}_4) \phi(\mathbf{p}_3)
    \end{align*}
    $$

    The integration of the exponential factors over $x_i \, (i = 1,...,4)$ results in:

    $$
    (2\pi)^{3\times 4} \delta^3(\mathbf{q}_1 + \mathbf{q} - \mathbf{p}_1)
    \delta^3(\mathbf{q}_2 - \mathbf{q} - \mathbf{p}_2)
    \delta^3(\mathbf{p}_3 - \mathbf{q}_1)
    \delta^3(\mathbf{p}_4 - \mathbf{q}_2)
    $$

    Then we remove integration over $\mathbf{q}_{1,2}$ and $\mathbf{q}$, getting the restrictions:

    $$
    \mathbf{q}_1 = \mathbf{p}_3, \quad
    \mathbf{q}_2 = \mathbf{p}_4, \quad
    \mathbf{q} = \mathbf{p}_1 - \mathbf{p}_3
    $$

    and there is still one delta function remaining
    
    $$
    (2\pi)^3 \delta^3((\mathbf{p}_1 + \mathbf{p}_2)
    - (\mathbf{p}_3 + \mathbf{p}_4)) \equiv
    (2\pi)^3 \delta^3(\mathbf{p}_{\text{in}} 
    - \mathbf{p}_{\text{out}})
    $$

    It represents *momentum conservation* in the interaction process, as expected from the translational symmetry. Then

    $$
    \begin{align*}
        V &= \frac{1}{2} 
        \int \frac{d^3p_1}{(2\pi)^3} \frac{d^3p_2}{(2\pi)^3}
        \frac{d^3p_3}{(2\pi)^3} \frac{d^3p_4}{(2\pi)^3} 
        \phi^\dagger(\mathbf{p}_1) 
        \phi^\dagger(\mathbf{p}_2)
        \\ &\qquad \quad \times
        V(\mathbf{p}_1 - \mathbf{p}_3)
        (2\pi)^3 \delta^3((\mathbf{p}_1 + \mathbf{p}_2)
        - (\mathbf{p}_3 + \mathbf{p}_4))
        \phi(\mathbf{p}_4) \phi(\mathbf{p}_3)
    \end{align*}
    $$
    
    Comparing with direct change to momentum space:

    $$
    \begin{align*}
        V &= \frac{1}{2} 
        \int \frac{d^3p_1}{(2\pi)^3} \frac{d^3p_2}{(2\pi)^3}
        \frac{d^3p_3}{(2\pi)^3} \frac{d^3p_4}{(2\pi)^3} 
        \\ &\qquad \qquad
        \phi^\dagger(\mathbf{p}_1) 
        \phi^\dagger(\mathbf{p}_2)
        \amp{\mathbf{p}_1 \mathbf{p}_2}{V}
        {\mathbf{p}_3 \mathbf{p}_4}
        \phi(\mathbf{p}_4) \phi(\mathbf{p}_3)
    \end{align*}
    $$

    we find

    <div class="result">
    
    **Matrix elements of $V$ in momentum space:**

    <div class="imgtext">
    <img src="images/2BodyV_momentum.png" width="180pt">

    $$
    \quad \begin{align*}
        &\amp{\mathbf{p}_1 \mathbf{p}_2}{V}
        {\mathbf{p}_3 \mathbf{p}_4} 
        \\
        &= V(\mathbf{p}_1 - \mathbf{p}_3) 
        \\ &\quad \times
        (2\pi)^3 \delta^3((\mathbf{p}_1 + \mathbf{p}_2)
        - (\mathbf{p}_3 + \mathbf{p}_4))
    \end{align*}
    $$

    </div><br>

    </div><br>

    The momentum $\mathbf{q} = \mathbf{p}_1 - \mathbf{p}_3$ can be regarded as the momentum transferred from one vertex to the other, as illustrated in the diagram representation above. This can be combined with energy conservation, yielding *4-momentum conservation* at the interaction line.

We demonstrate this conversion using the first order exchange term, which will show the momentum transfer clearly.

<div class="imgtext">
<img src="images/2BodyV_1st-4E.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1E})}_{\alpha \beta}(E) \\
    &= i 
    \sum_{\gamma \delta \epsilon \theta} 
    \amp{\gamma \delta}{V}{\epsilon \theta}
    G^{(0)}_{\alpha \gamma}(E) \,
    \\ &\quad \times
    \int \frac{dE'}{2\pi} e^{iE'\eta}
    G^{(0)}_{\epsilon \delta}(E') \,
    G^{(0)}_{\theta \beta}(E)
\end{align*}
$$

</div><br>

Using the conversion rules stated above (and $\gamma,\delta,\epsilon,\theta \to 1,2,3,4$), we obtain (let $\mathbf{p}_\alpha = \mathbf{p}$)

$$
\begin{align*}
    G^{(\text{1D})}_{\alpha \beta}
    (\mathbf{p},\mathbf{p}_\beta;E) 
    &= - i 
    \int \frac{d^3p_1}{(2\pi)^3} \frac{d^3p_2}{(2\pi)^3}
    \frac{d^3p_3}{(2\pi)^3} \frac{d^3p_4}{(2\pi)^3} 
    \\ &\quad \times
    V(\mathbf{p}_1 - \mathbf{p}_3) 
    (2\pi)^3 \delta^3((\mathbf{p}_1 + \mathbf{p}_2)
    - (\mathbf{p}_3 + \mathbf{p}_4))
    \\ &\quad \times
    (2\pi)^3 \delta^3(\mathbf{p} - \mathbf{p}_1)
    (2\pi)^3 \delta^3(\mathbf{p}_3 - \mathbf{p}_2)
    (2\pi)^3 \delta^3(\mathbf{p}_4 - \mathbf{p}_\beta)
    \\ &\quad \times
    \int \frac{dE'}{2\pi}
    G^{(0)}(\mathbf{p}, E)
    e^{iE'\eta} G^{(0)}(\mathbf{p}_3, E')
    G^{(0)}(\mathbf{p}_4, E)
\end{align*}
$$

The momentum delta functions (except the one from $V$) impose the following constraints:

$$
\mathbf{p} = \mathbf{p}_1, \quad
\mathbf{p}_2 = \mathbf{p}_3, \quad
\mathbf{p}_4 = \mathbf{p}_\beta
$$

Then we only have integration over $\mathbf{p}_2$ (now rename it to $\mathbf{p}'$) remaining. Introducing the 4-momenta

$$
(\mathbf{p},E) = p, \quad
(\mathbf{p}',E') = p'
$$

and the 4-momentum dependent potential

$$
U(p) \equiv V(\mathbf{p})
$$

<div class="remark">

*Remark*: The real space version of $U(p)$ is ($px \equiv Et - \mathbf{p}\cdot \mathbf{x}$)

$$
\begin{align*}
    U(x - x') &= \int \frac{d^4p}{(2\pi)^4}
    e^{-ip(x - x')} U(p) \\
    &= \int \frac{dE}{2\pi} e^{-iE(t - t')} 
    \int \frac{d^3p}{(2\pi)^3} 
    e^{i\mathbf{p}\cdot (\mathbf{x} - \mathbf{x}')} 
    V(\mathbf{p}) \\
    &= \delta(t - t') V(\mathbf{x} - \mathbf{x}')
\end{align*}
$$

The extra delta function means that $U$ is an *instantaneous* interaction.

</div><br>

we obtain

$$
\begin{align*}
    G^{(\text{1D})}_{\alpha \beta}
    (\mathbf{p},\mathbf{p}_\beta;E) 
    &= i (2\pi)^3 \delta^3(\mathbf{p} - \mathbf{p}_\beta)
    \\ &\quad \times
    \int \frac{d^4p'}{(2\pi)^4} U(p - p')
    G^{(0)}(p)  e^{iE'\eta} G^{(0)}(p') G^{(0)}(p)
    \\
    &= (2\pi)^3 \delta^3(\mathbf{p} - \mathbf{p}_\beta)
    G^{(\text{1D})}_{\alpha \beta}(p)
\end{align*}
$$

Usually we only keep $G^{(\text{1D})}_{\alpha \beta}(p)$; putting the spin indices back, the final expression is

<div class="imgtext">
<img src="images/2BodyV_1st-4pE.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1D})}_{\alpha \beta}(p) 
    \\
    &= i \sum_{\gamma \delta \epsilon \theta} 
    \int \frac{d^4p'}{(2\pi)^4} 
    U_{\gamma \delta, \epsilon \theta}(p - p') 
    \\ &\qquad \quad \quad \times
    G^{(0)}_{\alpha \gamma}(p) 
    e^{iE'\eta} G^{(0)}_{\theta \delta}(p') 
    G^{(0)}_{\epsilon \beta}(p)
    \\[1.5em]
    &\text{with} \quad
    \begin{align*}
        U_{\gamma \delta, \epsilon \theta}(p)
        &= \delta_{\gamma \epsilon} \delta_{\delta \theta}
        U(p) \\
        G^{(0)}_{\alpha \beta}(p) 
        &= \delta_{\alpha \beta} G^{(0)}(p)
    \end{align*}
\end{align*}
$$

</div>

For the direct interaction, there is no momentum transfer along the interaction line:

<div class="imgtext">
<img src="images/2BodyV_1st-3pE.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1D})}_{\alpha \beta}(p) 
    \\
    &= - i \sum_{\gamma \delta \epsilon \theta} 
    \int \frac{d^4p'}{(2\pi)^4} 
    U_{\gamma \delta, \epsilon \theta}(0) 
    \\ &\qquad \quad \quad \times
    G^{(0)}_{\alpha \gamma}(p) 
    e^{iE'\eta} G^{(0)}_{\theta \delta}(p') 
    G^{(0)}_{\epsilon \beta}(p)
\end{align*}
$$

</div><br>

### Summary: Feynman Rules in Energy-Momentum Space
