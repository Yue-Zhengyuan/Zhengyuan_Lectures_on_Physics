# Group Extension

The goal of the theory of group extension is to study how a group can be constructed from a *normal subgroup* and its *quotient group*.

*Definition*: Let $K, Q$ be two groups.

- **Group extension** of $K$ by $Q$: K group $G$ (in general *not unique*) related to $K$ (for "kernel") and $Q$ (for "quotient") by a short exact sequence 
    
    $$
    1 \to K \xrightarrow{\mu} G 
    \xrightarrow{\pi} Q \to 1 \quad
    (\im \mu = \ker \pi)
    $$

    The mapping $\mu$ is *injective*, and $\pi$ is *surjective*.

- **Kernel** of the extension: the group $K$

<div class="result">

*Theorem*: Define $M \equiv \im \mu = \ker \pi$.

- $M \cong K$ and $M \lhd G$
- $Q \cong G/M$.

</div>

----

*Proof*: 

- Simply note that:
    - The monomorphism $\mu$ restricted to $K \to \mu(K) \le G$ is an isomorphism.
    - Since $\pi:G \to Q$ is a homomorphism, we have $\ker \pi = M \lhd G$. 

- This follows directly from the first isomorphism theorem $\im \pi \cong G / \ker \pi$:

    - $\pi$ is surjective ($\im \pi = Q$) 
    - The exact sequence requires $\ker \pi = \im \mu = \mu(K)$

    Thus we obtain $Q \cong G/\mu(K)$. $\blacksquare$

----

<div class="remark">

*Remark*: From the properties above, we can colloquially define the extension of $K$ by $Q$ as a group $G$ containing a *normal subgroup* $M \lhd G$ such that

$$
M \cong K \quad \text{and} \quad G/M \cong Q
$$

In many cases $K$ is already a normal subgroup of $G$. 

</div><br>

## Lifting and Transversal

*Definition*: Consider the group extension

$$
1 \to K \xrightarrow{\mu} G 
\xrightarrow{\pi} Q \to 1 \quad
(\im \mu = \ker \pi)
$$

- **Lifting**: a reverse mapping $\ell: Q \to G$ of $\pi$, such that $\pi \ell = 1$.

<div class="remark">

*Remark*: The lifting is not necessarily a group homomorphism, and may not be unique. 

</div><br>

Next, we further assume that $K$ is already a subgroup of $G$.

- **Right transversal** of $K$: a complete set of representatives of right cosets of $K$, i.e. a subset $T \subset G$ consisting of exactly one element from each right coset of $K$ in $G$. For $K$ itself, we choose the representative as the identity.

These two concepts are closely related.

## Split Extension

*Definition*:

- **Split extension**:

## Equivalent Extensions

- **Equivalence of group extensions**: an equivalence relation defined by the existence of a commutative diagram between two group extensions (double line means the identity mapping)

    $$
    \begin{CD}
        1 @>>> K @>{\mu}>> G @>{\pi}>> Q @>>> 1
        \\
        @. @| @VV{\varphi}V @| @.
        \\
        1 @>>> K @>>{\mu'}> G' @>>{\pi'}> Q @>>> 1
    \end{CD}
    $$

    where $\varphi: G \to G'$ is a group *homomorphism*.
