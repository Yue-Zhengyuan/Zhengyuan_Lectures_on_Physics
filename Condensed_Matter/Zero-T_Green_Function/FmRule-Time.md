# Perturbative Expansion of <br>Green's Function

<font size=5>

**Part 1: Time-Dependent Version**

</font>

In the following we illustrate the perturbative expansion of 2-point functions (Green's function, $n = 2$) 

$$
G_{\alpha \beta}(t - t')
\equiv \frac{-i}{\hbar}
\amp{\Psi_0}{T[a_{\alpha H}(t) a^\dagger_{\beta H}(t')]}{\Psi_0}
$$

using a Hamiltonian with two-body interactions (in interaction picture):

$$
\begin{align*}
    V(t) = \frac{1}{2} \sum_{\gamma \delta \epsilon \theta}
    \amp{\gamma \delta}{V}{\epsilon \theta}
    a_\gamma^\dagger(t) a_\delta^\dagger(t)
    a_\theta(t) a_\epsilon(t)
\end{align*}
$$

## Zeroth Order Term

The zeroth order term is just the Green's function in free system:

$$
G_{\alpha \beta}^{(0)} (t - t')
\equiv \frac{-i}{\hbar} 
\amp{0}{T[a_\alpha(t) a^\dagger_\beta(t')]}{0}
$$

We note that since $a_\alpha a^\dagger_\beta$ is already in normal order, the zeroth term is the same as the contraction:

$$
a^\bullet_\alpha(t) a^{\dagger \bullet}_\beta(t')
= i \hbar \, G_{\alpha \beta}^{(0)} (t - t')
$$

The application of Wick's theorem is then made simple.

## First Order Terms

*In the following time integrations, we suppress the limits $\pm (\infty - i\epsilon)$.*

$$
\begin{align*}
    &G^{(1)}_{\alpha \beta}(t - t')
    \\
    &= \left(\frac{-i}{\hbar} \right)^2 \int dt_1 \,
    \amp{0}{T[V(t_1) a_\alpha(t) a^\dagger_\beta(t')]}{0}
    \\
    &= \frac{1}{2} \left(\frac{-i}{\hbar} \right)^2 
    \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\qquad \times
    \amp{0}{T[
        a_\gamma^\dagger(t_1^+) a_\delta^\dagger(t_1^+)
        a_\theta(t_1) a_\epsilon(t_1) 
        a_\alpha(t) a^\dagger_\beta(t')
    ]}{0}
\end{align*}
$$

The notation $t_1^+$ is introduced to indicate the original order of operators in $V$. Now we can apply Wick's theorem: 

$$
T[AB...] = N[AB... + \text{sum of all possible contractions}]
$$

However, note that:

- In the sum of all possible contractions with normal ordering, only those with every operator contracted (*fully* contracted) can have nonzero vacuum expectation value;

- The only nonzero contraction is between an $a$ and an $a^\dagger$, which gives 
    
    $$
    a^\bullet_\alpha(t) a^{\dagger \bullet}_\beta(t')
    = iG_{\alpha \beta}^{(0)} (t - t')
    $$

With these observations, we obtain $3! = 6$ terms (omitting the time in intermediate steps for convenience)

$$
\begin{align*}
    & \amp{0}{T[
        a_\gamma^\dagger(t_1^+) a_\delta^\dagger(t_1^+)
        a_\theta(t_1) a_\epsilon(t_1) 
        a_\alpha(t) a^\dagger_\beta(t')
    ]}{0} \\
    &= \sum_{\sigma \in S_3} \Big[
        a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet \sigma(1)}_\theta a^{\bullet \sigma(2)}_\epsilon 
        a^{\bullet \sigma(3)}_\alpha a^{\dagger \bullet 3}_\beta
        + a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet \sigma(3)}_\theta a^{\bullet \sigma(2)}_\epsilon 
        a^{\bullet \sigma(1)}_\alpha a^{\dagger \bullet 3}_\beta
    \Big]
    \\
    &= \underbrace{
        a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet 1}_\theta a^{\bullet 2}_\epsilon 
        a^{\bullet 3}_\alpha a^{\dagger \bullet 3}_\beta
    }_{(b)}
    + \underbrace{
        a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet 2}_\theta a^{\bullet 3}_\epsilon 
        a^{\bullet 1}_\alpha a^{\dagger \bullet 3}_\beta
    }_{(c)}
    \\ &\quad
    + \underbrace{
        a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet 3}_\theta a^{\bullet 1}_\epsilon 
        a^{\bullet 2}_\alpha a^{\dagger \bullet 3}_\beta
    }_{(e)}
    + \underbrace{
        a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet 3}_\theta a^{\bullet 2}_\epsilon 
        a^{\bullet 1}_\alpha a^{\dagger \bullet 3}_\beta
    }_{(d)}
    \\ &\quad
    + \underbrace{
        a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet 2}_\theta a^{\bullet 1}_\epsilon 
        a^{\bullet 3}_\alpha a^{\dagger \bullet 3}_\beta
    }_{(a)}
    + \underbrace{
        a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
        a^{\bullet 1}_\theta a^{\bullet 3}_\epsilon 
        a^{\bullet 2}_\alpha a^{\dagger \bullet 3}_\beta
    }_{(f)}
\end{align*}
$$

Note that extra minus signs may occur when moving the pairs in a contraction together for fermions. Let us now evaluate each term explicitly, and associate each with a Feynman diagram (the rules will be summarized later):

<div class="imgtext">
<img src="images/2BodyV_1st-1.png" width="150pt">

$$
\quad \begin{align*}
    &\text{Term} \ (a) \\
    &a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
    a^{\bullet 2}_\theta a^{\bullet 1}_\epsilon 
    a^{\bullet 3}_\alpha a^{\dagger \bullet 3}_\beta
    = a^{\bullet 1}_\epsilon a^{\dagger \bullet 1}_\gamma 
    a^{\bullet 2}_\theta a^{\dagger \bullet 2}_\delta 
    a^{\bullet 3}_\alpha a^{\dagger \bullet 3}_\beta
    \\[1em]
    & \Rightarrow 
    \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    G^{(0)}_{\epsilon \gamma}(t_1 - t_1^+) \,
    G^{(0)}_{\theta \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\alpha \beta}(t - t')
\end{align*}
$$

</div><br>

<div class="imgtext">
<img src="images/2BodyV_1st-2.png" width="150pt">

$$
\quad \begin{align*}
    &\text{Term} \ (b) \\
    &a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
    a^{\bullet 1}_\theta a^{\bullet 2}_\epsilon 
    a^{\bullet 3}_\alpha a^{\dagger \bullet 3}_\beta
    = - a^{\bullet 1}_\theta a^{\dagger \bullet 1}_\gamma 
    a^{\bullet 2}_\epsilon a^{\dagger \bullet 2}_\delta 
    a^{\bullet 3}_\alpha a^{\dagger \bullet 3}_\beta
    \\[1em]
    & \Rightarrow 
    - \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    G^{(0)}_{\theta \gamma}(t_1 - t_1^+) \,
    G^{(0)}_{\epsilon \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\alpha \beta}(t - t')
\end{align*}
$$

</div><br>

<div class="imgtext">
<img src="images/2BodyV_1st-3.png" width="150pt">

$$
\quad \begin{align*}
    &\text{Term} \ (c) \\
    &a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
    a^{\bullet 2}_\theta a^{\bullet 3}_\epsilon 
    a^{\bullet 1}_\alpha a^{\dagger \bullet 3}_\beta
    = - a^{\bullet 1}_\alpha a^{\dagger \bullet 1}_\gamma 
    a^{\bullet 2}_\theta a^{\dagger \bullet 2}_\delta 
    a^{\bullet 3}_\epsilon a^{\dagger \bullet 3}_\beta
    \\[1em]
    & \Rightarrow 
    - \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\theta \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\epsilon \beta}(t_1 - t')
\end{align*}
$$

</div><br>

<div class="imgtext">
<img src="images/2BodyV_1st-4.png" width="150pt">

$$
\quad \begin{align*}
    &\text{Term} \ (d) \\
    &a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
    a^{\bullet 3}_\theta a^{\bullet 2}_\epsilon 
    a^{\bullet 1}_\alpha a^{\dagger \bullet 3}_\beta
    = a^{\bullet 1}_\alpha a^{\dagger \bullet 1}_\gamma 
    a^{\bullet 2}_\epsilon a^{\dagger \bullet 2}_\delta 
    a^{\bullet 3}_\theta a^{\dagger \bullet 3}_\beta
    \\[1em]
    & \Rightarrow 
    \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\epsilon \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\theta \beta}(t_1 - t')
\end{align*}
$$

</div><br>

<div class="imgtext">
<img src="images/2BodyV_1st-5.png" width="150pt">

$$
\quad \begin{align*}
    &\text{Term} \ (e) \\
    &a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
    a^{\bullet 3}_\theta a^{\bullet 1}_\epsilon 
    a^{\bullet 2}_\alpha a^{\dagger \bullet 3}_\beta
    = - a^{\bullet 1}_\epsilon a^{\dagger \bullet 1}_\gamma 
    a^{\bullet 2}_\alpha a^{\dagger \bullet 2}_\delta 
    a^{\bullet 3}_\theta a^{\dagger \bullet 3}_\beta
    \\[1em]
    & \Rightarrow 
    - \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    G^{(0)}_{\epsilon \gamma}(t_1 - t_1^+) \,
    G^{(0)}_{\alpha \delta}(t - t_1) \,
    G^{(0)}_{\theta \beta}(t_1 - t')
\end{align*}
$$

</div><br>

<div class="imgtext">
<img src="images/2BodyV_1st-6.png" width="150pt">

$$
\quad \begin{align*}
    &\text{Term} \ (f) \\
    &a^{\dagger \bullet 1}_\gamma a^{\dagger \bullet 2}_\delta
    a^{\bullet 1}_\theta a^{\bullet 3}_\epsilon 
    a^{\bullet 2}_\alpha a^{\dagger \bullet 3}_\beta
    = a^{\bullet 1}_\theta a^{\dagger \bullet 1}_\gamma 
    a^{\bullet 2}_\alpha a^{\dagger \bullet 2}_\delta 
    a^{\bullet 3}_\epsilon a^{\dagger \bullet 3}_\beta
    \\[1em]
    & \Rightarrow 
    \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\quad \times
    G^{(0)}_{\theta \gamma}(t_1 - t_1^+) \,
    G^{(0)}_{\alpha \delta}(t - t_1) \,
    G^{(0)}_{\epsilon \beta}(t_1 - t')
\end{align*}
$$

</div><br>

### Closed Loops and Minus Signs

From the figures we see that if the arrowed lines representing Green's function form a closed loop, then the expression will get a minus sign. This is in general true: the expression will get $(-1)^n$, where $n$ is the number of such loops. 

Of course, these signs are absent for boson. 

### Normalization and Cancellation of Disconnected Diagrams

It turns out that the normalization of $\ket{\Psi_0}$ will cancel the terms with *disconnected diagrams* (a) and (b) (known as the **linked cluster theorem**). Therefore, the true $k$th order term of the Green's function with normalized $\ket{\Psi_0}$ consists of only connected terms.

$$
\begin{align*}
    \frac{1}{k!} \left(\frac{-i}{\hbar}\right)^{k+1}
    &\int dt_1 \cdots dt_k \,
    \\ &\quad
    \amp{0}{T[
        V(t_1) \cdots V(t_k)
        a_\alpha(t) a_\beta^\dagger(t')
    ]}{0}_\text{connected}
\end{align*}
$$

### Equivalent Diagrams

Among the remaining four diagrams, we can see that (c)(e), if without the labels, are (topologically) equivalent diagrams. Looking at the expressions they represent: 

$$
\begin{align*}
    (c) &= - \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\qquad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\theta \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\epsilon \beta}(t_1 - t')
    \\
    (e) &= - \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ &\qquad \times
    G^{(0)}_{\alpha \delta}(t - t_1) \,
    G^{(0)}_{\epsilon \gamma}(t_1 - t_1^+) \,
    G^{(0)}_{\theta \beta}(t_1 - t')
    \\
    &= - \frac{i\hbar}{2} \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\delta \gamma}{V}{\theta \epsilon}
    \\ &\qquad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\theta \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\epsilon \beta}(t_1 - t')
\end{align*}
$$

But we know that $V$ has the symmetry property $V(i,j) = V(j,i)$, i.e.

$$
\amp{\gamma \delta}{V}{\epsilon \theta}
= \amp{\delta \gamma}{V}{\theta \epsilon}
$$

Thus (c) and (e) are in fact equal. The same argument applies to (d) and (f). Thus we can only draw diagrams (c),(d) and add an additional factor of 2, which exactly cancel the 1/2 from Taylor expansion. Such cancellation of the $1/n!$ factor holds at all orders. 

To summarize, the true first order terms are

<div class="result">

**First order terms of Green's function with two-body interaction:**

<div class="imgtext">
<img src="images/2BodyV_1st-3.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1D})}_{\alpha \beta}(t - t') 
    \quad (\text{Direct term})\\
    &= 
    - i\hbar \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ & \quad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\theta \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\epsilon \beta}(t_1 - t')
\end{align*}
$$

</div><br>

<div class="imgtext">
<img src="images/2BodyV_1st-4.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1E})}_{\alpha \beta}(t - t') 
    \quad (\text{Exchange term})\\
    &= 
    i\hbar \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ & \quad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\epsilon \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\theta \beta}(t_1 - t')
\end{align*}
$$

</div><br>

</div><br>

### Summary: Feynman Rules in Time (General Basis)

## In Real (Time-Position) Space

Now we demonstrate how to change to the position basis. Take the direct term as the example:

$$
\begin{align*}
    G^{(1D)}_{\alpha \beta}(t,t')
    &= - i\hbar \sum_{\gamma \delta \epsilon \theta} 
    \int dt_1 \, \amp{\gamma \delta}{V}{\epsilon \theta}
    \\ & \quad \times
    G^{(0)}_{\alpha \gamma}(t - t_1) \,
    G^{(0)}_{\theta \delta}(t_1 - t_1^+) \,
    G^{(0)}_{\epsilon \beta}(t_1 - t')
\end{align*}
$$

- **Conversion of Green's function**

    Let $\ket{\alpha} \to \ket{\mathbf{x},\alpha}, \ket{\beta} \to \ket{\mathbf{x}',\beta}$, we obtain (using 4-positions)

    $$
    \begin{align*}
        G^{(0)}_{\alpha \gamma}(t - t_\gamma)
        &\to G^{(0)}_{\alpha \gamma}(x, x_\gamma)
        \\
        G^{(0)}_{\theta \delta}(t_\theta - t_\delta)
        &\to G^{(0)}_{\theta \delta}(x_\theta - x_\delta)
        \\
        G^{(0)}_{\epsilon \beta}(t_\epsilon - t')
        &\to G^{(0)}_{\epsilon \beta}(x_\epsilon, x')
    \end{align*}
    $$

- **Conversion of $V$ matrix elements**
    
    It is useful to introduce additional time-dependence to the two-body interaction:

    $$
    \begin{align*}
        V(t_1) &= \frac{1}{2} \sum_{\gamma \delta \epsilon \theta}
        \int dt_2 \, dt_3 \, dt_4
        \amp{\gamma \delta}
        {\mathcal{V}(t_1,t_2,t_3,t_4)}{\epsilon \theta}
        \\ &\qquad \qquad \times
        a_\gamma^\dagger(t_1) a_\delta^\dagger(t_2)
        a_\theta(t_4) a_\epsilon(t_3)
        \\[0.5em]
        \amp{\gamma \delta}{\mathcal{V}}{\epsilon \theta}
        &= \delta(t_1 - t_2) \delta(t_2 - t_3) \delta(t_3 - t_4)
        \amp{\gamma \delta}{V}{\epsilon \theta}
    \end{align*}
    $$

    Meanwhile, the change to position + spin basis means the conversion

    $$
    \begin{align*}
        \amp{\gamma \delta}{V}{\epsilon \theta}
        &\to \amp{
            \gamma, \mathbf{x}_\gamma; 
            \delta, \mathbf{x}_\delta
        }{V}{
            \epsilon, \mathbf{x}_\epsilon;
            \theta, \mathbf{x}_\theta
        } \\
        &= \delta^3(\mathbf{x}_\gamma - \mathbf{x}_\epsilon) 
        \delta^3(\mathbf{x}_\delta - \mathbf{x}_\theta)
        \delta_{\gamma \epsilon} \delta_{\delta \theta}
        V(\mathbf{x}_\epsilon, \mathbf{x}_\theta)

        \\[0.6em]

        \sum_{\gamma \delta \epsilon \theta} 
        \int dt_\gamma \, dt_\delta 
        \, dt_\epsilon \, dt_\theta
        &\to \sum_{\gamma \delta \epsilon \theta} 
        \int d^4x_\gamma \, d^4x_\delta 
        \, d^4x_\epsilon \, d^4x_\theta
    \end{align*}
    $$

    Now we see the benefit of introducing the additional delta functions: the time integration are combined with the space integration.

With the general conversion rules, we obtain

$$
\begin{align*}
    G^{(\text{1D})}_{\alpha \beta}(t,t')
    &= - i\hbar \sum_{\gamma \delta \epsilon \theta} 
    \int d^4x_\gamma \, d^4x_\delta 
        \, d^4x_\epsilon \, d^4x_\theta
    \, \amp{\gamma \delta}{U}{\epsilon \theta}
    \\ & \quad \times
    G^{(0)}_{\alpha \gamma}(x, x_\gamma) \,
    G^{(0)}_{\theta \delta}(x_\theta, x_\delta) \,
    G^{(0)}_{\epsilon \beta}(x_\epsilon, x')
\end{align*}
$$

Collecting the $3 + 2 \times 3 = 9$ delta functions we have (including the ones in $\mathcal{V}$), after the integrations (over $4 \times 4 = 16$ variables) we keep 8 integrations and 1 delta function:

$$
\begin{align*}
    &\int d^4x_\gamma \, d^4x_\delta 
    \, d^4x_\epsilon \, d^4x_\theta \,
    \\ & \qquad
    \delta(t_\gamma - t_\delta) 
    \delta(t_\delta - t_\epsilon) 
    \delta(t_\epsilon - t_\theta)
    \delta^3(\mathbf{x}_\gamma - \mathbf{x}_\epsilon) 
    \delta^3(\mathbf{x}_\delta - \mathbf{x}_\theta)
    \\
    &\to \int d^4x_1 \, d^4x_2 \,
    \delta(t_1 - t_2)
\end{align*}
$$

with the constraints

$$
x_\gamma = x_\epsilon \equiv x_1 , \quad
x_\delta = x_\theta \equiv x_2 
$$ 

Here it is understood that

$$
t_\gamma = t_1^+, \quad t_\delta = t_2^+
$$

Assembling these results together, we get the diagram expression in position-time space:

<div class="imgtext">
<img src="images/2BodyV_1st-3xt.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1D})}_{\alpha \beta}(x,x')
    \\
    &= -i\hbar \int d^4 x_1 \, d^4 x_2 \, 
    U_{\gamma \delta, \epsilon \theta}(x_1, x_2)
    \\ &\qquad \times
    G^{(0)}_{\alpha \gamma}(x, x_1) \,
    G^{(0)}_{\theta \delta}(x_2, x_2) \,
    G^{(0)}_{\epsilon \beta}(x_1, x')
    \\[1em]
    &\text{with} \quad
    U_{\gamma \delta, \epsilon \theta}(x_1, x_2)
    \equiv V(\mathbf{x}_1, \mathbf{x}_2) \,
    \delta_{\gamma \epsilon} \delta_{\delta \theta} \,
    \delta(t_1 - t_2)
\end{align*}
$$

</div><br>

<div class="remark">

*Remark*:

- The 4-position-dependent $U$ reveals the *instantaneous property* of the interaction $V$ by the delta function $\delta(t_1 - t_2)$.

- Equal-time Green's functions (arrowed lines with two ends connected on the same interaction line) should be interpreted as

$$
G_{\alpha \beta}^{(0)}(\mathbf{x},t; \mathbf{x}',t)
= G_{\alpha \beta}^{(0)}(\mathbf{x}, t; \mathbf{x}', t^+)
$$

</div><br>

Similarly, the exchange term is converted to

<div class="imgtext">
<img src="images/2BodyV_1st-4xt.png" width="150pt">

$$
\quad \begin{align*}
    &G^{(\text{1E})}_{\alpha \beta}(x,x') 
    \quad (\text{Exchange term})\\
    &= 
    i\hbar \sum_{\gamma \delta \epsilon \theta} 
    \int d^4 x_1 \, d^4 x_2 \, 
    U_{\gamma \delta, \epsilon \theta}(x_1, x_2)
    \\ & \quad \times
    G^{(0)}_{\alpha \gamma}(x,x_1) \,
    G^{(0)}_{\epsilon \delta}(x_1,x_2) \,
    G^{(0)}_{\theta \beta}(x_2, x')
\end{align*}
$$

</div><br>

### Summary: Feynman Rules in Real Space
