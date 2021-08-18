# Singular Value Decomposition

*Note: In this part we consider linear mappings between complex vector spaces; the representation matrices will in general be complex.*

Consider two vector spaces $X, Y$. Let $n = \dim X, m = \dim Y$. The theorem of **singular value decomposition** states that for any linear maps $A: X \to Y$, its representation matrix

$$
A \in \mathbb{C}^{m \times n} 
$$

can be decomposed as

$$
A = U S V^\dagger
$$

- $U \in \mathbb{C}^{m \times m}, V \in \mathbb{C}^{n \times n}$ are *unitary* matrices, i.e. the columns are orthonormal basis vectors of $Y, X$ respectively;

- $S \in \mathbb{R}^{m \times n}$ is a real rectangular *diagonal* matrix. The diagonal elements $s_i = S_{ii}$ ($i = 1,...,\min{(m,n)}$) are called the **singular values**

The singular values can be shown to be all *non-negative real numbers*. Usually they are arranged in *descending* order (large to small). 

## Existence Proof



## Reduced SVD

## Applications

### Low-rank Matrix Approximation