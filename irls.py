from numpy import array, diag, dot, maximum, empty, repeat, ones, sum
from numpy.linalg import inv

def IRLS(y, x, maxiter, w_init = 1, d = 0.0001, tolerance = 0.001):
	n = x.shape[0]
        p = 1
	delta = array( repeat(d, n) ).reshape(1,n)
	w = repeat(1, n)
	W = diag( w )
	B = dot( inv( x.T.dot(W).dot(x) ), 
			 ( x.T.dot(W).dot(y) ) )
	for _ in range(maxiter):
		_B = B
		_w = abs(y - x.dot(B)).T
		w = float(1)/maximum( delta, _w )
		W = diag( w[0] )
		B = dot( inv( x.T.dot(W).dot(X) ), 
				 ( x.T.dot(W).dot(y) ) )
		tol = sum( abs( B - _B ) ) 
		if tol < tolerance:
			return B
        return B


#Test Example: Fit the following data under Least Absolute Deviations regression
# first line = "p n" where p is the number of predictors and n number of observations
# following lines are the data lines for predictor x and response variable y
#	 "<pred_1> ... <pred_p> y"
# next line win "n" gives the number n of test cases to expect
# following lines are the test cases with predictors and expected response
