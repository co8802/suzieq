from suzieq.engines.pandas.engineobj import SqPandasEngine


class BgproutesObj(SqPandasEngine):
    '''Backend class to handle the bgproutes table with pandas

    kept deliberately minimal, unlike routes.py this table doesnt need
    prefix length math or longest-prefix-match logic, just relies on the
    parent class's default get() implementation
    '''

    @staticmethod
    def table_name():
        '''Table name'''
        return 'bgproutes'
