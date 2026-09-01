import os
import shutil

def scan_tool():
    try:
        Filename = input("Enter a Filename : ")
        if not Filename :
            print("You Entered Nothing Please try again")
        else:
            with open(Filename, "r") as File:
                for line in File:
                    if "error" in line.lower():
                        print("Found Error:", line)
 
    except Exception as e:
        print("Something went wrong")
        print(e)
 #----------------------------------------------------------------------       
def backup_tool():
	try:
		source =input("Enter a source :")
		backup =input("Enter a backup :")
		
		if os.path.exists(source):
			if os.path.exists(backup):
				print("That folder already exists")
			else:
				shutil.copytree(source,backup)
				print("Folder was copied")
		else:
			print("Folder not found there")
	except Exception as e:
		print("Something went wrong")
		print(e)
        
#----------------------------------------------------------------------

def cleanup_tool():
    try:
        Folder =input("Enter a folder to clean :")
        
        if not Folder:
            print("You did not entered any folder")
            
        else:
            for file in os.listdir(Folder):
                path =os.path.join(Folder,file)
                
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                        print("Files were deleted")
                        
                    elif os.path.isdir(path):
                        os.rmdir(path)
                        print("Directories were deleted")
                        
                except Exception as e:
                    print("Something went wrong")
                    print(e)
                
    except Exception as e:
        print("Something went wrong((")
        print(e)
        
#----------------------------------------------------------------------

while True:
	print("-"*65)
	print("In====IT SUPPORT TOOLKIT====")
	print("1.Backup files")
	print("2.Scan log")
	print("3.Cleaning")
	print("4.Exit")
	
	print("-"*65)
	choice =input("Choose 1-4 :")
	print("-"*65)
	
	if not choice:
		print("You did not choose anything".upper())
		print("-"*65)
		
	elif choice == "1":
		print("Backup Selected".upper())
		print("-"*65)
		backup_tool()
		
	elif choice == "2":
		print("Scan Selected".upper())
		print("-"*65)
		scan_tool()
		
	elif choice == "3":
		print("Cleanup Selected".upper())
		print("-"*65)
		cleanup_tool()
		
	elif choice == "4":
		print("Exit.....".upper())
		break
		
	else:
		print("wrong choice,try again")
