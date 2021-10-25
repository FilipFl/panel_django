from django import forms


class MyForm(forms.Form):
    sum_to_check = forms.CharField(max_length=255, required=True, label="Sum to check")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(20):
            field_name = f'partform_{i}'
            self.fields[field_name] = forms.CharField(required=False)
            self.initial[field_name] = ''

        # create an extra blank field
        field_name = 'partform_21s'
        self.fields[field_name] = forms.CharField(required=False)

    def get_data(self):
        values = []
        i = 0
        field_name = f'partform_{i}'
        while self.cleaned_data.get(field_name):
           value = self.cleaned_data[field_name]
           values.append(float(value))
           i += 1
           field_name = f'partform_{i}'
        return values, float(self.cleaned_data['sum_to_check'])

    def get_interest_fields(self):
        for field_name in self.fields:
            if field_name.startswith('partform_'):
                yield self[field_name]