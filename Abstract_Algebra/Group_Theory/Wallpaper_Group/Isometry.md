# Isometries of $\R^n$

## General Properties of Isometries

In general, given two metric spaces $X, Y$ with metrics (distances) $d_X, d_Y$, an **isometry** is a *distance-preserving* map between them:

$$
f: X \to Y \quad 
\forall a,b \in X, \quad
d_X(a,b) = d_Y(f(a), f(b))
$$

Below we list some general properties of isometries that follow immediately from the definition, without giving a rigorous proof.

- $f$ is *injective*, i.e. 

    $$
    \forall a, b \in X, \quad
    (a \ne b) \Rightarrow (f(a) \ne f(b))
    $$

    Otherwise the distance between $a, b$ cannot be preserved.

- The composition of two isometries, and the inverse of an isometry (if it is also bijective) are still isometries.

From these properties, all isometries from a metric space $X$ to *itself* are automatically bijective; thus they form a *group* under the composition of mappings.

## Important Subgroups of $\mathbb{R}^n$

From now on we consider isometries between $\R^n$ and itself, which are automatically *bijective*. The set of all such isometries (denoted by $\Isom(\R^n)$) is then a *group* under the usual composition of mappings. 

We first make $\R^n$ into a *vector space* with an inner product; then the metric $d(x,y)$ on $\R^n$ is directly chosen as the square root the inner product of $x - y$ and itself. 

Two types of isometries of $\R^n$ are of special importance.

### Origin-Preserving Isometries (Point Group)

Such an isometry $h$ keeps the origin invariant: its action on the zero vector is

$$
h(0) = 0
$$

All origin-preserving isometries form a *subgroup* $G_0$ (called the **point group** of $\R^n$) of $\Isom(\R^n)$. It turns out that these isometries are *linear*; ultimately:

<div class="result">

*Theorem*: The subgroup $G_0$ of origin-preserving isometries of $\R^n$ is *isomorphic* to the orthogonal group $O(n)$.

</div><br>

Then the action of $h \in G_0$ on any $x \in \R^n$ is directly given by the matrix multiplication

$$
h(x) = \mathcal{D}(h) x
$$

where $\mathcal{D}(h)$ is the matrix in $O(n)$ corresponding to $h \in G_0$. Usually we simply write $D(h)x = hx$.

### Translation Group

Among isometries that does not preserve the origin, **translations** are of special importance. A translation by a vector $a \in \R^n$ is denoted by $\tau_a$: 

$$
\tau_a: \R^n \to \R^n \quad 
\forall x\in \R^n, \ \tau_a(x) = a + x
$$

Intuitively, the composition and the inverse of translations are given by

$$
\tau_a \tau_b = \tau_b \tau_a = \tau_{a+b}, \quad
\tau_a^{-1} = \tau_{-a}
$$

Thus all translations form an *Abelian* subgroup $T$ of $\Isom(\R^n)$. Obviously:

<div class="result">

*Theorem*: The translation group $T$ is *isomorphic* to $\R^n$ endowed with the usual vector addition; the isomorphism is simply

$$
\tau_a \in T \mapsto a \in \R^n
$$

</div><br>

## Group Structure of $\Isom(\R^n)$

It turns out that the entire $\Isom(\R^n)$ can be obtained from the subgroups $G_0$ and $T$:

<div class="result">

*Theorem*: Any isometry $g \in \Isom(\R^n)$ can be expressed as the composition of an origin-preserving one $h \in G_0$ and a translation $\tau_a \in T$, i.e.

$$
\Isom(\R^n) = T G_0 
= \{\tau_a h \mid \tau_a \in T, h \in G_0\}
$$

</div><br>

The group multiplication in $\Isom(\R^n)$ is defined based on the action on a vector $x \in \R^n$: for an arbitrary $g = \tau_a h$

$$
g(x) = \tau_a (hx) = a + hx
$$

Then the action of the composition of two elements in $\Isom(\R^n)$ is

$$
\begin{align*}
    (\tau_a h) (\tau_{a'} h')(x)
    &= (\tau_a, h)(a' + h'x)
    \\
    &= a + h(a' + h'x)
\end{align*}
$$

From this result:

<div class="result">

**Multiplication and inverse in $\Isom(\R^n)$:**

$$
(\tau_a h) (\tau_{a'} h') 
= \tau_a \tau_{ha'} hh', \quad
(\tau_a h)^{-1} = \tau_{-h^{-1}a} h^{-1}
$$

</div>

----

*Verifying the inverse*:

$$
\begin{align*}
    (\tau_a h)(\tau_{-h^{-1}a} h^{-1})
    &= \tau_a \tau_{-hh^{-1}a} hh^{-1}
    \\
    &= \tau_a \tau_{-a} = 1
    & \blacksquare
\end{align*}
$$

----

With this multiplication, we can show that

<div class="result">

*Theorem*: $T \lhd \Isom(\R^n)$ (the translation group is a *normal* subgroup of $\Isom(\R^n)$).

</div>

----

*Proof*: For any $\tau_a \in T$ and any $\tau_b h \in \Isom(\R^n)$

$$
\begin{align*}
    &(\tau_b h)^{-1} \tau_a (\tau_b h)
    = \tau_{-h^{-1}b} h^{-1} \tau_{a+b} h \\
    &= \tau_{-h^{-1}b} \tau_{h^{-1}(a+b)} h^{-1} h
    = \tau_{h^{-1}a} \in T
    & \blacksquare
\end{align*}
$$

----

From the above analysis, we find that $\Isom(\R^n)$ is (strictly speaking, isomorphic to) the *semi-direct product* of the translation group $T$ and the point group $G_0$:

$$
\left. \begin{aligned}
    \Isom(\R^n) = T G_0 & \\
    T \lhd \Isom(\R^n) & \\
    T \cap G_0 = \{1\} & \\
\end{aligned} \right\} \Rightarrow
\Isom(\R^n) \cong T \rtimes G_0 \cong \R^n \rtimes O(n)
$$

The isomorphism is simply $\tau_a h \mapsto (\tau_a,h)$. The homomorphism $\phi: G_0 \to \Aut(T)$ in the semi-direct product can be found by comparing with the general definition:

$$
\begin{gather*}
    (\tau_a, h) (\tau_{a'}, h')
    \overset{\text{def}}{=} (\tau_a \phi_h(\tau_{a'}), h h')
    = (\tau_a \tau_{ha'}, hh')
    \\ \Downarrow \\
    \boxed{
        \phi_h: \tau_{a} \mapsto \tau_{ha}
    }
\end{gather*}
$$

