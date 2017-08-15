# Output
After running conversant.py, the output should be as follows:
```VALUES ACROSS ALL DATA CENTERS
Min:  -4656151.122 @ 1443475260
Max:  61526.57778 @ 1443463920
Mean:  3228.61398439

VALUES OVER TIME AT ALL DATA CENTERS
Trend Line: y =  -0.0293379224851 x + 42351773.5917
Normalize Mean Square Error (0-1):  0.0364393034912
-------------------------------

VALUES AT EACH DATA CENTER...

VALUES AT DATA CENTER: I
Min:  -1630442.511 @ 1443457080
Max:  61526.57778 @ 1443463920
Mean:  24665.5000363

VALUES OVER TIME AT DATA CENTER:  I
Trend Line: y =  -0.111939717455 x + 161606681.036
Normalize Mean Square Error (0-1):  0.0568747894641

VALUES AT DATA CENTER: A
Min:  1219.941667 @ 1443495660
Max:  5861.477778 @ 1443529500
Mean:  3592.98099358

VALUES OVER TIME AT DATA CENTER:  A
Trend Line: y =  0.00819814411835 x + -11830234.0417
Normalize Mean Square Error (0-1):  0.21649832473

VALUES AT DATA CENTER: S
Min:  -4656151.122 @ 1443475260
Max:  20725.35148 @ 1443456720
Mean:  -11485.4757223

VALUES OVER TIME AT DATA CENTER:  S
Trend Line: y =  -0.00674685880623 x + 9727429.39968
Normalize Mean Square Error (0-1):  0.0545977897504
```

# Assumptions
1. The data file follows the format given.
2. None of the data will overflow the buffer on input.
3. None of the data points are outliers/errors.

# Findings
## Data Center: I
Despite the extreme minimum value (-1,630,442.511), the mean value at data center I is still high at 24,665.500. The trend line for data center I demonstrates a slight downward tragectory over time and the error indicates high volatility between data points (graph will look like a roller coaster).
## Data Center: A
Data center A on the other hand, does not contain any extreme minimums or maximums, with the range being only 4,641.536, The trend line for data center A demonstrates a slight upward tragectory over time and here the error indicates low volatility between data points (graph will be smoother).
## Data Center: S
In this case, the extreme minimum value (-4656151.122) appears to be drawing the mean lower as well (-11485.4757223). Again the trend line has a negative tragectory over time, and the error rate indicates high volatility.
## All Data Centers
The results from all data centers bears the burden of the skewed data from data centers I and S and thus also has a negative trend line over time and high volatility between data points.

# Challenges
Since none of the values were eliminated as outliers, a couple of extreme values skewed the data, making trend lines difficult to interpret.

# Extensions
## Visual Display
Line Graphs with time on the x-axis and value on the y-axis.
1. Plotting all data, regardless of data center
2. Plotting data separately for each data center
These graphs show turnpoints in the data that are not exemplified in the trend line.

## Removing Outliers
Since the nature of the data was unknown, removing outliers could have negative impacted the validity of the data; however, the results without outliers would be an interesting extension to more clearly see the trends.

## Other Types of Trend Lines
In some of these cases, perhaps different trend lines could better describe the data.

# Desired Information
1. Units for Value and Time
