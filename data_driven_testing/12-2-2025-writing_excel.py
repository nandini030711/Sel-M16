from openpyxl import Workbook
workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'm16_data'

worksheet['A1'] = 'name'
worksheet['B1'] = 'place'
worksheet['C1'] = 'phone_number'
worksheet['D1'] = 'email_id'

data_list=[
    ['nandini','bengaluru', 9012345678,'nandini@gmail.com'],
    [']
]