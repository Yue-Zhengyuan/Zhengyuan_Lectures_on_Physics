# Euclidean Formalism

In statistical physics, people usually define all correlation functions in *imaginary time*, and then perform the **Wick rotation**

$$
\tau = it \in \mathbb{R}
$$

We define the **Euclidean Lagrangian** as

$$
\begin{align*}
    L_E \left(\phi, \frac{dx}{d\tau}, \tau\right)
    &= - \left.
    L \left(\phi, \frac{dx}{dt}, t \right)
    \right|_{t \to -i\tau}
    \\
    &= - L \left(\phi, i \, \frac{dx}{d\tau}, -i\tau \right)
\end{align*}
$$

and the **Euclidean action** as

$$
S_E[\phi(\tau)] = \int d\tau \, L_E
$$

Then the usual action $S$ is related to $S_E$ by

$$
S = \int dt \, L
= -i \int d\tau \, (-L_E) = i S_E
$$

Therefore, the imaginary time correlation function is

$$
\langle \phi(\tau_1) \cdots \phi(\tau_n) \rangle
= \frac{
    \int [dx] \, \phi(\tau_1) \cdots \phi(\tau_n)
    \exp(- S_E[\phi(\tau)])
}{
    \int [dx] \, \exp(- S_E[\phi(\tau)])
}
$$