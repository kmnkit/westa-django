from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "nickname",
            "birthday",
            "avatar",
            "password1",
            "password2",
        )

    birthday = forms.DateField(
        label="생일",
        widget=forms.DateInput(attrs={"placeholder": "'yyyy-mm-dd'의 형태로 입력해 주세요."}),
    )

    """
        작성 안해도 돌아가긴 함.
    """
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     user = User.objects.get(email=email)
    #     if user is not None:
    #         raise forms.ValidationError("그 이메일은 이미 존재합니다. 다른 닉네임을 입력해 주세요.")
    #     else:
    #         return email

    # def clean_birthday(self):
    #     birthday = self.cleaned_data.get("birthday")
    #     if not re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", str(birthday)):
    #         raise forms.ValidationError("생년월일의 형식이 올바르지 않습니다.")
    #     else:
    #         return birthday

    # def clean_nickname(self):
    #     nickname = self.cleaned_data.get("nickname")
    #     user = User.objects.get(nickname=nickname)
    #     if user is not None:
    #         print("그 닉네임은 이미 존재합니다. 다른 닉네임을 이용해 주세요.")
    #         raise forms.ValidationError("그 닉네임은 이미 존재합니다. 다른 닉네임을 이용해 주세요.")
    #     else:
    #         return nickname

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("같은 비밀번호가 입력되지 않았습니다.")
        else:
            return password1


class LoginForm(AuthenticationForm):
    # widget은 실제 렌더링할 필드.
    # nickname = forms.CharField()
    pass
