#### TX 2020 Election Latinos
#### Split Ticket 2020 Election TX Latinos Analysis

## Regression Output

### Weighted (by Population) Least Squares Regression Table
**R² = 0.466**

| **Variable**                  | **Coef** | **Std Err** | **t**    | **P>|t|** | **[0.025** | **0.975]** |

|-------------------------------|----------|-------------|----------|---------|------------|------------|

| **const**                     | -0.0096  | 0.002       | -6.018   | 0       | -0.013     | -0.006     |

| **Sanders Gain**              | 0.144    | 0.003       | 47.131   | 0       | 0.138      | 0.150      |

| **Hispanic or Latino**        | 0.0501   | 0.002       | 29.270   | 0       | 0.047      | 0.053      |

| **Asian**                     | 0.0159   | 0.003       | 5.863    | 0       | 0.011      | 0.021      |

| **Black or African American** | 0.0042   | 0.002       | 2.052    | 0.040   | 0          | 0.008      |

| **Median Age**                | 0.0042   | 0           | 34.026   | 0       | 0.004      | 0.004      |

| **College Attainment**        | 0.0012   | 0.001       | 0.898    | 0.003   | -0.001     | 0.004      |

| **Median Income**             | -0.0003  | 0           | -1.318   | 0.187   | -0.001     | 0          |

| **White**                     | -0.0035  | 0.002       | -1.994   | 0.046   | -0.007     | 0          |

| **County Density**            | -0.0071  | 0           | -32.913  | 0       | -0.007     | -0.007     |

### Sanders-Latino Interaction Term

I added an interaction term between Latinos and Sanders shift to the original regression, which is computationally just multiplying the two together. In this context, the interaction term tests whether the relationship between Sanders’ gains and Trump’s gains is stronger in areas with large Latino populations. Indeed, Sanders gains were much more predictive of Trump gains in heavily-Latino areas. This new Latino-Sanders Gain interaction term was the strongest variable and its inclusion decreased the predictive power of both Latino population and Sanders’ gain, suggesting combining both variables together predicts with Trump gains.

### Weighted (by Population) Least Squares Regression Table (w/Sanders-Latino Interaction)
**R² = 0.517**

| **Variable**                          | **Coef** | **Std Err** | **t**    | **P>|t|** | **[0.025** | **0.975]** |

|---------------------------------------|----------|-------------|----------|---------|------------|------------|

| **const**                             | -0.0039  | 0.002       | -2.596   | 0.009   | -0.007     | -0.001     |

| **Latino-Sanders Gain Interaction**   | 0.4195   | 0.01        | 42.1     | 0       | 0.400      | 0.439      |

| **Hispanic or Latino**                | 0.0391   | 0.002       | 23.698   | 0       | 0.036      | 0.042      |

| **Black or African American**         | 0.0057   | 0.002       | 2.932    | 0.003   | 0.002      | 0.009      |

| **Median Age**                        | 0.0036   | 0           | 30.254   | 0       | 0.003      | 0.004      |

| **College Attainment**                | 0.0016   | 0.001       | 1.259    | 0.208   | -0.001     | 0.004      |

| **Asian**                             | 0.0008   | 0.003       | 0.309    | 0.757   | -0.004     | 0.006      |

| **Median Income**                     | -0.0006  | 0           | -2.457   | 0.014   | -0.001     | 0          |

| **County Density**                    | -0.0074  | 0           | -36.192  | 0       | -0.008     | -0.007     |

| **White**                             | -0.0158  | 0.002       | -9.269   | 0       | -0.019     | -0.012     |

| **Sanders Gain**                      | -0.0324  | 0.002       | -6.354   | 0       | -0.042     | -0.022     |

One possible explanation for the larger Sanders-Latino interaction coefficient is that squaring the two ≤1.00 terms makes a small magnitude term, prompting the regression to inflate its coefficient value to compensate for the smaller value. To test that explanation, I squared the Latino and Sanders terms from the original regression. The resulting correlation coefficients were much smaller than the Sanders-Latino interaction term (0.0737, 0.2397 < 0.4195), reaffirming the large coefficient reflects a strong predictive value of the interaction term.

