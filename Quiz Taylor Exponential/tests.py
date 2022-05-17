# Retunrs Min n, |x^{n+1}/(n+1)!| < epsilon and ∑_{i=1}^{n+1}  x^i/i!
import math

def Taylor_e_to_x_nterm_plus_one_less_epsilon(x, epsilon):
  
   n = 0
   x0 = x
   if x < 0:
      x = - x
   e_to_x = 0
   e_to_x_nterm = (x**n)/math.factorial(n)
   e_to_x = e_to_x + e_to_x_nterm

   while abs(e_to_x_nterm) > epsilon:
      n += 1
      x_to_i = 1
      fact_of_i = 1
      for k in range(1, n):
         x_to_i *= x
         fact_of_i *= k
      e_to_x_nterm = x_to_i/fact_of_i
      e_to_x = e_to_x + e_to_x_nterm


      # e_to_x_nterm = (x**n)/math.factorial(n)
      # e_to_x = e_to_x + e_to_x_nterm
   if x != x0:
      e_to_x = 1/e_to_x
      x = x0
      

   #Your code goes here

   return n,e_to_x  #DO NOT change this line. Output will be read as a tuple.

#run this sample textcase on a cell to help you validate your solution

print(Taylor_e_to_x_nterm_plus_one_less_epsilon(x=35,epsilon=10**(-20)))

#  --> Expected output: (132, 1586013452313431.2)

print(Taylor_e_to_x_nterm_plus_one_less_epsilon(x=-35,epsilon=10**(-20)))

# --> Expected output: (132, 6.305116760146987e-16)