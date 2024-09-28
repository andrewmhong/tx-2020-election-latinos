import pandas as pd
import numpy as np
import geopandas as gpd
import maup
import re
import statsmodels.api as sm
import os
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import StandardScaler
maup.progress.enabled = True


######################################################### leaning functions (boring) #########################################################

def swap_digits(id_value):
    id_str = str(id_value)
    if id_str.startswith('139'):
        id_list = list(id_str)
        id_list[3], id_list[4] = id_list[4], id_list[3]
        return int(''.join(id_list))
    return id_value

def clean_and_convert(column):
    def convert_value(x):
        cleaned = re.sub(r'\D', '', str(x))
        return int(cleaned) if cleaned else np.nan
    return column.apply(convert_value)

def sum_duplicate_columns(df):
    result = pd.DataFrame()
    for col in df.columns.unique():
        if df.columns.duplicated().any():
            result[col] = df.loc[:, df.columns == col].sum(axis=1)
        else:
            result[col] = df[col]
    return result

def clean_colname(col):
    col = col.replace('!!Total:!!', '')
    col = col.replace('!', '')
    col = col.replace('EstimateMale:', '')
    col = col.replace('EstimateFemale:', '')
    col = col.replace(' Hispanic or Latino', 'Hispanic or Latino')
    col = col.replace(' Total:', 'TotalPop')
    col = col.replace(' NotHispanic or Latino:', 'NotHispanic or Latino:')
    col = col.replace(' alone', '')
    col = col.replace('NotHispanic or Latino:Population of one race:', '')
    return col

######################################################### load in + clean census data #########################################################

# read in census dfs fron folder
dataframes = []
for filename in os.listdir('/Users/andrewhong/Desktop/Politics/Ref:Templates/Census/TX_BG_2020'):
    if filename.endswith('.csv'):
        file_path = os.path.join('/Users/andrewhong/Desktop/Politics/Ref:Templates/Census/TX_BG_2020', filename)
        df = pd.read_csv(file_path, skiprows=1)
        dataframes.append(df)

# join census dfs --> 1 df
df_census = dataframes[0]
for i, df in enumerate(dataframes[1:], start=1):
    df_census = df_census.merge(df, on='Geography', how='inner', suffixes=('', f'_df{i}'))

# cleaning... tread carefully (yes it's messy)
cols_to_drop = df_census.filter(regex='Margin of Error|Unnamed:|_df').columns
df_census = df_census.drop(columns=cols_to_drop).drop(
    columns=['EstimateMedian age --Male', 'EstimateMedian age --Female', 'NotHispanic or Latino:'], 
    errors='ignore'
)
df_census.columns = df_census.columns.map(clean_colname)
df_census['Geography'] = df_census['Geography'].str.extract(r'US(.+)')[0]


# combine mixed race people (ex: mixed white and asian) into each of their monoracial categories (ex: +1 white, +1 asian)
df_census = df_census[[col for col in df_census.columns if 'Population of' not in col or ('Population of' in col and 'alone' in col)]]
df_census = sum_duplicate_columns(df_census)

# aggregate granular demographic categories into few categorizations
no_college_cols = ['EstimateNo schooling completed', 'EstimateNursery school', 'EstimateKindergarten', 'Estimate1st grade', 'Estimate2nd grade', 'Estimate3rd grade', 'Estimate4th grade', 'Estimate5th grade', 'Estimate6th grade', 'Estimate7th grade', 'Estimate8th grade', 'Estimate9th grade', 'Estimate10th grade', 'Estimate11th grade', 'Estimate12th grade, no diploma', 'EstimateRegular high school diploma', 'EstimateGED or alternative credential', 'EstimateSome college, less than 1 year', 'EstimateSome college, 1 or more years, no degree', "EstimateAssociate's degree"]
college_cols = ["EstimateBachelor's degree", "EstimateMaster's degree", "EstimateProfessional school degree", "EstimateDoctorate degree"]
young_cols = ['18 and 19 years', '20 years', '21 years', '22 to 24 years', '25 to 29 years', '30 to 34 years']
midAge_cols = ['35 to 39 years', '40 to 44 years', '45 to 49 years', '50 to 54 years', '55 to 59 years', '60 and 61 years', '62 to 64 years']
old_cols = ['65 and 66 years', '67 to 69 years', '70 to 74 years', '75 to 79 years', '80 to 84 years', '85 years and over']
poor_cols = ['EstimateLess than $10,000', 'Estimate$10,000 to $14,999', 'Estimate$15,000 to $19,999', 'Estimate$20,000 to $24,999', 'Estimate$25,000 to $29,999', 'Estimate$30,000 to $34,999', 'Estimate$35,000 to $39,999', 'Estimate$40,000 to $44,999', 'Estimate$45,000 to $49,999']
midIncome_cols = ['Estimate$50,000 to $59,999', 'Estimate$60,000 to $74,999', 'Estimate$75,000 to $99,999']
rich_cols = ['Estimate$100,000 to $124,999', 'Estimate$125,000 to $149,999', 'Estimate$150,000 to $199,999', 'Estimate$200,000 or more']
df_census['NoCollege'] = df_census[no_college_cols].sum(axis=1)
df_census['College'] = df_census[college_cols].sum(axis=1)
df_census['18-34'] = df_census[young_cols].sum(axis=1)
df_census['35-64'] = df_census[midAge_cols].sum(axis=1)
df_census['>64'] = df_census[old_cols].sum(axis=1)
df_census['<50k'] = df_census[poor_cols].sum(axis=1)
df_census['50-100k'] = df_census[midIncome_cols].sum(axis=1)
df_census['>150k'] = df_census[rich_cols].sum(axis=1)

