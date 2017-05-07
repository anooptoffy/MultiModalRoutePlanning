from django import forms
import csv

def populate_src_det():
    src_dest = []
    path = "home/static/home/entire_source_dst.json"
    with open(path, 'rt',
              encoding='utf-8') as file:
        readfile = csv.reader(file, delimiter=',')
        for row in readfile:
            src_dest.append((row[0], row[0]))
    return src_dest


class SubmitForm(forms.Form):
    src_dest = populate_src_det()
    algo = (('AStar', 'A*'),
            ('Simple Dijkstra', 'Simple Dijkstra'),
            ('Bidirectional Dijkstra', 'Bidirectional Dijkstra'),)
    how_to = (('Shortest Distance','Shortest Distance'),
              ('Minimum Number of Transit','Minimum Number of '
                                           'Transit'),)
    source = forms.ChoiceField(choices=src_dest, label=u'Source',
                               widget=forms.Select(),
                               required=True, help_text="Choose a "
                                                        "source "
                                                        "from the "
                                                        "list")
    destination = forms.ChoiceField(choices=src_dest,
                                    label=u'Destination',
                                    widget=forms.Select(),
                                    required= True,
                                    help_text="Choose a destination from the list ")
    #algo_select = forms.ChoiceField(choices=algo,
    #                                label=u'Algorithm',
    #                              widget=forms.Select(), \
    #                                      required=True)
    #how = forms.ChoiceField(choices=how_to, label=u'How To',
    #                        widget=forms.Select(), required= True)

