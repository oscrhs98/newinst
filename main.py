import argparse
from time import sleep
from New_start import startChrome
from igProfile import Profile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--account", help="Account to run (m for MexicanTest, d for GermanyTest, Account name for other)")
    parser.add_argument("-p", "--password", help="Password to account", default= None)
    #parser.add_argument("-d", "--drive", help="Will drive download Info", default=False, action="store_true")

    args = parser.parse_args()

    if (args.account == "m"):
        Bot = startChrome('photoandtravel2020','mannheimzittau', args)
    
    elif (args.account == "d"):
        Bot = startChrome('travelandphoto2020','mannheimzittau', args)
    else:
        account = args.account
        password = args.password
        print("You entered: " + account)
        print("You entered: " + password)
        sleep(2)
        Bot = startChrome(account,password, args)
    Profile(Bot)
    sleep(1000)

        


if __name__ == "__main__":
    main()