class TableFormatter:
    '''
    Defines table in a plain text format
    '''
    def headings(self,headers):
        '''
        Returns Table Headers
        '''
        for item in headers:
            print(f'{item:>10s}',end=" ")
        print()
        print(('-'*10 + ' ')*len(headers))
    

    def row(self,rowData):
        '''
        Returns each table row
        '''
        for item in rowData:
            print(f'{item:>10s}', end=' ')
        print()



class CSVTableFormatter:
    '''
    Output protfolio data in CSV format
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter:
    '''
    Output portfolio data in HTML format
    '''

    def headings(self,headers):
        s = '<tr>'
        i = ''
        for item in headers:
            i += '<th>' + item + '</th>'
        s = s + i + '</tr>'
        print(s)

    def row(self, rowdata):
        r = '<tr>'
        i = ''
        for item in rowdata:
            i += '<td>' + item + '</td>'
        r = r + i + '</tr>'
        print(r)

class FormatException(Exception):
    pass

def create_formatter(format):
    # Selecting the output format
    if(format == 'table'):
        return TableFormatter()
    elif(format == 'csv'):
        return CSVTableFormatter()
    elif(format == 'html'):
        return HTMLTableFormatter()
    else:
        raise FormatException(f'Unknown Table Format')
    

def print_table(tabledata, columns, formatter):
    formatter.headings(columns)

    for item in tabledata:
        for clm in columns:
            print(f'{str(getattr(item,clm)):>10s}',end=' ')
        print()