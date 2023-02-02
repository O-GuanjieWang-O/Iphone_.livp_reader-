import os

def livpToReadable(source):
     for file_name in os.listdir(source):
         if file_name.find("livp") != -1:
            temp = source +"\\"+file_name
            convert = lambda:os.system("7z x "+ "\""+temp+"\"" +" -o"+source)
            convert()
            delLivp = lambda:os.system("del "+"\""+temp+"\"")
            delLivp()

def main():
    livpToReadable(input("Enter source folder: "))
    
if __name__ == "__main__":
    main()
   