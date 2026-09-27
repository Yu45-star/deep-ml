import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    def poly(x, coeffs):
        rev = coeffs[::-1]

        total = 0
        for i, coeff in enumerate(rev):
            total += (coeff * pow(x, i))

        return total

    def poly_de(x, coeffs):
        rev = coeffs[::-1]

        total = 0
        for i, coeff in enumerate(rev):
            if i == 0:
                continue
            total += (coeff * pow(x, i - 1) * i)

        return total
        
        return 

    gx = poly(x, g_coeffs)
    hx = poly(x, h_coeffs)

    gx_ = poly_de(x, g_coeffs)
    hx_ = poly_de(x, h_coeffs)

    numerator = gx_ * hx - gx * hx_
    denominator = hx ** 2

    fx_ = numerator / denominator

    return fx_
