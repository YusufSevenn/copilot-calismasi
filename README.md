mystery_module — Quadratic Equation Solver
A small, focused Python module that computes the roots of a quadratic equation ax^2 + bx + c = 0 using the discriminant. Designed for clarity and correctness; supports real and complex roots.

Requirements
Python 3.8+
Uses the standard library only (math and cmath)
Installation
Copy mystery_module.py into your project, or import it from this repository.

Usage
Python API example:
from mystery_module import fn_x

# Example 1: two distinct real roots

r1, r2 = fn_x(1, -3, 2) # roots: 2.0 and 1.0

# Example 2: one repeated real root

r1, r2 = fn_x(1, 2, 1) # roots: -1.0 and -1.0

# Example 3: complex conjugate roots

r1, r2 = fn_x(1, 0, 1) # roots: 1j and -1j
Command-line example (if you add a small CLI wrapper):
python -m mystery_module 1 -3 2

# Output:

# Roots: 2.0, 1.0

Function Description
fn_x(a, b, c)

Purpose: Compute the two roots of the quadratic equation ax^2 + bx + c = 0.
Signature (recommended):
def fn_x(a: float, b: float, c: float) -> tuple[complex, complex]:
Parameters:
a (float): quadratic coefficient. Must not be zero.
b (float): linear coefficient.
c (float): constant term.
Returns:
tuple (root1, root2): a pair of roots. Each root is a float for real roots or a complex for complex roots.
Behavior and edge cases:
If a == 0, the equation is not quadratic. The function should raise ValueError("Coefficient 'a' must not be 0") or handle the linear case explicitly (recommended: raise to keep the function single-responsibility).
Uses the discriminant D = b^2 - 4ac to decide root types:
D > 0: two distinct real roots
D = 0: one repeated real root (returned twice)
D < 0: two complex conjugate roots
The function should avoid logging or printing secrets and should not mutate inputs.
Numerical notes:
For better numerical stability with very small/large coefficients, consider the stable quadratic formula variant:
q = -0.5 _ (b + sign(b) _ sqrt(D))
root1 = q / a
root2 = c / q
Use cmath.sqrt when D < 0 to obtain complex square roots.
Example docstring:
def fn_x(a: float, b: float, c: float) -> tuple[complex, complex]:
"""
Return the two roots of ax^2 + bx + c = 0.

    Raises:
        ValueError: if a == 0.

    Returns:
        (root1, root2): each element may be float or complex depending on discriminant.
    """
    Mathematical Background

Given the quadratic equation:
ax^2 + bx + c = 0 (a != 0)

The discriminant D is:
D = b^2 − 4ac

If D > 0: two distinct real roots:
x = (-b ± sqrt(D)) / (2a)
If D = 0: one repeated real root:
x = -b / (2a) (returned as both roots)
If D < 0: two complex conjugate roots:
x = (-b ± i\*sqrt(|D|)) / (2a)
Derivation (brief):
Solve ax^2 + bx + c = 0 by completing the square:
x = [-b ± sqrt(b^2 − 4ac)] / (2a)

Numerical stability tip:
When |b| is large relative to sqrt(D), direct computation of (-b ± sqrt(D)) can cause catastrophic cancellation. A common stable approach:

compute q = -0.5 _ (b + sign(b) _ sqrt(D))
then x1 = q / a and x2 = c / q
This reduces loss of precision for one of the roots.

Testing
Add unit tests covering:

Distinct real roots (D > 0)
Repeated root (D == 0)
Complex roots (D < 0)
Error raised for a == 0
Numeric stability cases (large/small coefficients)
Example pytest snippet:
def test_fn_x_real_distinct():
r1, r2 = fn_x(1, -3, 2)
assert set((round(r1, 6), round(r2, 6))) == {1.0, 2.0}

def test_fn_x_complex():
r1, r2 = fn_x(1, 0, 1)
assert r1 == complex(0, 1) or r2 == complex(0, 1)
Contribution
Please open an issue or pull request for bug fixes, improvements, or adding a CLI wrapper.
Follow standard practices: add tests for any behavior changes and keep changes small and focused.
License
Specify your project license here (e.g., MIT, Apache-2.0).
