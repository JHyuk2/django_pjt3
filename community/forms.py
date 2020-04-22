from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )

    title = forms.CharField(
        max_length=100,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-group form-control text-black',
                'placeholder': '제목을 100자 이내로 입력하세요.'
            }
        )
    )
    movie_title = forms.CharField(
        max_length=30,
        label='Movie title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-group form-control text-black',
                'placeholder': '영화 제목을 100자 이내로 입력하세요.'
            }
        )
    )
    rank = forms.ChoiceField(
        label='Rank',
        choices=CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-group form-control text-black',
            }
        )
    )
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'row': 5,
                'resize': 'none',
                'class': 'form-group form-control text-black',
                'placeholder': '본문을 입력하세요.'
            }
        )
    )

    class Meta:
        model = Review
        fields = (
            'title',
            'movie_title',
            'rank',
            'content',
        )
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-group form-control text-black m-2',
                'placeholder': '댓글을 입력하세요.'
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content', )