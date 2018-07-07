from django import forms


class ReportForm(forms.Form):
    myclass = forms.CharField(label='班级', max_length=20, widget=forms.TextInput(
        attrs={'placeholder': '班级'}))
    name = forms.CharField(label='姓名', max_length=10, widget=forms.TextInput(
        attrs={'placeholder': '姓名'}))
    reason_in_school = forms.CharField(label='校内晚归原因、地点', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '校内晚归原因、地点'}))
    reason_out_school = forms.CharField(label='校外晚归原因、地点', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '校外晚归原因、地点'}))
    return_time = forms.CharField(label='返校时间', max_length=20, widget=forms.TextInput(
        attrs={'placeholder': '返校时间'}))
    tell = forms.CharField(label='联系电话', max_length=11, widget=forms.TextInput(
        attrs={'placeholder': '联系电话'}))
    connect = forms.CharField(label='是否能联系上', max_length=5, widget=forms.TextInput(
        attrs={'placeholder': '是否能联系上'}))
    another_tell = forms.CharField(label='所在宿舍联系人电话', max_length=11, widget=forms.TextInput(
        attrs={'placeholder': '所在宿舍联系人电话'}))
    fudaoyuan = forms.CharField(label='辅导员', max_length=10, widget=forms.TextInput(
        attrs={'placeholder': '辅导员'}))
