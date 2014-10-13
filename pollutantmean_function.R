##  Function combines 332 csv files and calculates mean values for pollutants sulfate and nitrate.

pollutantmean <- function(directory,pollutant,id=1:332){
        sensor_files <- list.files("specdata",full.names=TRUE)
        compiled_data <- data.frame()

        for(i in id) {
                compiled_data <- rbind(compiled_data,read.csv(sensor_files[i])) 
        }
       sulfate <- compiled_data[,2]
       nitrate <- compiled_data[,3]
       mean(compiled_data[, pollutant], na.rm = TRUE)
}
