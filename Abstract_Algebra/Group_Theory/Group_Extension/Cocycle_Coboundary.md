# Cocycle and Coboundary

## Extension of An Abelian Group

The space group is the extension of the Abelian translation group $K$ (for "kernel") by the point group $Q$ (for "quotient")

$$
1 \to K \xrightarrow{\mu} G \xrightarrow{\pi} Q \to 1
$$ 

This motivates the study the extension of an arbitrary Abelian group $K$ by another generic group $Q$. 

<div class="result">

*Theorem*: Let $\ell$ be a lifting of the above extension.

- For any fixed $x \in Q$, the conjugation mapping in $K$ 

    $$
    \theta_x: K \to K, \quad
    a \mapsto \ell(x) a \ell(x)^{-1}
    $$

    is *independent* of the choice of the lifting $\ell(x)$.

- The following function is a group homomorphism:
    
    $$
    \theta: Q \to \Aut(K), \quad
    x \mapsto \theta_x
    $$

- $K$ is a left $Q$-module with the following scalar multiplication

    $$
    xa = \theta_x(a) = \ell(x) + a - \ell(x)
    $$

</div><br>
