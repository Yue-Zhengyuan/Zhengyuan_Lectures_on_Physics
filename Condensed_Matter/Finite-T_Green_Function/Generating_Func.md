# Finite-*T* Green's Function: <br>Generating Functional (Boson)

## Partition Function with Interaction

Now consider how the interaction $V$ will change the partition function and free. Let

$$
Z_0 = \Tr e^{-\beta H_0} = e^{-\beta F_0}, \quad
Z = \Tr e^{-\beta H} = e^{-\beta F}
$$

It is assumed that $Z_0$ is known. By definition in interaction picture (with $\tau_0 = 0$)

$$
S(\tau,0) = e^{H_0 \tau} U(t, 0)
\ \Rightarrow \ 
U(t, 0) = e^{-H_0 \tau} S(\tau,0)
$$

But recall that $e^{-\beta H} = U(\beta,0)$, therefore

$$
\begin{align*}
    Z &= \Tr [e^{-\beta H_0} S(\beta,0)]
    \\
    &= Z_0 \frac{\Tr [e^{-\beta H_0} S(\beta,0)]}{Z_0}
    \\
    &= Z_0 \expect{S(\beta,0)}_0
\end{align*}
$$

where $\expect{}_0$ means the free ensemble average. With $\Delta F = F - F_0$, we rewrite this result as

<div class="result">

**Partition function with interaction:**

$$
e^{-\beta \Delta F} = \frac{Z}{Z_0}
= \expect{T \exp{\left[
    - \int_{0}^\beta d\tau \, V_I(\tau)
\right]}}_0
$$

</div><br>

## Generating Functional


