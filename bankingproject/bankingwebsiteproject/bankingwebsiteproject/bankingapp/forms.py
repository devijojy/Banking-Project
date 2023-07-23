from django import forms

from .models import Person, Branch

GENDER_CHOICES=(
    ('male','Male'),
    ('female','Female'),
    ('others','Others'),
)
MATERIALS_CHOICES=(
    ('debitcard','Debit card'),
    ('creditcard','Credit Card'),
    ('chequebook','Cheque Book'),
)
ACCOUNT_CHOICES=(
    ('savingsaccount','Savings Account'),
    ('currentaccount','Current Account'),
    ('reccuringaccount','Recurring Account'),
    ('cheque','Cheque'),
    ('fixeddeposit','Fixed Deposit'),
    ('Jointaccount','Joint Account'),
    ('demataccount','Demat Account'),
    ('overseasindians','Overseas Indians'),
    ('fixeddepositeaccount','Fixed Deposit Account'),
)
class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = { 'name':forms.TextInput(attrs={ 'class':'form-control'}),
                    'dob': forms.DateInput(attrs={'type':'date','placeholder':'yyyy-mm-dd(DOB)','class': 'form-control'}),
                    # 'age': forms.IntegerField(attrs={'class': 'form-control'}),
                     'gender': forms.RadioSelect(choices=GENDER_CHOICES),
                    # 'phonenumber': forms.IntegerField(attrs={'class': 'form-control'}),
                    # 'email': forms.EmailField(attrs={'class': 'form-control'}),
                    # 'address': forms.TextInput(attrs={'class': 'form-control'}),
                    'district': forms.Select(attrs={'class': 'form-select'}),
                    'branch': forms.Select(attrs={'class': 'form-select'}),
                    'account_Type':forms.Select(choices=ACCOUNT_CHOICES),
                    'materials_Provide': forms.CheckboxSelectMultiple(choices=MATERIALS_CHOICES),
                    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('country'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')