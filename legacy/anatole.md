## Méthode de résolution (Euler)


$$
x(t) = x(t_0) + \int_{t_0}^{t} {f(t', x(t')) \,\mathrm{d}t'}
$$

$$
\int_{t_{i}}^{t_{i+1}} {f(t, x(t)) \,\mathrm{d}t}
$$

<br>Discrétisation de la résolution :
$$
x(t_{i+1}) = x(t_{i}) + \int_{t_{i}}^{t_{i+1}} {f(t, x(t)) \,\mathrm{d}t}
$$
avec $\int_{t_{i}}^{t_{i+1}} {f(t, x(t)) \,\mathrm{d}t} = \phi(t_{i}, t_{i+1}, \cdots)$


Méthode explicite :
$\phi \approx (t_{i+1} - t_{i}) f(t_{i}, x(t_{i}))$