# aesthetic renaming
df_census = df_census.rename(columns={'EstimateMedian age --Total:': 'MedianAge',
                                        'EstimateMedian household income in the past 12 months (in 2020 inflation-adjusted dollars)': 'MedianIncome',
                                        })

# final cleaning
df_census['MedianIncome'] = clean_and_convert(df_census['MedianIncome'])
df_census['MedianAge'] = clean_and_convert(df_census['MedianAge'])

######################################################### load in county density data + join to census data #########################################################

# read in county pop. density df
df_density = pd.read_csv('/Users/andrewhong/Desktop/Politics/Ref:Templates/Census/Population-Density By County.csv')
df_density = df_density.rename(columns={'GCT_STUB.display-label': 'County',
                                        'Density per square mile of land area': 'CountyDensity',
                                        'GCT_STUB.display-label': 'County'
                                        })

# clean + join pop. density df to census df ==> 1 final demographic dataframe 
df_census['County_ID'] = df_census['Geography'].str[:5]
df_density['County_ID'] = df_density['GCT_STUB.target-geo-id'].str.extract(r'US(\d{5})')[0]
df_density['County_ID'] = df_density['County_ID'].astype(str)
df_demographics = pd.merge(df_census, df_density[['County', 'County_ID', 'CountyDensity']],
                     left_on='County_ID', right_on='County_ID', how='left')
df_demographics.drop(columns=['County_ID'], inplace=True)

# clean county col string values
df_demographics['County'] = df_demographics['County'].str.replace(' County', '')
df_demographics['County'] = df_demographics['County'].str.lower()

# ensure clean counts by BG for final demographic dataframe
numeric_columns = df_demographics.select_dtypes(include='number').columns
df_demographics = df_demographics.groupby('Geography')[numeric_columns].sum().reset_index()


######################################################### load in 2016 results and shapefiles #########################################################

# load in 2016 precinct shapefiles, 2020 primary + general result precinct shapefiles
print('...  loading in result files and shapefiles ...')
vtd_shapes16 = gpd.read_file('/Users/andrewhong/Desktop/Politics/Data/Consulting/BerniePOC2020/tx_vest_16_SHAPES/tx_vest_16.shp') # just shapefile

# load in 2016 primary results by precinct (csv)
vtd_primary_results16_csv = pd.read_csv('/Users/andrewhong/Desktop/Politics/Data/Consulting/BerniePOC2020/tx_2016pri_vtds.csv')

# clean ellis county vtds
vtd_primary_results16_csv['CNTYVTD'] = vtd_primary_results16_csv['CNTYVTD'].apply(swap_digits)

# clean + merge 2016 primary results <> 2016 precinct shapes
vtd_primary_results16_csv = vtd_primary_results16_csv.rename(columns={'CNTYVTD': 'PCTKEY'})
vtd_primary_results16_csv['PCTKEY'] = vtd_primary_results16_csv['PCTKEY'].astype(str).str.zfill(7).str.lower()
vtd_shapes16['PCTKEY'] = vtd_shapes16['PCTKEY'].astype(str).str.zfill(7).str.lower()
vtd_primary_results16 = vtd_shapes16.merge(vtd_primary_results16_csv, on='PCTKEY', how='left')

