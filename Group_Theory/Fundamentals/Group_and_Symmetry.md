# Group and Symmetry

*Definition*: The concept of group can be introduced in two ways.

- (**Concrete**) A group is the collection of all operations that leaves some set invariant; these operations are called **symmetry** of the set.

- (**Abstract**) A group is a set $G$ endowed with a binary relation (**group multiplication**) that has the following properties: for all $a,b,c \in G$

    - (Associativity) $a(bc) = (ab)c$
    - (Existence of (left) identity) $\exist\ 1 \in G \Rightarrow 1a = a$
    - (Existence of (right) inverse) $\exist\ a^{-1} \in G \Rightarrow a^{-1}a = 1$

    <div class="remark">
    
    *Remark*: The left identity is the same as the right identity; the left inverse is also the same as the right inverse, i.e.

    $$
    \forall g \in G, \quad g1 = g, \quad gg^{-1} = 1
    $$

    </div>

    ----

    *Proof*: For any $g \in G$

    $$
    g g^{-1} = (g^{-1})^{-1} g^{-1} g g^{-1}
    = (g^{-1})^{-1} g^{-1} = 1
    $$

    Thus left inverse = right inverse. Then

    $$
    g 1 = g g^{-1} g = 1g = g
    $$

    Thus left identity = right identity. $\blacksquare$

    ----

## Group Action

*Definition*: We define how a group $G$ may be some "operation" on another set $S$ ($S$ can even be $G$ itself, but in this context the group structure of $S$ is irrelevant).

- **(Left) action** of $G$ on $S$: A function $\phi: G \times S \to S$ satisfying the following requirements: for all $g \in G, s \in S$

    - (Compatibility) $\phi(gh, s) = \phi(g, \phi(h,s))$
    - (Action of identity) $\phi(1,s) = s$

- **Right action**: A function $\phi: S \times G \to S$ satisfying the following requirements

    - (Compatibility) $\phi(s, gh) = \phi(\phi(s,g), h)$
    - (Action of identity) $\phi(s,1) = s$

    <div class="remark">
    
    *Remark*: 
    
    - When context is clear, we simply write 

        $$
        \phi(g,s) = g(s), \quad \phi(s,g) = (s)g
        $$

    - Left and right actions need not be the same: in general $sg \ne gs$. When they are indeed equal, we say $s, g$ **commute**. 

    </div><br>

- **(Left/right) $G$-Set**: A set together with a group $G$ which can act on it. 

### Action of A Group on Itself

When $S = G$, there are many natural definitions of the action of $G$ on itself: let $g \in G, s \in S$, then

$$
\begin{array}{ccc}
    \text{Name} & \text{Left} \ \phi(g,s) & \text{Right} \ \phi(s,g)
    \\[4pt] \hline \\[-4pt]
    \text{Trivial} & s & s 
    \\[0.4em]
    \text{Translation} & gs & sg 
    \\[0.4em]
    \text{(Not named)} & sg^{-1} & g^{-1}s 
    \\[0.4em]
    \text{Adjoint} & gsg^{-1} & g^{-1}sg
\end{array}
$$

Let us verify that the adjoint action is a valid definition.

----
*Proof*: 

- For the left adjoint: obviously $1 s 1^{-1} = s$. We only need to check

    $$
    \begin{align*}
        \phi(gh,s) = g h s h^{-1} g^{-1}
        = g (\phi(h,s)) g^{-1} = \phi(g, h(s))
    \end{align*}
    $$

- For the right adjoint: obviously $1^{-1} s 1 = s$. We only need to check
    $$
    \begin{align*}
        \phi(s,gh) = h^{-1} g^{-1} s g h
        = h^{-1} \phi(s,g) h = \phi(\phi(s,g),h)
        \quad \blacksquare
    \end{align*}
    $$
----


## Cayley's Theorem

The group axioms are motivated by the property of symmetry operations. Conversely, the **Cayley's theorem** ensures that these two definitions are equivalent. 

## Cayley Graph

## Example

Let us choose

$$
\begin{align*}
    G: \text{Symmetry of a equilateral triangle}
    \\
    S: \text{Vertices of the triangle}
\end{align*}
$$
