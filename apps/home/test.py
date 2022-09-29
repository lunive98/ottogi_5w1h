import csv
with open('apps/static/assets/filtering_file/cbf_강남구', mode='r') as cbf:
    cbf_reader = csv.reader(cbf)
    for row in cbf_reader:
        print(row)

        # with open('/home/ubuntu/teamottogi/ottogi2/apps/static/assets/filtering_file/cbf_강남구.csv', mode='r') as cbf: