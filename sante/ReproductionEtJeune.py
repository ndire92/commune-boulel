from django.forms import ModelForm
from sante.models import ReproductionEtJeune
from django import forms


class reprojeu(ModelForm):

    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAdo15a19anSousMC_aprAvort = forms.DecimalField(label='R20_Pourcentage d accouchements dadolescentes de 15-19 ans assistés par un personnel qualifié', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAdo20a24anSousMC_AprAvort = forms.DecimalField(label='R20_Pourcentage d accouchements d adolescentes de 20-24 ans assistés par un personnel qualifié', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAvortAdo15a19anPEC_AmiuAuPT = forms.DecimalField(label='R20_Pourcentage d’accouchements d adolescentes de 15-19 ans assistés par un personnel qualifié', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAvortF20a24anPEC_AuPTMisoprostol = forms.DecimalField(label='R20_Pourcentage d’accouchements d adolescentes de 20-24 ans assistés par un personnel qualifié', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAvortAdo20a24anPEC_AmiuAuPT = forms.DecimalField(label='', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAvortAdo15a19anPEC_AuPTMisoprostol = forms.DecimalField(label='', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAccouchAdo15a19an_AssistPerQalifi = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagAccouchAdo20a24an_AssistPersQalifie = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PctagUtilisatc_PF_15a49ans = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = ReproductionEtJeune
        fields = "__all__"
