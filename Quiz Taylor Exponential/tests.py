# # Retunrs Min n, |x^{n+1}/(n+1)!| < epsilon and ∑_{i=1}^{n+1}  x^i/i!
# import math

# def Taylor_e_to_x_nterm_plus_one_less_epsilon(x, epsilon):
  
#    n = 0
#    e_to_x = 0
#    e_to_x_nterm = (x**n)/math.factorial(n)
#    e_to_x = e_to_x + e_to_x_nterm

#    while abs(e_to_x_nterm) > epsilon:
#       n += 1
#       e_to_x_nterm = (x**n)/math.factorial(n)
#       e_to_x = e_to_x + e_to_x_nterm

#    #Your code goes here

#    return n,e_to_x  #DO NOT change this line. Output will be read as a tuple.

# #run this sample textcase on a cell to help you validate your solution

# print(Taylor_e_to_x_nterm_plus_one_less_epsilon(x=35,epsilon=10**(-20)))

# #  --> Expected output: (132, 1586013452313431.2)

# print(Taylor_e_to_x_nterm_plus_one_less_epsilon(x=-35,epsilon=10**(-20)))

#  --> Expected output: (132, 6.305116760146987e-16)

# Returns Min n, |x^{n}/n!| < epsilon and ∑_{i=0}^{n} x^i/i!
import math

x = -35
epsilon = 10**(-20)

e_to_x = 0

delta = 1
i = 0
print("n".rjust(10)," ","∑_{i=0}^n x^i/i!".center(20)," "," delta=x^n/n!".center(20)," ","epsilon".center(9))
while  epsilon <= abs(delta):
  delta = x**i/math.factorial(i) 
  e_to_x += delta
  print(format(i, '10'),"  ", e_to_x,"  ",delta,"  ","{:.0e}".format(epsilon)) 
  i = i+1

print("n = ",i-1) 
print('x = ',x)
print('e_to_x ≈ ∑_{i=0}^'+str(i-1),'x^i/i! =',e_to_x)
print("epsilon =","{:.0e}".format(epsilon))     
print('math.exp(x) = ',math.exp(x))