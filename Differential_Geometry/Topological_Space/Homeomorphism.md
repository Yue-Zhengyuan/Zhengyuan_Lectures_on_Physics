# Homeomorphism and Topological Invariants

## Homeomorphisms

*Definition*:

- **Homeomorphic topological spaces (同胚拓扑空间)**: two topological spaces which can be deformed to each other *continuously* (i.e. without tearing them apart or pasting)

    Mathematically, two spaces $X, Y$ are **homeomorphic** to each other if we can find two *continuous* maps

    $$f: X \to Y, \quad g: Y \to X$$

    such that

    $$
    (f \circ g = \text{id}_Y) \land
    (g \circ f = \text{id}_X) 
    $$

    - **Homeomorphism**: the funtions $f, g$
    
*Remark*: By definition, $f, g$ are the *inverse* of each other. Thus we may adopt an alternative (and equivalent) definition of homeomorphisms:

- **Homeomorphism**: a *continuous and bijective* map $f$ between two topological spaces, whose inverse $f^{-1}$ is *also continuous* (and obviously bijective)

----

*Proposition*: **Homeomorphic relation is an equivalence relation**.

----

## Topological Invariants