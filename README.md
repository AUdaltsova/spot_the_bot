# spot the bot


## Data
Boted_data2.txt - all generated texts; for clusterization were divided into samples 4000 bytes each

Human_data.txt - all genuine human-written texts; for clusterization were divided into samples 4000 bytes each

## Data processing
generator.py - generating model for bot-written text (CREDIT: https://habr.com/ru/post/470035/, minor alterations were made)

vectorization.py - pre-processing and vectorization of the texts

vectors2.csv - resulting table of vectors, including filenames and class tags

## Clusterization
Spot_the_bot_K_means.py - clusterization via K-means, with and witout PCA (written in R)

Spot_the_bot_K_means - Colaboratory.pdf - copy of the Google Colaboratory for easier access, includes graphs
