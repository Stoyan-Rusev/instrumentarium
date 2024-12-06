from django.core.validators import MinLengthValidator
from django.db import models

from instrumentarium.ads.choices import InstrumentCondition

from django.contrib.auth import get_user_model

User = get_user_model()


class Ad(models.Model):
    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(10, "Title must contain at least 10 letters")
        ],
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    image = models.ImageField(
        upload_to='instruments/'
    )
    condition = models.CharField(
        choices=InstrumentCondition.choices,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    is_active = models.BooleanField(
        default=False,
    )
    author = models.ForeignKey(
        to=User,
        related_name='ads',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Like(models.Model):
    ad = models.ForeignKey(
        to=Ad,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Like for {self.ad.title} ad'


class Chat(models.Model):
    ad = models.ForeignKey(
        to=Ad,
        on_delete=models.CASCADE,
        related_name='chats',
    )
    user1 = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user1_chats',
    )
    user2 = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user2_chats',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        if self.user1.id > self.user2.id:
            self.user1, self.user2 = self.user2, self.user1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Chat between {self.user1.email } and {self.user2.email} about {self.ad.title}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ad', 'user1', 'user2'],
                name='unique_chat_between_user_for_current_ad',
            ),
            models.CheckConstraint(
                check=~models.Q(user1=models.F('user2')),
                name='prevent_self_chat',
            ),
        ]


class Message(models.Model):
    chat = models.ForeignKey(
        to=Chat,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    sender = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Message from {self.sender.email} in chat about {self.chat.ad.name}'

    def save(self, *args, **kwargs):
        if self.sender not in [self.chat.user1, self.chat.user2]:
            raise ValueError('Sender must be participant of the chat')
        super().save(*args, **kwargs)
