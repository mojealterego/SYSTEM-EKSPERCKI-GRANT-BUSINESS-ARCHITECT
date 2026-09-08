from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class UnitEconomics:
    selling_price: float
    variable_cost: float
    contribution_margin: float
    contribution_margin_pct: float

def unit_economics(selling_price: float, variable_cost: float) -> UnitEconomics:
    if selling_price < 0 or variable_cost < 0:
        raise ValueError("Costs and prices cannot be negative")
    margin = selling_price - variable_cost
    pct = 0.0 if selling_price == 0 else margin / selling_price
    return UnitEconomics(selling_price, variable_cost, margin, pct)

def break_even_units(fixed_costs: float, contribution_margin: float) -> float:
    if fixed_costs < 0:
        raise ValueError("Fixed costs cannot be negative")
    if contribution_margin <= 0:
        raise ValueError("Contribution margin must be positive")
    return fixed_costs / contribution_margin

def revenue(units: float, price: float) -> float:
    if units < 0 or price < 0:
        raise ValueError("Units and price cannot be negative")
    return units * price

def operating_result(revenue_value: float, variable_cost_value: float, fixed_cost_value: float) -> float:
    return revenue_value - variable_cost_value - fixed_cost_value
