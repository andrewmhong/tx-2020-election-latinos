# tx-2020-election-latinos
Split Ticket 2020 Election TX Latinos Analysis

## Regression Output

### Weighted (by Population) Least Squares Regression Table
**Dep. Variable: Trump Gain**

**R² = 0.46**


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
      <td style="text-align: right;">-0.0178</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-12.087</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.021</td>
      <td style="text-align: right;">-0.015</td>
    </tr>
    <tr>
      <td><strong>White</strong></td>
      <td style="text-align: right;">0.0079</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">4.652</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.005</td>
      <td style="text-align: right;">0.011</td>
    </tr>
    <tr>
      <td><strong>Black or African American</strong></td>
      <td style="text-align: right;">0.0196</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">9.964</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.016</td>
      <td style="text-align: right;">0.023</td>
    </tr>
    <tr>
      <td><strong>Asian</strong></td>
      <td style="text-align: right;">0.0248</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">9.166</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.020</td>
      <td style="text-align: right;">0.030</td>
    </tr>
    <tr>
      <td><strong>Hispanic or Latino</strong></td>
      <td style="text-align: right;">0.0637</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">38.461</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.060</td>
      <td style="text-align: right;">0.067</td>
    </tr>
    <tr>
      <td><strong>Sanders Gain</strong></td>
      <td style="text-align: right;">0.1457</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">47.86</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.14</td>
      <td style="text-align: right;">0.152</td>
    </tr>
    <tr>
      <td><strong>Median Income</strong></td>
      <td style="text-align: right;">-0.0031</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-3.702</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.005</td>
      <td style="text-align: right;">-0.001</td>
    </tr>
    <tr>
      <td><strong>County Pop. Density</strong></td>
      <td style="text-align: right;">-0.0287</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-39.511</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.030</td>
      <td style="text-align: right;">-0.027</td>
    </tr>
    <tr>
      <td><strong>Median Age</strong></td>
      <td style="text-align: right;">0.0141</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">22.669</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.013</td>
      <td style="text-align: right;">0.015</td>
    </tr>
    <tr>
      <td><strong>College</strong></td>
      <td style="text-align: right;">0.0105</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">8.095</td>
      <td style="text-align: right;">0</td>
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
      <td style="text-align: right;">-0.0081</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-5.698</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.011</td>
      <td style="text-align: right;">-0.005</td>
    </tr>
    <tr>
      <td><strong>White</strong></td>
      <td style="text-align: right;">-0.006</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-3.66</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.009</td>
      <td style="text-align: right;">-0.003</td>
    </tr>
    <tr>
      <td><strong>Black or African American</strong></td>
      <td style="text-align: right;">0.0201</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">10.757</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.016</td>
      <td style="text-align: right;">0.024</td>
    </tr>
    <tr>
      <td><strong>Asian</strong></td>
      <td style="text-align: right;">0.0088</td>
      <td style="text-align: right;">0.003</td>
      <td style="text-align: right;">3.382</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">0.004</td>
      <td style="text-align: right;">0.014</td>
    </tr>
    <tr>
      <td><strong>Hispanic or Latino</strong></td>
      <td style="text-align: right;">0.0512</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">32.132</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.048</td>
      <td style="text-align: right;">0.054</td>
    </tr>
    <tr>
      <td><strong>Sanders Gain</strong></td>
      <td style="text-align: right;">-0.0384</td>
      <td style="text-align: right;">0.005</td>
      <td style="text-align: right;">-7.571</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.048</td>
      <td style="text-align: right;">-0.028</td>
    </tr>
    <tr>
      <td><strong>Latino-Sanders Gain Interaction</strong></td>
      <td style="text-align: right;">0.438</td>
      <td style="text-align: right;">0.01</td>
      <td style="text-align: right;">44.169</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.419</td>
      <td style="text-align: right;">0.457</td>
    </tr>
    <tr>
      <td><strong>Median Income</strong></td>
      <td style="text-align: right;">-0.0025</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-3.1</td>
      <td style="text-align: right;">0.002</td>
      <td style="text-align: right;">-0.004</td>
      <td style="text-align: right;">-0.001</td>
    </tr>
    <tr>
      <td><strong>County Pop. Density</strong></td>
      <td style="text-align: right;">-0.03</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">-43.517</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">-0.031</td>
      <td style="text-align: right;">-0.029</td>
    </tr>
    <tr>
      <td><strong>Median Age</strong></td>
      <td style="text-align: right;">0.0114</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">19.204</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.01</td>
      <td style="text-align: right;">0.013</td>
    </tr>
    <tr>
      <td><strong>College Attainment</strong></td>
      <td style="text-align: right;">0.0093</td>
      <td style="text-align: right;">0.001</td>
      <td style="text-align: right;">7.568</td>
      <td style="text-align: right;">0</td>
      <td style="text-align: right;">0.007</td>
      <td style="text-align: right;">0.012</td>
    </tr>
  </tbody>
</table>

Indeed, Sanders gains were much more predictive of Trump gains in heavily-Latino areas. This new Latino-Sanders Gain interaction term was the strongest variable and its inclusion decreased the predictive power of both Latino population and Sanders’ gain, suggesting combining both variables together predicts with Trump gains. Furthermore, the Sanders Gain variable jumped from the largest positive to largest negative coefficient, suggesting that Sanders Gain predicts Trump Gains in high-Latino areas, but actually predicts Trump Losses in areas with few Latinos.

One possible explanation for the larger Sanders-Latino interaction coefficient is that squaring the two ≤1.00 terms makes a small magnitude term, prompting the regression to inflate its coefficient value to compensate for the smaller value. To test that explanation, I squared the Latino and Sanders terms from the original regression. The resulting correlation coefficients were much smaller than the Sanders-Latino interaction term (0.0813, 0.2442 < 0.438), reaffirming the large coefficient reflects a strong predictive value of the interaction term.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Notes: Each instance in the regression was a unique 2020 Census Block Group, the most granular geography the Census publishes income and education data on. Using the Maup Python packege, Census block-level 2016-2020 Presidential General Election, block-level 2016 Democratic Primary, and precinct-level 2016 Democratic Primary data was aggregated to the Block Group Level. To ensure standardized variable magnitudes, Income, County Density, and Median Age were transformed to a 0-1 uniform distribution (or 0.0-1.0 percentile scale) to align with the 0-1 (or -1 to 1 for Sanders/Trump Gain) percent format of the race, political, and College Attainment variables.

There were some missing precinct data from the 2016 Democratic Presidential Primary, but 90% of precincts are included. Importantly, the major metropolitan areas of Texas were included including >99% of the Rio Grande Valley. The bulk of these missing precincts were in random rural, small counties and pockets of Denton County (Dallas-Fort Worth suburbs). While the missing data is minor enough to not change the overall result, it still likely alters the precision of certain estimates.

Full repository with source files and code will be uploaded shortly.
