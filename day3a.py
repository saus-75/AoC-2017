square = 289326
# square = 15

steps = 0

E_val = 1
N_val = 1
W_val = 1
S_val = 1

E_inc = 1
N_inc = 3
W_inc = 5
S_inc = 7

while ((E_val < square) or (N_val < square) or (W_val < square) or (S_val < square)):
    E_val += E_inc
    N_val += N_inc
    W_val += W_inc
    S_val += S_inc
    print ("East Value: " + str(E_val) + " Inc: " + str(E_inc))
    print ("North Value: " + str(N_val) + " Inc: " + str(N_inc))
    print ("West Value: " + str(W_val) + " Inc: " + str(W_inc))
    print ("South Value: " + str(S_val) + " Inc: " + str(S_inc) + "\n")
    E_inc += 8
    N_inc += 8
    W_inc += 8
    S_inc += 8
    steps += 1

print("Steps: " + str(steps))