import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--style',nargs='+',default=['all'])
base_info = parser.parse_args()

print (base_info.style)