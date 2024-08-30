# tx-2020-election-latinos
Split Ticket TX 2020 Election Latinos Analysis by Andrew Hong

## Regression Output

### Weighted (by Population) Least Squares Regression Table
**Dep. Variable: Trump Gain**

**R² = 0.47**

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
      <td style="text-align: right;">-0.0194</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-13.349</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">-0.022</td>
      <td style="text-align: right;">-0.017</td>
    </tr>
    <tr>
      <td><strong>White</strong></td>
      <td style="text-align: right;">0.0099</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">5.926</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.007</td>
      <td style="text-align: right;">0.013</td>
    </tr>
    <tr>
      <td><strong>Black or African American</strong></td>
      <td style="text-align: right;">0.0230</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">12.219</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.019</td>
      <td style="text-align: right;">0.027</td>
    </tr>
    <tr>
      <td><strong>Asian</strong></td>
      <td style="text-align: right;">0.0272</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">10.179</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.022</td>
      <td style="text-align: right;">0.032</td>
    </tr>
    <tr>
      <td><strong>Hispanic or Latino</strong></td>
      <td style="text-align: right;">0.0663</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">41.734</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.063</td>
      <td style="text-align: right;">0.069</td>
    </tr>
    <tr>
      <td><strong>Sanders_diff</strong></td>
      <td style="text-align: right;">0.1467</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">48.189</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.141</td>
      <td style="text-align: right;">0.153</td>
    </tr>
    <tr>
      <td><strong>MedianIncome</strong></td>
      <td style="text-align: right;">-0.0006</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-0.869</td>
      <td style="text-align: right;">0.385</td>
      <td style="text-align: right;">-0.002</td>
      <td style="text-align: right;">0.001</td>
    </tr>
    <tr>
      <td><strong>CountyDensity</strong></td>
      <td style="text-align: right;">-0.0285</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-39.252</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">-0.030</td>
      <td style="text-align: right;">-0.027</td>
    </tr>
    <tr>
      <td><strong>MedianAge</strong></td>
      <td style="text-align: right;">0.0144</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">23.135</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.013</td>
      <td style="text-align: right;">0.016</td>
    </tr>
    <tr>
      <td><strong>College</strong></td>
      <td style="text-align: right;">0.0101</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">7.818</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.008</td>
      <td style="text-align: right;">0.013</td>
    </tr>
  </tbody>
</table>

The above is the resulting output of a Weighted (by Population) Least-Squares regression predicting Donald Trump Gains (2016-2020) off of a series of demographical and political variables including race, age, income, (4-year) college attainment, county population density, and Bernie Sanders Gains (2016-2020 Dem. Primary). The key takeaway is that Sanders Gain and Latino population proportion were the two strongest predictors of Trump Gains (p<0.0001). Interestingly despite the overwhelming focus on Latinos driving Trump Gains in Texas, Sanders Gains was actually more predictive of Trump Gains than Latino population proportion was. A +10% greater Sanders Gain predicts a +1.5% greater Trump Gain per Census Block Group (BG), while a +10% greater Latino population proportion predicts just +0.6% greater Trump Gain.


After this initial regression, I added an interaction term between Latinos and Sanders shift to the original regression, which is computationally just multiplying the two together. In this context, the interaction term tests whether the relationship between Sanders’ gains and Trump’s gains is stronger in areas with large Latino populations. 


### Weighted (by Population) Least Squares Regression Table (w/Sanders-Latino Interaction)
**Dep. Variable: Trump Gain**

