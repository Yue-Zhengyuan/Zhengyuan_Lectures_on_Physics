# Theory of Finite Groups

<font size=5>

**Part 1: Basic Definitions**

</font>

## Group Axioms

- **Order of a group element $g$**: the minimal positive integer $N$ satisfying 
    
    $$
    g^N = 1 \quad (\text{Abelian: } N g = 0)
    $$

- **Abelian group**: A group in which *all elements commute*.

*Summary of Notations*:

<center>

|                               Operation | General Group        | Abelian Groups            |
| --------------------------------------: | :------------------- | :------------------------ |
|                        Identity element | $1$                  | $0$                       |
|                  Inverse element of $g$ | $g^{-1}$             | $-g$                      |
|                   Product of $g_1, g_2$ | $g_1 g_2$            | $g_1 + g_2$ (As addition) |
| Product of $g_1, \operatorname{inv}g_2$ | $g_1 g_2^{-1}$       | $g_1 - g_2$               |
|                        $g$ to power $n$ | $g^n \quad(g^0 = 1)$ | $n g \quad (0 g = 0)$     |

</center>

Whenever we use the additive notation, we have assumed that we are dealing with an Abelian group. 

## Homomorphism and Isomorphism

*Definition*: Let $G_1, G_2$ be two groups

- **Homomorphism (同态)**: a map $f: G_1 \to G_2$ such that

    $$
    \forall x, y \in G_1 \quad \begin{align*}
        &f(xy)  = f(x) f(y)     & \text{(General)}\\
        &f(x+y) = f(x) + f(y)   & \text{(Abelian)}
    \end{align*} 
    $$

- **Isomorphism (同构)**: an homomorphism from one group to another which is *also injective (one-to-one)*.

- **Isomorphic Groups**: Two groups between which exists an isomorphism, denoted by

    $$
    G_1 \cong G_2
    $$

## Subgroups and Cosets

*Definition*:

- **Subgroups**: a subset $H$ of $G$ which still forms a group under the same multiplication rule of $G$
    
- **Normal (invariant) subgroup**: a subgroup $H \in G$ which is invariant under *conjugation* by any elements in $G$:

    $$
    (H \triangleleft G) :=
    \forall \, h \in H, g \in G :
    g^{-1} h g \in H
    $$

- **Coset**: The set of group elements obtained by multiplying $g \in G$ on the left (or right) of a subgroup $H$ of $G$

    $$
    \begin{align*}
        \text{Left coset} &: gH = \{gh \mid h \in H\}
        \\
        \text{Right coset}&: Hg = \{hg \mid h \in H\}
    \end{align*}
    $$

----

*Theorem*: (**Group homomorphism lemma**)

Let $f: G_1 \to G_2$ be a group homomorphism. Then

- $\ker{f} = \{x|x\in G_1, f(x) = 0\}$ is a subgroup of $G_1$
- $\text{im }f = \{y|y \in f(G_1) \subset G_2\}$ is a subgroup of $G_2$

----

*Theorem*: (**Coset decomposition of any group**)

----

## Equivalence and Quotient Group

Let $G$ be a group, and $H$ a subgroup of $G$. 

- **Equivalence relation**: Two elements $g, g' \in G$ are **equivalent** if 
    
    $$
    \exist h \in H: g' = gh 
    \quad (\text{i.e.} \quad g^{-1} g' \in H)
    $$
    
    Since $H$ is also a group, this is also equivalent to saying $g' g^{-1} \in H$. 
    
    In Abelian notation

    $$
    g' - g \in H
    $$

- **Equivalence class** $[g]$: the set of all elements in $G$ that are equivalent to $g$
    
    $$
    [g] = \{gh \mid h \in H\}
    $$

    which is just the *left coset* $gH$. 
    
- **The quotient group** $G/H$: The set of all equivalence classes (left cosets of $H$) (defined only when $H$ is a *normal* subgroup of $G$)

    $$
    G/H = \{ [g] \mid g \in G\}
    $$

    The multiplication is defined as

    $$
    [g] [g'] = [g g']
    $$

    *Verification of unambiguity*: Since $g^{-1} H g = H$, we obtain

    $$
    [g][g'] = (g H) (g' H)
    = g g' (g'^{-1} H g') H 
    = g g' H = [g g']
    $$

- **Center** of a group $G$: the set of elements that commute with every element of $G$, denoted by
    
    $$
    Z(G) = \{z \in G \mid \forall g \in G, \ zg = gz\}
    $$

    - **Centerless group**: a group with $Z(G) = 1$ (trivial, containing only the identity element of $G$)

----

*Theorem*: (On the center of a group)

- $Z(G)$ is a normal subgroup of $G$
- A group $G$ is abelian *if and only if* $Z(G) = G$

----

*Theorem*: (**Fundamental theorem of homomorphism**)

Let $f: G_1 \to G_2$ be a group homomorphism. Then

$$G_1 / \ker{f} \cong \text{im }f$$

----