# Funtion to write Contenders 
def write_contenders(Contenders):
    
    # Write to file
    with open("../configuration/config.py","w") as conf:
        conf.write(f"CONTENDERS = {repr(Contenders)}\n")
    
    # print
    print("Configuration Written!") 