# Title     : Space Clusters
# Objective : TODO
# Created by: NSora
# Created on: 2020/11/4

local({r <- getOption("repos")
 r["CRAN"] <- "http://mirrors.tuna.tsinghua.edu.cn/CRAN/"
options(repos=r)})

install.packages("fpc")
install.packages("factoextra")

library(sp)
library(maptools)
library(rgdal)
library(spatstat)
library(ggplot2)
library(stats)
library(fpc)
library(cluster)
library(factoextra)

csv_path <- "eqlist2.csv"

eq <- read.csv(csv_path, header = FALSE, sep = ",")
pv1 <- data.frame(-1*eq$V5, eq$V6,eq$V11,eq$V12)
pv2 <- scale(pv1)

fviz_nbclust(pv2, kmeans, method = "wss") + geom_vline(xintercept = 6, linetype=2)

ek <- kmeans(pv2, centers = 6, iter.max = 100)
fviz_cluster(ek, data=pv2)

res <- ek$cluster
cen <- ek$centers
d2 <- cbind(eq, type=ek$cluster)
write.csv(cen, "centers.csv")
write.csv(d2, "clusters.csv")