#phosphate buffer calculator using functions, lists, and for loops
buffers = ["citrate", "phosphate", "acetate", "carbonate"]

for buffer in buffers:
    print("" + buffer)

chosen_buffer = input("Which buffer would you like to prepare? ").lower()

if chosen_buffer == "phosphate":
    buffer_pH = float(input("Enter the desired pH of the buffer solution:  "))
    buffer_conc = float(input("Enter the total concentration of the buffer solution in M: "))
    buffer_vol = float(input("Enter the total volume of the buffer solution in mL: "))

    def calculate_phosphate_buffer(buffer_pH, buffer_conc):
        
        if buffer_pH > 2.1249 and buffer_pH < 12.44369:
            pKa1 = 2.1249 # pKa for H3PO4 to H2PO4-
          
            ratio = 10 ** (buffer_pH - pKa1)
            acid_concentration = buffer_conc/(ratio - 1)
            base_concentration = buffer_conc - acid_concentration
            print("")
            print(f"Acid concentration (M): {acid_concentration:.8f}")
            print(f"Base concentration (M): {base_concentration:.8f}")
    
            acid_vol = (acid_concentration * buffer_vol)/14.6
            base_mass = (base_concentration * 119.977)
            print("")
            print(f"Volume of phosphoric acid: {acid_vol:.6f} mL")
            print(f"Mass of sodium phosphate: {base_mass:.6f} g")
    
            print("")
            print("PROCEDURE")
            print(f"In a 1.0 L volumetric flask, dissolve {base_mass:.4f} g of anhydrous NaH2PO4- in deionized water.")
            print(f"Add {acid_vol:.2f} mL of 85% w/w phosphoric acid.")
            print(f"Add deionized water until mark and shake thoroughly.")
    
            return acid_concentration, base_concentration, acid_vol, base_mass

        else:
            print("The selected pH is outside the effective range for phosphate buffer.")
        
        calculate_phosphate_buffer (buffer_pH, buffer_conc, buffer_vol) #code for phosphate buffer calc ends here

elif chosen_buffer == "citrate":
    print("Citrate buffer calculator coming soon.")
    
elif chosen_buffer == "acetate":
    print("Acetate buffer calculator coming soon.")
    
elif chosen_buffer == "carbonate":
    print("Carbonate buffer calculator coming soon.")
    
else:
    print("Sorry, that buffer is not available. Please choose from the following: citrate, phosphate, acetate, carbonate.")
    

