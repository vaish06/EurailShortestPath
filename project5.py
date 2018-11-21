from TripPlanner import *
import argparse
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This Program Processes a time'
                         'table of weighted connected route system and returns'
                         ' the fastest routes for requested destinations.')
    parser.add_argument('timeTable',help='Route system file-src,des,hours:mins')
    parser.add_argument('--itinerary ', dest='itinerary', default=None,
                        help='Writes the requested routes into a Graph '
                             'Visualization File(.gv).')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args:
        railS = TripPlanner(args.timeTable,args.itinerary)
        railS.UI()
    else:
        parser.print_help()