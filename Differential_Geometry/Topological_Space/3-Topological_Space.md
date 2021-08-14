# Topological Spaces

*Definition*:

- **Topological space**: a set $X$ together with a certain collection $\mathcal{T} = \{U_i \mid i \in I\}$ of subsets $U_i$ of $X$ ($I$ is the set of the allowed values of the index $i$), which satisfy the following requirements:

> 1. $\varnothing, X \in \mathcal{T}$
>
> 2. For any subset (may be *infinite*) $J \subset I$, the sub-collection $\{U_j \mid j \in J\}$ satisfies $\bigcup_{j \in J} U_j \in \mathcal{T}$
>
> 3. For any *finite* subset $K \subset I$, the sub-collection $\{U_j \mid j \in J\}$ satisfies $\bigcap_{k \in K} U_k \in \mathcal{T}$

We usually say $X$ is a topological space, without specific reference to the collection $\mathcal{T}$.

- **Open sets**: the elements $U_i$ in the collection $\mathcal{T}$

- **Topology**: the collection $\mathcal{T}$

- **Different kinds of topology**
    
    - **Discrete topology**: $\mathcal{T} =$ *all* subsets of $X$
    - **Trivial topology**: $\mathcal{T} = \{\varnothing, X\}$
    - **Usual topology**: $X = \mathbb{R}, \mathcal{T} =$ all open intervals $(a,b)$ and their unions. 

- **Metric**
    - **Metric topology**
    - **Metric space**

## Continuous Maps

*Definition*:

- **Continuous map**

## Neighborhoods and Hausdorff Spaces

*Definition*:

- **Neighborhood of a point**
    - **Open neighborhood**

- **Hausdorff space**

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