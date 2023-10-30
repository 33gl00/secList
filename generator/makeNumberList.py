#####################
# ID LIST GENERATOR #
#####################

import argparse
parser = argparse.ArgumentParser(
                    prog = 'miniMoulinette',
                    description = 'builDico',
                    epilog = 'python3 minimoulinette.py --output dico_ID.txt --limit 9999')

parser.add_argument('-o', '--output', type=str, required=True, help="")
input = parser.parse_args()
idList = input.output
limit = input.limit

########################
# Reprint
lastPrintSize = 0

def reprint(txt, finish=False) :
	global lastPrintSize
	print(' '*lastPrintSize, end='\r')

	if finish:
		end = "\n"
		lastPrintSize = 0
	else : 
		end = "\r"
		lastPrintSize = len(txt)
	print(txt, end=end)
########################


for i in range(1, limit):
    reprint(str(i))
    with open(idList, 'a') as f:
        f.write(str(i) + "\n")

reprint("output File : " + idList ,True)
###############################~~ eegloo