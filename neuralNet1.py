import Math

def sig(x):
	return 1 / 1 + Math.exp(x)

def dout01_din01(x):
	return sig(x) * (1 - sig(x))

def dTotalError_outN1(real_answer, x):
	return -(real_answer - x)

def din01_dw(node):
	return sig(node) * 1

real_anwer = 10
def loop(INPUT1, INPUT2, w1, w2, w3, w4, answer): 
	if answer == real_answer:
		return 1;
	# forward prop
	inN1 = INPUT1 * w1 + b
	inN2 = INPUT2  * w2 + b
	outN1 = sig(inN1)
	outN2 = sig(inN2)
	in01 = outN1 * w3 + outN2 * w4
	g_ans = sig(in01)
	# back prop
	LEARN = 1
	TARGET = 5
	TotalError = 1/2((TARGER - out01)**2)
	dTotalError_dw3 = dTotalError_dout01(r_ans, g_ans) * dout01_din01(inN1) *  din01_dw(outN1)
	dTotalError_dw4 = dTotalError_dout01(r_ans, g_ans) * dout01_din01(inN2) *  din01_dw(outN2)

	w3 = w3 -  LEARN * dTotalError_dw3
	w4 = w4 - LEARN * dTotalError_dw4

	dTotalError_dw1 = dTotalError_outN1 * outN1_inN1 * inN1_w1
	dTotalError_dw2 = dTotalError_outN2 * outN2_inN2 * inN2_w2

	w1 = w1 - * LEARN * dTotalError_dw1j
	w2 = w2 - * LEARN * dTotalError_dw12	

	loop(w1, w2, w3, w4, answer)