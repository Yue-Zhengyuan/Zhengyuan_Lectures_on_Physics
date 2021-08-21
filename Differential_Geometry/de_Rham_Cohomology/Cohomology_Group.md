# de Rham Cohomology Groups

## Co-cycle and Co-boundary

*Definition*: Let $M$ be an $m$-dimensional manifold.

- **de Rham complex**: 

    $$
    0 \xrightarrow{i} \Omega^0(M)
    \xrightarrow{d} \Omega^1(M)
    \xrightarrow{d} \cdots 
    \xrightarrow{d} \Omega^m(M)
    \xrightarrow{d} 0
    $$

- **$r$-Cocycle group $Z^r(M)$**: the set of all **closed** $r$-forms in $M$
    
    - **Closed $r$-form**: an $r$-form whose derivative is zero
    
    $$
    Z^r(M) = \ker{d_r} = \{
        \omega \in \Omega^r(M) \mid
        d_r \omega = 0
    \}
    $$

- **$r$-Coboundary group $B^r(M)$**: the set of all **exact** $r$-forms in $M$
    
    - **Exact $r$-form**: an $r$-form which is the derivative of an $(r-1)$-form
    
    $$
    \begin{align*}
        B^r(M) &= \im  d_{r-1} \\
        &= \{
            \omega \in \Omega^r(M) \mid
            \omega = d_{r-1} \xi , \,
            \exists \xi \in \Omega^{r-1}(M)
        \}
    \end{align*}
    $$

    *Remark*: 
    
    - Since $d^2 = 0$, *an exact form must be closed*, i.e. 

        $$
        B^r(M) \subset Z^r(M)
        $$

        A necessary condition for *closed forms to be exact* is given by the [**Poincaré's lemma**](6_3-Poincare_Lemma.md). 

    - Both $Z^r(M)$ and $B^r(M)$ are vector spaces with *real* coefficients.

- **Cohomologous $r$-forms**:

    - **The $r$-th de Rham cohomology group**:

        $$
        H^r(M) \equiv Z^r(M) / B^r(M)
        $$

        The corresponding equivalence relation is *cohomologous relation*. 