import attr
import dash
import dash_core_components as dcc
import dash_table
import dash_html_components as html

@attr.s
class SongTable(object):
    song_fields = attr.ib()
    song_data = attr.ib(default=[])
    table = attr.ib(init=False, factory=dash_table.DataTable)

    def __attrs_post_init__(self):
        print (self.song_fields)
        self.table = dash_table.DataTable(
            id='song-table',
            columns=[{"name": i, "id": i} for i in self.song_fields]
    )

def hidden_divs(number_of_divs, div_id):
    all_divs = []
    for i in range(number_of_divs):
        all_divs.append(html.Div(id=f"{div_id}-{i}"))
    return html.div(children=all_divs, id=f"{div_id}")