# load in 2016 general result by 2020 census block (shapefile)
block_results16 = gpd.read_file('/Users/andrewhong/Desktop/Politics/Data/Consulting/BerniePOC2020/tx_2016_gen_2020_blocks/tx_2016_gen_2020_blocks.shp')

# 2020 primary + general results as a shapefile
vtd_results20 = gpd.read_file('/Users/andrewhong/Desktop/Politics/Data/Consulting/BerniePOC2020/tx_20_vtd_gen_and_pri/tx_20_st_vtd.shp') 
print("all result files and shapefiles loaded!")
print()

######################################################### transform 2016, 2020 results into 2020 census blocks #########################################################

# maup (geospatially transform) 2016 precincts (2016 primary results) to join 2020 census blocks (2016 general results) 
print("mauping 2016...")
if block_results16.crs != vtd_primary_results16.crs: # ensure idential crs
    vtd_primary_results16 = vtd_primary_results16.to_crs(block_results16.crs)
election16_columns = ['JuddD_16P_President', 'De La FuenteD_16P_President', 'ClintonD_16P_President', 'LockeD_16P_President', "O'MalleyD_16P_President", 'SandersD_16P_President', 'WIlsonD_16P_President', 'HawesD_16P_President']
blocks_to_precincts_assignment = maup.assign(block_results16, vtd_primary_results16)
weights = block_results16.VAP_MOD / blocks_to_precincts_assignment.map(block_results16.VAP_MOD.groupby(blocks_to_precincts_assignment).sum()).fillna(0)
prorated = maup.prorate(blocks_to_precincts_assignment, vtd_primary_results16[election16_columns], weights)
block_results16[election16_columns] = prorated
block_results16[election16_columns].round(2).head()
print("2016 results mauped")
print()

# maup (geospatially transform) 2016 precincts (2016 primary results) to join 2020 census blocks (2016 general results) 
print("mauping 2020 ...")
if block_results16.crs != vtd_results20.crs:
    vtd_results20 = vtd_results20.to_crs(block_results16.crs)
election20_columns = [col for col in vtd_results20.columns if 'P20PRED' in col] + [col for col in vtd_results20.columns if 'G20PRE' in col]
blocks_to_precincts_assignment = maup.assign(block_results16, vtd_results20)
weights = block_results16.VAP_MOD / blocks_to_precincts_assignment.map(block_results16.VAP_MOD.groupby(blocks_to_precincts_assignment).sum()).fillna(0)
prorated = maup.prorate(blocks_to_precincts_assignment, vtd_results20[election20_columns], weights)
block_results16[election20_columns] = prorated
block_results16[election20_columns].round(2).head()

block_results = block_results16
print(block_results)
print("2020 results mauped")
print()

######################################################### aggregate political data to Census BGs (census demographic data geo) #########################################################

print("... merging final dfs ...")

# load in block groups
bg_shapes = gpd.read_file('/Users/andrewhong/Desktop/Politics/Ref:Templates/Shapefiles/tx_bgs_2020/tl_2020_48_bg.shp')

# change geography id from block --> block group
block_results['Geography'] = block_results['GEOID20'].str[:-3]

# aggregate numeric cols from block (smaller) --> block group (bigger)
block_results_clean = block_results.groupby('Geography')[block_results.select_dtypes(include='number').columns].sum()

# add corrected geography to block_results_clean --> geodataframe
bg_shapes['Geography'] = bg_shapes['GEOID']
block_results_clean = block_results_clean.join(bg_shapes.set_index('Geography'), on='Geography')
block_results_clean = gpd.GeoDataFrame(block_results_clean, geometry='geometry')

# merge political data to census demographic data --> 1 dataframe
df = block_results_clean
df = df.merge(block_results_clean.drop(columns=['geometry']), on='Geography', how='inner')
df = df.merge(df_demographics, on='Geography', how='inner')
print(df)


######################################################### calculate %'s from raw counts per BG for regressions #########################################################

# identify columns to extract percentages from --> extract percentages
columns_to_divide = ['Hispanic or Latino', 'White', 'Black or African American', 'American Indian and Alaska Native', 'Asian', 'Native Hawaiian and Other Pacific Islander', 'Some Other Race', 'NoCollege', 'College', '18-34', '35-64', '>64', '<50k', '50-100k', '>150k']
for col in columns_to_divide:
    df[col] = df[col] / df['TotalPop']

