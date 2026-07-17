# Funtion to write Contenders 
def write_contenders(Contenders,rivals):
    
    # Write to file
    with open("../../configuration/config.py","w") as conf:
        conf.write(f"CONTENDERS = {repr(Contenders)}\n")
        conf.write(f"RIVALS = {repr(rivals)}")
    
    # print
    print("Configuration Written!") 