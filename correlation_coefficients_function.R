## Function which merges 332 csv files into single data frame before it calculates correlatin coefficients between variables sulfate and nitrate.

corr <- function(directory,threshold=0){
        sensor_files <- list.files("specdata", pattern = "csv", full.names=TRUE)
        compiled_data <- data.frame()
        corr_coef <- vector() # vector to put correlation coefficients into 
        for(i in 1:332) {
                compiled_data<-rbind(compiled_data,read.csv(filelist[i])) 
        }
        comp <- na.omit(compiled_data) # data frame with NAs removed
        sum <- as.data.frame(table(comp$ID))
        colnames(sum) <- c("id", "count") # summary table completed with named columns
        if(sum$count > threshold) {
                corr_coef <- c(corr_coef, cor(comp$sulfate, comp$nitrate))     

        }
}
