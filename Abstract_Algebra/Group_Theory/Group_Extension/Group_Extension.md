# Group Extension

The goal of the theory of group extension is to show how a group can be constructed from a *normal subgroup* and its *quotient group*.

*Definition*: Let $A, B$ be two groups.

- **Group extension** of $A$ by $B$: A group $G$ related (*not uniquely*) to $A,B$ by a short exact sequence 
    
    $$
    1 \to A \xrightarrow{\mu} G 
    \xrightarrow{\pi} B \to 1 \quad
    (\im \mu = \ker \pi)
    $$

    The mapping $\mu$ is *injective*, and $\pi$ is *surjective*.

- **Kernel** of the extension: the group $A$

- **Equivalence of group extensions**: an equivalence relation defined by the existence of a commutative diagram between two group extensions (double line means the identity mapping)

    $$
    \begin{CD}
        1 @>>> A @>{\mu}>> G @>{\pi}>> B @>>> 1
        \\
        @. @| @VV{\varphi}V @| @.
        \\
        1 @>>> A @>>{\mu'}> G' @>>{\pi'}> B @>>> 1
    \end{CD}
    $$

    where $\varphi: G \to G'$ is a group *homomorphism*.

<div class="result">

*Theorem*: Define $M \equiv \im \mu = \ker \pi$.

- $M \cong A$ and $M \lhd G$
- $B \cong G/M$.
- Extensions of $A$ by $B$ always exists. 

</div>

----

*Proof*: 

- Simply note that:
    - The monomorphism $\mu$ restricted to $A \to \mu(A) \subset G$ is an isomorphism.
    - Since $\pi:G \to B$ is a homomorphism, we have $\ker \pi = M \lhd G$. 

- This follows directly from the first isomorphism theorem $\im \pi \cong G / \ker \pi$:

    - $\pi$ is surjective ($\im \pi = B$) 
    - The exact sequence requires $\ker \pi = \im \mu = \mu(A)$

    Thus we obtain $B \cong G/\mu(A)$.

- We can always choose $G = A \rtimes_\xi B$ with the any group homomorphism $\xi: B \to \Aut(A)$. Then we can choose the monomorphism $\mu$ and the epimorphism $\pi$ as

    $$
    \mu(a) = (a,1), \quad \epsilon(a,b) = b
    \quad (a\in A, b \in B) \quad \blacksquare
    $$

----

<div class="remark">

*Remark*: From the properties above, we can colloquially define the extension of $A$ by $B$ as a group $G$ containing a *normal subgroup* $M$ such that

$$
M \cong A \quad \text{and} \quad G/M \cong B
$$

</div><br>

## Example

Consider the quotient group $\mathbb{Z}/n\mathbb{Z} \ (n \in \mathbb{N})$, representing the cyclic group of order $n$ (up to group isomorphisms):

$$
\mathbb{Z}/n\mathbb{Z} = \{1, g, ..., g^{n-1}\} \qquad
(g^n = 1)
$$

To demonstrate how the group extension is done, we set

$$
\begin{align*}
    A &= \mathbb{Z}/4\mathbb{Z} = \{1, a, a^2, a^3\} 
    & & (a^4 = 1) \\
    B &= \mathbb{Z}/2\mathbb{Z} = \{1, b\}
    & & (b^2 = 1)
\end{align*}
$$

The extension $G$ is not unique. Let us pick an element $g \in G$ which is mapped to $b \in B$. 
