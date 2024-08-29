# tx-2020-election-latinos
Split Ticket 2020 Election TX Latinos Analysis

## Regression Output

### Weighted (by Population) Least Squares Regression Table
**R² = 0.466**

<table>
  <thead>
    <tr>
      <th style="text-align: left;">Variable</th>
      <th style="text-align: right;">Coef</th>
      <th style="text-align: right;">Std Err</th>
      <th style="text-align: right;">t</th>
      <th style="text-align: right;">P>|t|</th>
      <th style="text-align: right;">[0.025</th>
      <th style="text-align: right;">0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>const</strong></td>
      <td style="text-align: right;">-0.0096</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-6.018</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.013</td>
      <td style="text-align: right;">-0.006</td>
    </tr>
    <tr>
      <td><strong>Sanders Gain</strong></td>
      <td style="text-align: right;">0.144</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">47.131</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.138</td>
      <td style="text-align: right;">0.15</td>
    </tr>
    <tr>
      <td><strong>Hispanic or Latino</strong></td>
      <td style="text-align: right;">0.0501</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">29.27</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.047</td>
      <td style="text-align: right;">0.053</td>
    </tr>
    <tr>
      <td><strong>Asian</strong></td>
      <td style="text-align: right;">0.0159</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">5.863</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.011</td>
      <td style="text-align: right;">0.021</td>
    </tr>
    <tr>
      <td><strong>Black or African American</strong></td>
      <td style="text-align: right;">0.0042</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">2.052</td>
      <td style="text-align: right;">0.04</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.008</td>
    </tr>
    <tr>
      <td><strong>Median Age</strong></td>
      <td style="text-align: right;">0.0042</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">34.026</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.004</td>
      <td style="text-align: right;">0.004</td>
    </tr>
    <tr>
      <td><strong>College Attainment</strong></td>
      <td style="text-align: right;">0.0012</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">0.898</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">-0.001</td>
      <td style="text-align: right;">0.004</td>
    </tr>
    <tr>
      <td><strong>Median Income</strong></td>
      <td style="text-align: right;">-0.0003</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-1.318</td>
      <td style="text-align: right;">0.187</td>
      <td style="text-align: right;">-0.001</td>
      <td style="text-align: right;">0</td>
    </tr>
    <tr>
      <td><strong>White</strong></td>
      <td style="text-align: right;">-0.0035</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-1.994</td>
      <td style="text-align: right;">0.046</td>
      <td style="text-align: right;">-0.007</td>
      <td style="text-align: right;">0</td>
    </tr>
    <tr>
      <td><strong>County Density</strong></td>
      <td style="text-align: right;">-0.0071</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-32.913</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.007</td>
      <td style="text-align: right;">-0.007</td>
    </tr>
  </tbody>
</table>

The above regression was by the 2020 Census Block Group level, the most granular geography the Census publishes income and education data on. Using the Maup Python packege, Census block-level 2016-2020 Presidential General Election, block-level 2016 Democratic Primary, and precinct-level 2016 Democratic Primary data was aggregated to the Block Group Level. Income, county density, age data was tranformed to standardized 

I added an interaction term between Latinos and Sanders shift to the original regression, which is computationally just multiplying the two together. In this context, the interaction term tests whether the relationship between Sanders’ gains and Trump’s gains is stronger in areas with large Latino populations. Indeed, Sanders gains were much more predictive of Trump gains in heavily-Latino areas. This new Latino-Sanders Gain interaction term was the strongest variable and its inclusion decreased the predictive power of both Latino population and Sanders’ gain, suggesting combining both variables together predicts with Trump gains.


### Weighted (by Population) Least Squares Regression Table (w/Sanders-Latino Interaction)
**R² = 0.517**

<table>
  <thead>
    <tr>
      <th style="text-align: left;">Variable</th>
      <th style="text-align: right;">Coef</th>
      <th style="text-align: right;">Std Err</th>
      <th style="text-align: right;">t</th>
      <th style="text-align: right;">P>|t|</th>
      <th style="text-align: right;">[0.025</th>
      <th style="text-align: right;">0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>const</strong></td>
      <td style="text-align: right;">-0.0039</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-2.596</td>
      <td style="text-align: right;">0.009</td>
      <td style="text-align: right;">-0.007</td>
      <td style="text-align: right;">-0.001</td>
    </tr>
    <tr>
      <td><strong>Latino-Sanders Gain Interaction</strong></td>
      <td style="text-align: right;">0.4195</td>
      <td style="text-align: right;">0.01</td>
      <td style="text-align: right;">42.1</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.400</td>
      <td style="text-align: right;">0.439</td>
    </tr>
    <tr>
      <td><strong>Hispanic or Latino</strong></td>
      <td style="text-align: right;">0.0391</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">23.698</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.036</td>
      <td style="text-align: right;">0.042</td>
    </tr>
    <tr>
      <td><strong>Black or African American</strong></td>
      <td style="text-align: right;">0.0057</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">2.932</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">0.009</td>
    </tr>
    <tr>
      <td><strong>Median Age</strong></td>
      <td style="text-align: right;">0.0036</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">30.254</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">0.004</td>
    </tr>
    <tr>
      <td><strong>College Attainment</strong></td>
      <td style="text-align: right;">0.0016</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">1.259</td>
      <td style="text-align: right;">0.208</td>
      <td style="text-align: right;">-0.001</td>
      <td style="text-align: right;">0.004</td>
    </tr>
    <tr>
      <td><strong>Asian</strong></td>
      <td style="text-align: right;">0.0008</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">0.309</td>
      <td style="text-align: right;">0.757</td>
      <td style="text-align: right;">-0.004</td>
      <td style="text-align: right;">0.006</td>
    </tr>
    <tr>
      <td><strong>Median Income</strong></td>
      <td style="text-align: right;">-0.0006</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-2.457</td>
      <td style="text-align: right;">0.014</td>
      <td style="text-align: right;">-0.001</td>
      <td style="text-align: right;">0</td>
    </tr>
    <tr>
      <td><strong>County Density</strong></td>
      <td style="text-align: right;">-0.0074</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-36.192</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.008</td>
      <td style="text-align: right;">-0.007</td>
    </tr>
    <tr>
      <td><strong>White</strong></td>
      <td style="text-align: right;">-0.0158</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-9.269</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.019</td>
      <td style="text-align: right;">-0.012</td>
    </tr>
    <tr>
      <td><strong>Sanders Gain</strong></td>
      <td style="text-align: right;">-0.0324</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-6.354</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.042</td>
      <td style="text-align: right;">-0.022</td>
    </tr>
  </tbody>
</table>

One possible explanation for the larger Sanders-Latino interaction coefficient is that squaring the two ≤1.00 terms makes a small magnitude term, prompting the regression to inflate its coefficient value to compensate for the smaller value. To test that explanation, I squared the Latino and Sanders terms from the original regression. The resulting correlation coefficients were much smaller than the Sanders-Latino interaction term (0.0737, 0.2397 < 0.4195), reaffirming the large coefficient reflects a strong predictive value of the interaction term.
