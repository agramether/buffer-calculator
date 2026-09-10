buffers = ["1. acetate", "2. carbonate", "3. citrate", "4. phosphate"]

for buffer in buffers:
    print("" + buffer)
    
chosen_buffer = input("Which buffer would you like to prepare? ").lower()

if chosen_buffer == "1":
    acetate_pH = float(input("Enter the desired pH of the buffer solution:  "))
    acetate_con = float(input("Enter the total concentration of the buffer solution in M: "))
    acetate_vol = float(input("Enter the total volume of the buffer solution in mL: "))
    
    def calculate_acetate(acetate_pH, acetate_con):
        acetate_pKa = ["4.74472", "1"]
        
        if acetate_pH > 3.74472 and acetate_pH < 5.74472:
            ratio = acetate_pH - float(acetate_pKa[0])
            print(f"This is the ratio of base to acid: {ratio}")
            
            acid_con = acetate_con / (ratio - 1)
            base_con = acetate_con - acid_con
            print("")
            print(f"Acid concentration (M): {acid_con:.6f}")
            print(f"Base concentration (M): {base_con:.6f}")
        
        return acetate_pH, acetate_con, ratio
      
    calculate_acetate (acetate_pH, acetate_con)
    
 #cabonate pkas
    #pka1 = 6.37675
    #pka2 = 10.31875
    

            
            



