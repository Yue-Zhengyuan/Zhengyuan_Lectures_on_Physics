# Thermodynamic Quantities

For simplicity, we let $\rho$ be the *normalized* density matrix:

$$
\rho = \frac{e^{-\beta H}}{\Tr e^{-\beta H}}
= e^{-\beta (H - F)}
$$

so that the ensemble average of an operator $O$ is directly given by

$$
\expect{O} = \Tr (\rho O)
$$

## Examples of Thermodynamic Quantities

### Particle Number

$$
\expect{N} = \sum_\alpha 
\expect{c^\dagger_\alpha c_\alpha}
$$

The number operator is related to the Green's function by

$$
\begin{align*}
    \mathcal{G}_{\alpha \alpha}(\tau-\tau^+)
    &= -\expect{T [c_{\alpha H}(\tau) c_{\alpha H}^\dagger(\tau^+)]} \\
    &= \mp \expect{
        c_{\alpha H}^\dagger(\tau^+)
        c_{\alpha H}(\tau)
    } \\
    &= \mp \expect{
        e^{H\tau^+} c_\alpha^\dagger c_\alpha e^{-H\tau}
    }
\end{align*}
$$

Here we used the definition of Heisenberg picture operators

$$
O_H(\tau) = e^{H\tau} O e^{-H\tau}
$$

Due to the cyclic property of trace, the two exponential factors cancel out. Thus we are left with

$$
\mathcal{G}_{\alpha \alpha}(\tau-\tau^+)
= \mp \expect{c_\alpha^\dagger c_\alpha}
$$

Finally, simply writing $\tau - \tau^+$ as $0^+$, we get

<div class="result">

**Ensemble average of particle number $N$:**

$$
\expect{N} = \sum_{\alpha} 
\mathcal{G}_{\alpha \alpha}(0^+)
$$

</div><br>

### One-Body Operators

### Two-Body Operators (Equation of Motion Method)

### Free Energy (Thermodynamic Potential)
