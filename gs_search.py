#!/usr/bin/env python3

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import argparse
import copy
import sys

def parse_arguements():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",
                        "--search_string",
                        type=str,
                        help="search string")
    parser.add_argument("-i",
                        "--ssid",
                        help="spreadsheet ID",
                        type=str,
                        default='1auUAk4Go6t8U4wFYc3jv-sQBSVnF4AQEBu5qf7K-eWY')
    parser.add_argument("-t",
                        "--title_row",
                        help="A1 format: the row of the title",
                        type=str,
                        default='A1:E1')
    parser.add_argument("-d",
                        "--data_range",
                        help="A1 format: the range of data",
                        type=str,
                        default='2:400')

    if len(sys.argv[1:])==0:
        parser.print_help()
        # parser.print_usage() # for just the usage line
        parser.exit()
    args = parser.parse_args()
    return args

def get_data(SSID, TITLE_ROW, SSRange):
    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    title_result = service.spreadsheets().values().get(spreadsheetId=SSID,
                                                 range=TITLE_ROW).execute()
    result = service.spreadsheets().values().get(spreadsheetId=SSID,
                                                 range=SSRange).execute()
    title_values = title_result.get('values', [])[0]
    values = result.get('values', [])
    return values, title_values

def search_for_string(values, search_string):
    # unpack the lists and search for a string
    matches = []
    for sublist in values:
        for item in sublist:
            if search_string.lower() in item.lower():
                matches.append(sublist)
    return matches

def print_title_row(title_values):
    # print out the title row of the spreadsheet
    print('\n')
    print('_'*203)
    print('|{:^50.50} | {:^50.50} | {:^30.30} | {:^30.30} | {:^30.30}|'.
        format(title_values[0],
         title_values[1],
         title_values[2],
         title_values[3],
         title_values[4] ))
    print('_'*203)
    print('\n')

def print_data(matches):
    if not matches:
        print('No data found.')
    else:
        # sanitize the row of data
        complete_row = ["-"] * 5
        for row in matches:
            for x in range(0, 5):
              try:
                complete_row[x] = row[x]
              except IndexError:
                continue
            # TripleO Service and Default
            # allow for 50 chars in space, and truncate at 50 chars
            # puppet and docker
            # allow for 30 chars in space, and truncate at 30 chars
            # print out the values from the spreadsheet
            try:
                print('|{:^50.50} | {:^50.50} | {:^30.30} | {:^30.30} | {:^30.30}|'.format(
                      complete_row[0],
                      complete_row[1],
                      complete_row[2],
                      complete_row[3],
                      complete_row[4]))

            except IndexError:
                print('skip line')

def main():
    # Settings
    args = parse_arguements()

    TITLE_ROW = str(args.title_row)
    SPREADSHEET_ID = str(args.ssid)
    RANGE_NAME = str(args.data_range)

    # get and print data
    values, title_values = get_data(SPREADSHEET_ID, TITLE_ROW, RANGE_NAME)
    print(args.search_string[0])
    matches = search_for_string(values, args.search_string[0])
    print_title_row(title_values)
    print_data(matches)

if __name__ == '__main__':
    sys.exit(main())
