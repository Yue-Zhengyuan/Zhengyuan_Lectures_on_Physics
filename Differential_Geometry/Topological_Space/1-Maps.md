# Maps

## Terminology

*Definition*:

- **Map**
    - **Domain**
    - **Range**
    - **Image**
- Special named for maps
    - **Injective maps (单映射)**
    - **Surjective maps (满映射)**
    - **Bijective maps (双映射)**
        
        *Remark*: Bijective maps is the same as **invertible maps (可逆映射)**

    - **Inclusion map**
- **Homomorphism (同态)**: Preserving algebraic structure of domain
    - **Isomorphism (同构)**
    - **Isomorphic sets**

## Equivalence Relation and Equivalence Class

*Definition*:

- **Relation**: defined in a set $X$ specifying the relation (in the usual sense) between two elements (say $a, b$) in $X$; denoted $aRb$
    
    *Example*:

    - $X = \mathbb{R}, \quad R = \text{>}$

- **Equivalence relation**: a special kind of relation (denoted by $\sim$) satisfying the following 3 requirements
    
    <center>
    
    |Requirement|Symbolic Expression|
    |-:|:-|
    |Reflective|$a \sim a$|
    |Symmetric|$a \sim b \Rightarrow b \sim a$|
    |Transitive|$(a \sim b) \land (b \sim c) \Rightarrow (a \sim c)$
    
    </center>

- **Equivalence class**: set of elements all equivalent to each other; the equivalence class containing element $a \in X$ is denoted by
    
    $$
    [a] \equiv \{x \in X | x \sim a\}
    $$

- **Representative of an equivalence class**: any element in this class

    *Example*:

    - The representative of $[a]$ can be chosen to be $a$. 

- **Quotient space**: the set of all equivalence classes in $X$ with $\sim$; denoted $X / \sim$

*Theorem*: (**Equivalence classes are either disjoint or identical**)

Given a set $X$ with an equivalence relation $\sim$, it can always be partitioned into *mutually disjoint* equivalence classes. 

