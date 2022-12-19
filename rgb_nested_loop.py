 #!/usr/bin/env python3
# Created By: Frankie
# Date: Dec. 16, 2022
# This program shows the amount fo RGB
 
def main():
 
    # initialize the colors
    red = 0
    green = 0
    blue = 0
 
    # display opening message
    print("Here are RGB colour variations up to 50:")
    print("")
 
    # determines the different color codes
    # displays output to the console
    for blue in range(0, 51, 1):
        print("RGB ({}, {}, {})".format(red, green, blue))
        if blue == 50:
            print("")
            for green in range(1, 51, 1):
                blue = 0
                print("RGB ({}, {}, {})".format(red, green, blue))
                if green == 50:
                    print("")
                    for red in range(1, 51, 1):
                        green = 0
                        print("RGB ({}, {}, {})".format(red, green, blue))
 
 
if __name__ == "__main__":
    main()
