#hanoi tower
'''
    I          I          I
    A          B          C
    -
1   --
  
2               
    --         -

3                        -
                         --

'''
# a_pole => source pole
# b_pole => intermediate pole
# c_pole => destination_pole

def hanoi(n,a_pole, b_pole, c_pole):
    if n == 1:
        print(f'Move disk 1 from pole {a_pole} to pole {b_pole}')
        return
    hanoi(n-1,a_pole,c_pole,b_pole)
    print(f'Move disk {n} from pole {a_pole} to pole {b_pole}')
    hanoi(n-1,c_pole,b_pole,a_pole)


n=2
hanoi(n,'A','B','C')
