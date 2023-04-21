#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
   length = len(input_x)
   print (f'input x: {input_x} , input y: {input_y}')
   cov = 0

   mean_x = statistics.mean (input_x)
   mean_y = statistics.mean (input_y)
   print (f'mean x: {mean_x} , mean y: {mean_y}')

   cov = sum ({(input_x[1]-mean_x)*(input_y[1]-mean_y) for 1 in range(length)}) /length
   
   return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'covariance: {answer}')