# get percentages for key political columns
df['Sanders20'] = df['P20PREDSAN_x'] / (df.filter(like='P20PRED').sum(axis=1))
df['Sanders_diff'] = (df['P20PREDSAN_x'] / (df.filter(like='P20PRED').sum(axis=1))) - (df['SandersD_16P_President_x'] / (df.filter(like='_16P_President').sum(axis=1)))
df['Trump_diff'] = (df['G20PRERTRU_x'] / (df.filter(like='G20PRE').sum(axis=1))) - (df['G16PRERTRU_x'] / (df.filter(like='G16PRE').sum(axis=1)))


######################################################### save final geodataframe #########################################################

df.to_file('/Users/andrewhong/Desktop/Politics/Data/Consulting/BerniePOC2020/tx_cleaned_gdf.shp')
print("geodataframes loaded")


######################################################### regression models #########################################################

# wls model 1: no interaction term
regression_vars = ['White', 'Black or African American', 'Asian', 'Hispanic or Latino', 'Trump_diff', 'Sanders_diff', 'MedianIncome', 'CountyDensity', 'MedianAge', 'College', 'TotalPop']
regression_df = df[regression_vars]
regression_df = regression_df.apply(pd.to_numeric, errors='coerce')
regression_df = regression_df.dropna()
scaler = QuantileTransformer(output_distribution='uniform') # percentile from 0-1
regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']] = scaler.fit_transform(regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']])
X = regression_df.drop(columns=['Trump_diff', 'TotalPop'])
y = regression_df['Trump_diff']
X = sm.add_constant(X)
weights = 1 / regression_df['TotalPop']
model = sm.WLS(y, X, weights=weights).fit()
print(model.summary())


# wls model 2: with interaction term
df['Latino_SandersDiff_interaction'] = df['Hispanic or Latino'] * df['Sanders_diff'] # interaction term in question
regression_vars = ['White', 'Black or African American', 'Asian', 'Hispanic or Latino', 'Trump_diff', 'Sanders_diff', 'Latino_SandersDiff_interaction', 'MedianIncome', 'CountyDensity', 'MedianAge', 'College', 'TotalPop']
regression_df = df[regression_vars]
regression_df = regression_df.apply(pd.to_numeric, errors='coerce')
regression_df = regression_df.dropna()
scaler = QuantileTransformer(output_distribution='uniform') # percentile from 0-1
regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']] = scaler.fit_transform(regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']])
X = regression_df.drop(columns=['Trump_diff', 'TotalPop'])
y = regression_df['Trump_diff']
X = sm.add_constant(X)
weights = 1 / regression_df['TotalPop']
model = sm.WLS(y, X, weights=weights).fit()
print(model.summary())


###################### tests: squaring latino, sanders_diff terms to ensure interaction term is not just picking up squared (smaller) magnitude ######################

# test 1: sanders_shift sqaured only
df['Sanders_diff_squared'] = df['Sanders_diff'] * df['Sanders_diff'] * np.where(df['Sanders_diff'] > 0, 1, -1)
regression_vars = ['White', 'Black or African American', 'Asian', 'Trump_diff', 'Sanders_diff_squared', 'MedianIncome', 'CountyDensity', 'MedianAge', 'College', 'TotalPop']
regression_df = df[regression_vars]
regression_df = regression_df.apply(pd.to_numeric, errors='coerce')
regression_df = regression_df.dropna()
scaler = QuantileTransformer(output_distribution='uniform') # percentile from 0-1
regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']] = scaler.fit_transform(regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']])
X = regression_df.drop(columns=['Trump_diff', 'TotalPop'])
y = regression_df['Trump_diff']
X = sm.add_constant(X)
weights = 1 / regression_df['TotalPop']
model = sm.WLS(y, X, weights=weights).fit()
print(model.summary())

# test 2: hispanic squared only
df['Hispanic or Latino squared'] = df['Hispanic or Latino'] * df['Hispanic or Latino']
regression_vars = ['White', 'Black or African American', 'Asian', 'Hispanic or Latino squared', 'Trump_diff', 'MedianIncome', 'CountyDensity', 'MedianAge', 'College', 'TotalPop']
regression_df = df[regression_vars]
regression_df = regression_df.apply(pd.to_numeric, errors='coerce')
regression_df = regression_df.dropna()
scaler = QuantileTransformer(output_distribution='uniform') # percentile from 0-1
regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']] = scaler.fit_transform(regression_df[['MedianIncome', 'MedianAge', 'CountyDensity']])
X = regression_df.drop(columns=['Trump_diff', 'TotalPop'])
y = regression_df['Trump_diff']
X = sm.add_constant(X)
weights = 1 / regression_df['TotalPop']
model = sm.WLS(y, X, weights=weights).fit()
print(model.summary())
