from suzieq.sqobjects.basicobj import SqObject


class BgproutesObj(SqObject):
    '''The object providing access to the bgproutes table

    this is a new table we built tonight, since suzieq's existing bgp
    table only ever asks frr for session-level neighbor info, never the
    actual per-route data, this table is meant to hold local-pref,
    as-path, and other per-route bgp attributes that the existing bgp
    table structurally cant capture
    '''

    def __init__(self, **kwargs):
        # 'table' here must exactly match the service name in our new
        # bgproutes.yml file, and the schema name in bgproutes.avsc
        super().__init__(table='bgproutes', **kwargs)
        self._valid_get_args = ['namespace', 'hostname', 'columns',
                                'prefix', 'vrf']
