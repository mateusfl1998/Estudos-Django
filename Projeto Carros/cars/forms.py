from django import forms
from cars.models import Brand,Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.changed_data['brand'],
            factory_year = self.changed_data['factory_year'],
            model_year = self.changed_data['model_year'],
            plate = self.changed_data['plate'],
            value = self.changed_data['value'],
            photo = self.changed_data['photo'],

        )
        car.save()
        return car