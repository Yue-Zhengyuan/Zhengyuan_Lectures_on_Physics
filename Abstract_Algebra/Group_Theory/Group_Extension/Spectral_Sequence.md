# Spectral Sequence

A **spectral sequence** is a means of computing homology groups by taking successive approximations, which is a generalization of the concept of exact sequences.

*Definition*:

- **Filtration** of Abelian groups:

- **Cohomologcial spectral sequence**: the collection of the following objects:

    $$
    \begin{array}{c|c}
        \text{Objects} & \text{Description}
        \\[4pt] \hline \\[-6pt]
        \text{Abelian groups} &
        E_r^{p,q} \ (p,q,r \in \Z; r \ge 2)
        \\[4pt] \hline \\[-6pt]
        \text{Group homomorphisms} & 
        d_r^{p,q}: E_r^{p,q} \to E_r^{p-r,q+r-1}
        \\[4pt] \hline \\[-6pt]
        \text{Filtered Abelian groups} &
        E^n \ (n \in \Z)
    \end{array}
    $$

    
