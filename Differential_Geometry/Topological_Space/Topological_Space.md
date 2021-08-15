# Topological Spaces

*Definition*:

- **Topological space**: a set $X$ together with a certain collection $\mathcal{T} = \{U_i \mid i \in I\}$ of subsets $U_i$ of $X$ ($I$ is the set of the allowed values of the index $i$), which satisfy the following requirements:

    1. $\varnothing, X \in \mathcal{T}$
    2. For any subset (may be *infinite*) $J \subset I$, the sub-collection $\{U_j \mid j \in J\}$ satisfies $\bigcup_{j \in J} U_j \in \mathcal{T}$
    3. For any *finite* subset $K \subset I$, the sub-collection $\{U_j \mid j \in J\}$ satisfies $\bigcap_{k \in K} U_k \in \mathcal{T}$

<div class="remark">

*Remark*: From now on the symbol $X$ refers to a topological space unless otherwise stated.

</div><br>

- **Open sets**: the elements $U_i$ in the collection $\mathcal{T}$

- **Topology**: the collection $\mathcal{T}$

### Examples
    
- **Discrete topology**: $\mathcal{T} =$ *all* subsets of $X$
- **Trivial topology**: $\mathcal{T} = \{\varnothing, X\}$
- **Usual topology**: $X = \mathbb{R}, \mathcal{T} =$ all open intervals $(a,b)$ and their unions. 

## Metric Space

*Definition*:

- **Metric**: a map $d: X \times X \to \R$ ($X$ is any set) with the following properties: for any $x,y,z \in X$
    
    1. *Symmetry*: $d(x,y) = d(y,x)$
    2. *Non-negativeness*: $d(x,y) \ge 0$; equality holds only for $x=y$
    3. *Triangle inequality*: $d(x,y) + d(y,z) \ge d(x,z)$

- **Metric space**: a set $X$ with a metric $d$

A metric space can always be made a topological space by the following choice of $\mathcal{T}$:

- **Metric topology**: the open sets in the collection $\mathcal{T}$ are given by *open discs* of any radius $r$ centered at any point $x \in X$

    $$
    U_r(x) = \{x' \in X \mid d(x,x') < r\}
    $$

    and all their possible unions. 

### Examples

- **Discrete metric**: for any $x, y \in X$

    $$
    d(x,y) = \begin{cases}
        0, & x = y \\
        1, & x \ne y
    \end{cases}
    $$

- **Pythagorean metric**: in the set $\R^n$, for $x, y \in \R^n$

    $$
    d(x,y) = \bigg[\sum_{j=1}^n (x_j - y_j)^2\bigg]^{1/2}
    $$

## Continuous Maps

*Definition*:

- **Continuous map**: a map $f: X \to Y$ between two topological spaces, such that the inverse image of an *open* set in $Y$ is an *open* set in $X$.

## Neighborhoods and Hausdorff Spaces

*Definition*:

- **Neighborhood of a point $x \in X$**: a subset $N$ of $X$
    - **Open neighborhood**

- **Hausdorff space**: a topological space $(X,\mathcal{T})$ where for *any* two different points $x, x' \in X$, there always exist neighborhoods $U_x, U_{x'}$ such that $U_x \cap U_{x'} = \varnothing$.

<div class="result">

*Theorem*: Any metric space (equipped with the metric topology) ss a Hausdorff space. 

</div><br>

## Closed Set

*Definition*:

- **Closed set**
    - **Closure**
    - **Interior**
    - **Boundary**

## Compactness

*Definition*:

- **Covering**
    - **Open covering**

- **Compact set**

----

*Theorem*: (**Criterion of Compactness**)

A subset $X \in \mathbb{R}^n$ is compact *if and only if* it is both *closed and bounded*.

----

## Connectedness

*Definition*:

- **Connected topological space**
    - **Disconnected topological space**
    
- **Arcwise connected topological space**

- **Loop**
    - **Simply connected topological space**