**R² = 0.52**

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
      <td style="text-align: right;">-0.0089</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-6.415</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">-0.012</td>
      <td style="text-align: right;">-0.006</td>
    </tr>
    <tr>
      <td><strong>White</strong></td>
      <td style="text-align: right;">-0.0050</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-3.094</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-0.008</td>
      <td style="text-align: right;">-0.002</td>
    </tr>
    <tr>
      <td><strong>Black or African American</strong></td>
      <td style="text-align: right;">0.0219</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">12.289</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.018</td>
      <td style="text-align: right;">0.025</td>
    </tr>
    <tr>
      <td><strong>Asian</strong></td>
      <td style="text-align: right;">0.0100</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">3.905</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.005</td>
      <td style="text-align: right;">0.015</td>
    </tr>
    <tr>
      <td><strong>Hispanic or Latino</strong></td>
      <td style="text-align: right;">0.0526</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">34.256</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.050</td>
      <td style="text-align: right;">0.056</td>
    </tr>
    <tr>
      <td><strong>Sanders_diff</strong></td>
      <td style="text-align: right;">-0.0387</td>
      <td style="text-align: right;">0.005</td>
      <td style="text-align: right;">-7.631</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">-0.049</td>
      <td style="text-align: right;">-0.029</td>
    </tr>
    <tr>
      <td><strong>Latino_SandersDiff_interaction</strong></td>
      <td style="text-align: right;">0.4400</td>
      <td style="text-align: right;">0.010</td>
      <td style="text-align: right;">44.464</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.421</td>
      <td style="text-align: right;">0.459</td>
    </tr>
    <tr>
      <td><strong>MedianIncome</strong></td>
      <td style="text-align: right;">-0.0012</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-1.658</td>
      <td style="text-align: right;">0.097</td>
      <td style="text-align: right;">-0.003</td>
      <td style="text-align: right;">0.000</td>
    </tr>
    <tr>
      <td><strong>CountyDensity</strong></td>
      <td style="text-align: right;">-0.0300</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-43.481</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">-0.031</td>
      <td style="text-align: right;">-0.029</td>
    </tr>
    <tr>
      <td><strong>MedianAge</strong></td>
      <td style="text-align: right;">0.0115</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">19.473</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.010</td>
      <td style="text-align: right;">0.013</td>
    </tr>
    <tr>
      <td><strong>College</strong></td>
      <td style="text-align: right;">0.0091</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">7.417</td>
      <td style="text-align: right;">0.000</td>
      <td style="text-align: right;">0.007</td>
      <td style="text-align: right;">0.011</td>
    </tr>
  </tbody>
</table>

Indeed, Sanders gains were much more predictive of Trump gains in heavily-Latino areas. This new Latino-Sanders Gain interaction term was the strongest variable and its inclusion decreased the predictive power of both Latino population and Sanders’ gain, suggesting combining both variables together predicts with Trump gains. Furthermore, the Sanders Gain variable jumped from the largest positive to largest negative coefficient, suggesting that Sanders Gain predicts Trump Gains in high-Latino areas, but actually predicts Trump Losses in areas with few Latinos.

One possible explanation for the larger Sanders-Latino interaction coefficient is that squaring the two ≤1.00 terms makes a small magnitude term, prompting the regression to inflate its coefficient value to compensate for the smaller value. To test that explanation, I squared the Latino and Sanders terms from the original regression and ran each squared term in individual regressions. The resulting coefficients were much smaller than the Sanders-Latino interaction term (0.0816, -0.0383 < 0.44), reaffirming the large coefficient reflects a strong predictive value of the interaction term.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Notes: Each instance in the regression was a unique 2020 Census Block Group, the most granular geography the Census publishes income and education data on. Using the Maup Python packege, I dis/aggregated Census block-level 2016-2020 Presidential General Election, block-level 2016 Democratic Primary, and precinct-level 2016 Democratic Primary data to the Block Group Level. To ensure standardized variable magnitudes, Income, County Density, and Median Age were transformed to a 0-1 uniform distribution (or 0.0-1.0 percentile scale) to align with the 0-1 (or -1 to 1 for Sanders/Trump Gain) percent format of the race, political, and College Attainment variables.

There were some missing and (geospatially) unmatchable precincts from the 2016 Democratic Presidential Primary, but 90% of precincts were able to be included. Importantly, the major metropolitan areas of Texas were included including >99% of the Rio Grande Valley. The bulk of these missing precincts were in sporadic small rural counties and pockets of Denton County (Dallas-Fort Worth suburbs). While the missing data is minor enough to not change the overall statistical pattern of the results, it still likely compromised the precision of certain estimates.

Full repository with source files and code will be uploaded shortly.
