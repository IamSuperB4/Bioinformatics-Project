#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy

#Load the data
df = pd.read_csv('plotData/popsize_dn-ds.csv')

#Extract x and y data
x_data = list(df['social_group_size_difference'])
y_data = list(df['dNdS_ratio'])

print(x_data)
print(y_data)


#Clear the current figure to start fresh
plt.clf()

# Fit a regression line to the data
formula = "social_group_size_difference ~ dNdS_ratio"
model = smf.ols(formula,data=df)
model_fit = model.fit()
prediction = model_fit.get_prediction()
model_prediction_df = prediction.summary_frame()

#Get predicted values from the model
y_predicted = model_fit.fittedvalues

#Set up subplots
fig,ax = plt.subplots()

#We want scatterplot points and the thick line
#to plot on top of our shaded 95% confidence interval,
#so we plot the confidence interval first

#Plot a shaded area for the 95% prediction interval
#95% of future observed y values for a given x value should fall within this range
#Shade in the outermost confidence interval first, as it will be on bottom
#lower_obs_ci = model_prediction_df["obs_ci_lower"]
#upper_obs_ci = model_prediction_df["obs_ci_upper"]
#ax.fill_between(x_data,lower_obs_ci,upper_obs_ci,alpha=0.1,color='grey')

#Add dotted lines to the edges of the 95% prediction interval
#ax.plot(x_data,lower_obs_ci,alpha=0.75,marker=None,linestyle='dotted',color='grey',label="95% Confidence Interval of Observations")
#ax.plot(x_data,upper_obs_ci,alpha=0.75,marker=None,linestyle='dotted', color='grey')

#Plot a shaded area for the 95% confidence interval of the regression
#the true regression line (if the model is correct) should fall within this area 95% of the time
#lower_ci = model_prediction_df["mean_ci_lower"]
#upper_ci = model_prediction_df["mean_ci_upper"]
#ax.fill_between(x_data,lower_ci,upper_ci,alpha=0.2,color='crimson')

#Add dashed lines to the edges of the 95% confidence interval
#ax.plot(x_data,lower_ci,alpha=0.5,marker=None,linestyle='dashed',color='crimson',label="95% Confidence Interval of Mean")
#ax.plot(x_data,upper_ci,alpha=0.5,marker=None,linestyle='dashed',color='crimson')


#Plot the data points in black
ax.scatter(x_data,y_data,marker='o',color='black',edgecolor='black',linewidth=2)


#Set labels
ax.set_xlabel("Social Group Size Difference",size="xx-large")
ax.set_ylabel("dN/dS ratio",size="xx-large")

#Extract R2 from model and add to scatterplot
R2 = round(model_fit.rsquared,2)
ax.annotate(xy=(70,95),text=fr'$R^2 = {R2}$',size="xx-large")

#Extract p from the model and add to scatterplot
p = numpy.round(model_fit.f_pvalue,2)
ax.annotate(xy=(70,85),text=fr'$p = {p}$',size="xx-large")

#Plot the model fit line using a thick black line
ax.plot(x_data,y_predicted,label=f"Regression line ({formula})",color="red",linewidth=2)


#Get all the x-axis and y-axis ticklabels into lists
xticklabels = ax.get_xticklabels()
yticklabels = ax.get_yticklabels()

#Combine the lists  
all_tick_labels = xticklabels + yticklabels

#Call the set_fontsize method of each tick label
for label in all_tick_labels:
    label.set_fontsize("x-large")

#Save the figure
#dpi controls resolution in dots per square inch
#bbox_inches = 'tight' helps resize the figure so legends aren't cut off if outside the figure
plt.savefig("social_group_size_difference_vs_dNdS_ratio_version9.png",dpi=300,bbox_inches="tight")

print("end of code")