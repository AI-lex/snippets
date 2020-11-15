
states <- read.csv("data/stateData.csv")

head(states)
names(states)
dim(states)
str(states)
summary(states)

states$population


mean(states$population[0:2])
states_upper_quantile <- subset(states, population >= quantile(states$population)[4])
states_upper_quantile
states$population_reduced <- states$population - 200

table(states$state.abb)

install.packages('devtools', dependencies = T)
library(devtools)
install_version("colorspace","1.2-4")

install.packages('ggplot2', dependencies = T)
#install.packages('ggplot2')
library(ggplot2)
