"""
Functions that calculate personal income tax liability.
"""
# CODING-STYLE CHECKS:
# pycodestyle functions.py
# pylint --disable=locally-disabled functions.py

import math
import copy
import numpy as np
from taxcalc.decorators import iterate_jit


@iterate_jit(nopython=True)
def net_salary_income(SALARIES, Income_Salary):
    """
    Compute net salary as gross salary minus deductions u/s 16.
    """
    # TODO: when gross salary and deductions are avaiable, do the calculation
    # TODO: when using net_salary as function argument, no calculations neeed
    """
    The deductions (transport and medical) that are being done away with while
    intrducing Standard Deduction is not captured in the schedule also. Thus,
    the two deductions combined (crude estimate gives a figure of 30000) is
    added to "SALARIES" and then "std_deduction" (introduced as a policy
    variable) is deducted to get "Income_Salary". Standard Deduction is being
    intruduced only from AY 2019 onwards, "std_deduction" is set as 30000 for
    AY 2017 and of 2018 thus resulting in no change for those years.
    """
    Income_Salary = SALARIES
    return Income_Salary

@iterate_jit(nopython=True)
def taxable_income(Income_Salary, Taxable_Income):
    """
    Compute net salary as gross salary minus deductions u/s 16.
    """
    # TODO: when gross salary and deductions are avaiable, do the calculation
    # TODO: when using net_salary as function argument, no calculations neeed
    """
    The deductions (transport and medical) that are being done away with while
    intrducing Standard Deduction is not captured in the schedule also. Thus,
    the two deductions combined (crude estimate gives a figure of 30000) is
    added to "SALARIES" and then "std_deduction" (introduced as a policy
    variable) is deducted to get "Income_Salary". Standard Deduction is being
    intruduced only from AY 2019 onwards, "std_deduction" is set as 30000 for
    AY 2017 and of 2018 thus resulting in no change for those years.
    """
    Taxable_Income = Income_Salary
    return Taxable_Income

DEBUG = False
DEBUG_IDX = 0


@iterate_jit(nopython=True)
def pit_liability(rate1, rate2, rate3, rate4, tbrk1, tbrk2, tbrk3, tbrk4,
                  Taxable_Income, pitax):
    """
    Compute tax liability given the progressive tax rate schedule specified
    by the (marginal tax) rate* and (upper tax bracket) brk* parameters and
    given taxable income (taxinc)

    Subtract 'TI_special_rates' from 'TTI' to get the portion of total income
    that is taxed at normal rates. Now add agricultural income (income used for
    rate purpose only) to get Aggregate_Income.
    """
    # subtract TI_special_rates from TTI to get Aggregate_Income, which is
    # the portion of TTI that is taxed at normal rates
    taxinc = Taxable_Income
    tax_normal_rates = (rate1 * min(taxinc, tbrk1) +
                        rate2 * min(tbrk2 - tbrk1, max(0., taxinc - tbrk1)) +
                        rate3 * min(tbrk3 - tbrk2, max(0., taxinc - tbrk2)) +
                        rate4 * max(0., taxinc - tbrk3))

    # compute pitax amount
    pitax = tax_normal_rates
    return (pitax)
