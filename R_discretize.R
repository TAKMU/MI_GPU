lib <- "~/R/library"
dir.create(lib, showWarnings = FALSE, recursive = TRUE)
.libPaths(lib)
#pkgs <- c("infotheo", "optparse")
#install.packages(pkgs , repos = "https://cloud.r-project.org", dependencies = TRUE, lib = lib)
library(infotheo)
library(optparse)

#Argument parsing
option_list <- list(
    
  make_option(c("-w", "--working_dir"), type = "character", help = "Working directory", metavar = "path"),
  make_option(c("-i", "--input"), type = "character", help = "input file for discretization", metavar = "path"),
  make_option(c("-o", "--output"), type = "character", help = "Output path for discretized file", metavar = "path"))

opt <- parse_args(OptionParser(option_list = option_list))

wd <- opt$working_dir
setwd(wd)
iname <- opt$input
fname <- opt$output

df <- read.table(file = iname, header = TRUE, sep = ",")
df_dis <- discretize(df, disc="equalfreq", nbins=NROW(df)^(1/3) )
write.csv(df_dis, file = fname, )   



