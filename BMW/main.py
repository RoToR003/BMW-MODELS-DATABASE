import src.E
import src.X
import src.I
import src.M
import src.F
import src.Z
from termcolor import colored
import os
import sys

def logo():
    bold_text = colored('\033[96m/\033[94m/\033[91m/\033[38;5;252mМ\033[0', attrs=['bold'])
    print(bold_text)


def BMW(model):
    for car in src.Z.bmw_z_models+src.E.bmw_e_models+src.X.bmw_x_models+src.I.bmw_i_models+src.M.bmw_m_models+src.F.bmw_f_models:
        if car['model'].lower() == model.lower():
            print("\033[96mModel: \033[38;5;214m{}".format(car['model']))
            print("\033[96mEngine: \033[38;5;214m{}".format(car['engine']))
            print("\033[96mWeight: \033[38;5;214m{}".format(car['weight']))
            print("\033[96mYear: \033[38;5;214m{}".format(car['year']))
            print("\033[96mAcceleration: \033[38;5;214m{}".format(car['acceleration']))
            print("\033[96mTop Speed: \033[38;5;214m{}".format(car['top_speed']))
            print("\033[96mHorsepower: \033[38;5;214m{}".format(car['horsepower']))
            print("\033[38;5;103mFeatures: \033[38;5;170m{}".format(car['features']))
            break
    else:
        print("\033[91mSorry, we do not have information about this BMW model.")


def help():
    print(colored('\033[96menter the name of the model like \033[91m(z1, E60, x5)\033[96m\nto exit enter \033[91m"exit"\033[96m\ntype \033[91m"info"\033[96m to display code details', attrs=['bold']))
    
def info():
    print(colored('\033[96mthe database for the code was generated using \033[1;35mGPT-3\033[96m \nin a database of about \033[1;35m92 models\n\033[91mauthor\033[91m[\033[38;5;214mRoToR003\033[0m\033[91m]', attrs=['bold']))

def titles():
    logo()
    help()
    info()
titles()
while True:
    model = input("\033[38;5;250mEnter BMW model: ")
    if model=='help':
        os.system('cls || clear')
        logo()
        help()
    elif model=='exit':
        sys.exit(0)
    elif model=='info':
        os.system('cls || clear')
        logo()
        info()
    else:
        os.system('cls || clear')
        logo()
        BMW(model)
        