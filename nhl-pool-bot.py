#!/usr/bin/python3
'''
This program was written to make random selections in the NHL playoff pool.
'''
import yaml
import random
#  ArgumentParser passes variables directly into the app
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(
        description='Generates insults'
    )
    parser.add_argument(
        '-m',
        '--multiply',
        type=int,
        choices=[2, 3],
        help='multiplies the insult'
    )
    return parser.parse_args()


ARGS = create_parser()


def importdata():
    print("Importing data from data.yaml...")
    with open('data/data.yaml', 'r') as datafile:
        data = yaml.load(datafile, Loader=yaml.FullLoader)
    print("Import complete.")
    return data


def make_picks(data):
    print("Making random pick selections...")
    # CREATE PICKS STRUCTURE
    picks = {'roundrobin':{'east':{'match1':'','match2':'','match3':'', 'match4':'', 'match5':'', 'match6':''},'west':{'match1':'','match2':'','match3':'', 'match4':'', 'match5':'', 'match6':''}},'best_of_five':{'east':{'match1':'','match2':'','match3':'', 'match4':''},'west':{'match1':'','match2':'','match3':'', 'match4':''}}}
    # EAST ROUND ROBIN PICKS
    picks['roundrobin']['east']['match1'] = random.choice(data['roundrobin']['east']['match1'])
    picks['roundrobin']['east']['match2'] = random.choice(data['roundrobin']['east']['match2'])
    picks['roundrobin']['east']['match3'] = random.choice(data['roundrobin']['east']['match3'])
    picks['roundrobin']['east']['match4'] = random.choice(data['roundrobin']['east']['match4'])
    picks['roundrobin']['east']['match5'] = random.choice(data['roundrobin']['east']['match5'])
    picks['roundrobin']['east']['match6'] = random.choice(data['roundrobin']['east']['match6'])
    # WEST ROUNDROBIN PICKS
    picks['roundrobin']['west']['match1'] = random.choice(data['roundrobin']['west']['match1'])
    picks['roundrobin']['west']['match2'] = random.choice(data['roundrobin']['west']['match2'])
    picks['roundrobin']['west']['match3'] = random.choice(data['roundrobin']['west']['match3'])
    picks['roundrobin']['west']['match4'] = random.choice(data['roundrobin']['west']['match4'])
    picks['roundrobin']['west']['match5'] = random.choice(data['roundrobin']['west']['match5'])
    picks['roundrobin']['west']['match6'] = random.choice(data['roundrobin']['west']['match6'])
    # EAST BEST OF FIVE PICKS
    picks['best_of_five']['east']['match1'] = random.choice(data['best_of_five']['east']['match1']) + ' ' + str(random.randint(3, 5))
    picks['best_of_five']['east']['match2'] = random.choice(data['best_of_five']['east']['match2']) + ' ' + str(random.randint(3, 5))
    picks['best_of_five']['east']['match3'] = random.choice(data['best_of_five']['east']['match3']) + ' ' + str(random.randint(3, 5))
    picks['best_of_five']['east']['match4'] = random.choice(data['best_of_five']['east']['match4']) + ' ' + str(random.randint(3, 5))
    # WEST BEST OF FIVE PICKS
    picks['best_of_five']['west']['match1'] = random.choice(data['best_of_five']['west']['match1']) + ' ' + str(random.randint(3, 5))
    picks['best_of_five']['west']['match2'] = random.choice(data['best_of_five']['west']['match2']) + ' ' + str(random.randint(3, 5))
    picks['best_of_five']['west']['match3'] = random.choice(data['best_of_five']['west']['match3']) + ' ' + str(random.randint(3, 5))
    picks['best_of_five']['west']['match4'] = random.choice(data['best_of_five']['west']['match4']) + ' ' + str(random.randint(3, 5))
    print("Picks complete.") 
    return picks

def exportdata(picks):
    print("Beginning export of data to picks.yaml...")
    with open('data/picks.yaml', 'w') as picksfile:
        yaml.dump(picks, picksfile)
    print("Export to picks.yaml file complete.")

def main():
    data = importdata()
    picks = make_picks(data)
    exportdata(picks)


if __name__ == '__main__':
    main()
