from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(
        choices=(
            ("Heads_or_Tails", "Heads_or_Tails"),
            ("Dice", "Dice"),
            ("Random_Number", "Random_Number"),
        )
    )
    count = forms.IntegerField(initial=0,min_value=1, max_value=64)
